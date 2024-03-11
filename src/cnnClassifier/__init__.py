import os
import sys 
import logging 
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s:%(message)s]"

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


log_dir = "log"

log_path = os.path.join(log_dir,f"running_logs_{current_time}.log")
os.makedirs("log",
            exist_ok=True 
                              )



logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    
    #logging.FileHandler(log_filepath): Sends log messages to the specified file.
    #logging.StreamHandler(sys.stdout): Sends log messages to the standard output (console).
    handlers= [
                logging.FileHandler(log_path),
                logging.StreamHandler(sys.stdout)
        
    ]   
    
)


logger = logging.getLogger("cnnClassifier")