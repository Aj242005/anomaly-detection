import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import cv2
from pathlib import Path


class AlertSystem:
    def __init__(self, config):
        self.config = config
        self.last_alert_time = datetime.min

    def should_send_alert(self) -> bool:
        current_time = datetime.now()
        if (current_time - self.last_alert_time).total_seconds() > self.config.EMAIL_SETTINGS['alert_cooldown']:
            self.last_alert_time = current_time
            return True
        return False

    def send_email_alert(self, probability: float, frame) -> bool:
        if not self.should_send_alert():
            return False

        # Save frame
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = Path(self.config.PATHS['recording_dir']) / f"alert_{timestamp}.jpg"
        cv2.imwrite(str(image_path), frame)

        # Prepare email
        msg = MIMEMultipart()
        msg['Subject'] = f'⚠️ Anomaly Detected! (Confidence: {probability:.2%})'
        msg['From'] = self.config.EMAIL_SETTINGS['sender_email']
        msg['To'] = self.config.EMAIL_SETTINGS['recipient_email']

        body = f"""
        Anomaly Detection Alert

        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Confidence: {probability:.2%}
        Location: System Camera

        Please check the system dashboard for more details.
        """

        msg.attach(MIMEText(body, 'plain'))

        # Attach image
        with open(image_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-Disposition', 'attachment', filename=image_path.name)
            msg.attach(img)

        # Send email
        try:
            with smtplib.SMTP(self.config.EMAIL_SETTINGS['smtp_server'],
                              self.config.EMAIL_SETTINGS['smtp_port']) as server:
                server.starttls()
                server.login(
                    self.config.EMAIL_SETTINGS['sender_email'],
                    self.config.EMAIL_SETTINGS['sender_password']
                )
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Failed to send email alert: {e}")
            return False