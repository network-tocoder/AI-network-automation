import os
import logging
import logging.config
import yaml
from typing import Dict, Any

# Get the absolute path of the logger.yml file
logger_config_path: str = os.path.join(os.path.dirname(__file__), 'logger.yml')

# Load the logging configuration from the logger.yml file
with open(logger_config_path, 'r') as f:
    config: Dict[str, Any] = yaml.safe_load(f.read())

# Configure the logger using the loaded configuration
logging.config.dictConfig(config)

# Create a logger with the name matching the file
logger: logging.Logger = logging.getLogger(__name__)
