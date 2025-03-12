import os
from datetime import datetime

# Simulate getting project name from API trigger
project_name = os.getenv("PROJECT_NAME", "Unknown Project")

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log to a file
with open("log.txt", "a") as f:
    f.write(f"{timestamp} - Project Submitted: {project_name}\n")

print(f"Project {project_name} submitted at {timestamp}")
