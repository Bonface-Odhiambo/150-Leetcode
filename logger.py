from datetime import datetime
import json

class Logger:
    """
    A class for handling application logging with different severity levels
    and output formats.
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.log_count = 0
        self.severity_levels = {
            'INFO': 0,
            'WARNING': 1,
            'ERROR': 2,
            'CRITICAL': 3
        }

    def log(self, message: str, level: str = 'INFO') -> None:
        """Log a message with timestamp and severity level"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            'timestamp': timestamp,
            'level': level,
            'message': message,
            'log_id': self.log_count
        }
        
        with open(self.filename, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        self.log_count += 1
        
        # Print critical errors to console
        if level == 'CRITICAL':
            print(f"CRITICAL ERROR: {message}")

    def clear_logs(self) -> None:
        """Clear all logs from file"""
        open(self.filename, 'w').close()
        self.log_count = 0

# Usage example:
app_logger = Logger('app.log')
app_logger.log("Application started", "INFO")
app_logger.log("Database connection failed", "CRITICAL")