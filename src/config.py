from pathlib import Path
import yaml
from dotenv import load_dotenv
import os


class Config:
    def __init__(self):
        load_dotenv()

        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)

        self.EMAIL_SETTINGS = {
            "smtp_server": config['email_settings']['smtp_server'],
            "smtp_port": config['email_settings']['smtp_port'],
            "sender_email": os.getenv('SENDER_EMAIL'),
            "sender_password": os.getenv('EMAIL_APP_PASSWORD'),
            "recipient_email": config['email_settings']['recipient_email'],
            "alert_cooldown": config['email_settings']['alert_cooldown']
        }

        self.MODEL_SETTINGS = config['model_settings']

        # Create directories
        for dir_name in config['paths'].values():
            Path(dir_name).mkdir(exist_ok=True)

        self.PATHS = config['paths']