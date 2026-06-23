from loguru import logger
import sys

# 1. Setup where the logs go (Optional: defaults to writing beautifully to the console)
logger.remove() # Remove default console handler if customizing
logger.add(sys.stderr, level="INFO") # Print to terminal
logger.add("app_loguru.log", rotation="500 MB", level="DEBUG") # Log to file, auto-split file when it hits 500MB

