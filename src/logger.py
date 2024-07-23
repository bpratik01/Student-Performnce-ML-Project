import logging  
from pathlib import Path 
from datetime import datetime
 
# Logging is a way to store information about your script and track events that occur.
# It can be used for debugging and understanding the flow of a program.


LOG_FILE = f'{datetime.now().strftime("%Y-%m-%d")}.log'


# Path.cwd() returns the current working directory.
# We combine this with 'logs' to create a path for the logs directory.
logs_path = Path.cwd() / 'logs'

# exist_ok=True avoids an error if the directory exists.
logs_path.mkdir(parents=True, exist_ok=True) # Create the logs directory if it does not exist.


LOG_FILE_PATH = logs_path / LOG_FILE

# Configure the logging settings.
# logging.basicConfig() sets up the basic configuration for logging.
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the file to which logs will be written.
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the format of log messages.
    # '%(asctime)s' adds a timestamp to each log message.
    # '%(name)s' adds the name of the logger.
    # '%(levelname)s' adds the severity level of the log message (e.g., INFO, DEBUG, ERROR).
    # '%(message)s' adds the actual log message.
    level=logging.INFO  # Set the logging level to INFO.
    # This means that all messages of this level and above (INFO, WARNING, ERROR, CRITICAL) will be logged.
)
