# src/__init__.py
from .config import Config
from .models import AnomalyDetector
from .data import VideoDataset
from .alerts import AlertSystem
from .logger import EventLogger
from .ui import AnomalyDetectionUI

__version__ = '1.0.0'

__all__ = [
    'Config',
    'AnomalyDetector',
    'VideoDataset',
    'AlertSystem',
    'EventLogger',
    'AnomalyDetectionUI',
]

# The version info for the project
VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION_PATCH = 0

# Import utility functions
from .utils import setup_logging, load_config

# Define package metadata
__title__ = 'anomaly_detection'
__description__ = 'Real-time anomaly detection system with email alerts'
__author__ = 'Your Name'
__author_email__ = 'your.email@example.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2024'