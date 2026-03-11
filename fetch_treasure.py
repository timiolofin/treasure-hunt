import os
import urllib.request

token = os.environ.get("TREASURE_KEY")

if not token:
    print("❌ TREASURE_KEY not set in environment.")
    exit(1)

url = "https://raw.githubusercontent.com/iyad-obeid/secret-message/main/treasure.txt"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})

try:
    with urllib.request.urlopen(req) as response:
        content = response.read().decode("utf-8")
        print("✅ SUCCESS!")
        print("========== SECRET MESSAGE ==========")
        print(content)
        print("====================================")
except urllib.error.HTTPError as e:
    print(f"❌ HTTP Error {e.code}: {e.reason}")
