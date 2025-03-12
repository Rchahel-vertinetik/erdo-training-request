import os

# Get variables from environment
project_name = os.getenv("PROJECT_NAME", "Unknown Project")
user_id = os.getenv("USER_ID", "0000")
request_date = os.getenv("REQUEST_DATE", "2025-01-01")

# Print values (for debugging in GitHub Actions logs)
print(f"🔹 Project Name: {project_name}")
print(f"🔹 User ID: {user_id}")
print(f"🔹 Request Date: {request_date}")

# Log the request
with open("requests_log.txt", "a") as log_file:
    log_file.write(f"{request_date} - User {user_id} requested {project_name}\n")

print("✅ Script executed successfully.")
