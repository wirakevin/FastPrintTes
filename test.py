import requests
import hashlib
from datetime import datetime

# -----------------------------
# Step 1: Generate dynamic username/password
# -----------------------------
today = datetime.today()
username = "tesprogrammer020226C01"
# password_plain = f"bisacoding-{today.month}-{today.day}-{str(today.year)[-2:]}"
password_plain = f"bisacoding-{today.day:02d}-{today.month:02d}-{str(today.year)[-2:]}"
# password_plain = "bisacoding-2-1-26"
password_md5 = hashlib.md5(password_plain.encode()).hexdigest()

# -----------------------------
# Step 2: Use requests session
# -----------------------------
session = requests.Session()

url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

# Set headers including credentials
data = {
    "username": "tesprogrammer020226C01",  # copy the server username exactly
    "password": password_md5
}

# Send POST request
response = session.post(url, data=data)

# -----------------------------
# Step 3: Debug output
# -----------------------------
print("Status code:", response.status_code)
print("Response headers:", response.headers)
print("Cookies:", session.cookies.get_dict())
print("Response JSON:", response.json())