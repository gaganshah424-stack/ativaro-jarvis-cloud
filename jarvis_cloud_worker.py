import os
import time
import json
import requests
from datetime import datetime

# Read from Environment Variables or Cloud Secrets
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN", "EAAUjYJZBEC58BSyR6YpmvcGJfC8CZCIRcGdsHOQQpzCpoPmJeh8fz1MwI1sjZCXDMR8gdWt7I20khFlxMnSVJERUqEjhaLUcbRMquhjEca5ZA7dbOJuKj0QTCOrD74hFQzaiJwbCYbvReZCVtdJmmUgphuDKZAX9VAZBEfVTDGRvrAdhNQ2Y8lhP0d5GexRZANvfNLY6nM5M")
PAGE_ID = os.getenv("PAGE_ID", "1176540182219032")
IG_ID = os.getenv("IG_ID", "17841428319394361")

print("⚡⚡⚡ ATIVARO 24/7 CLOUD WORKER IS ACTIVE ON CLOUD SERVER! ⚡⚡⚡")
print("[*] Running in cloud 24/7 independently of local laptop.")
print(f"[*] Facebook Page ID: {PAGE_ID} | Instagram ID: {IG_ID}")

while True:
    try:
        # 1-second polling loop
        time.sleep(1)
    except Exception as e:
        print(f"[!] Worker Error: {e}")
        time.sleep(5)
