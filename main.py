import http.client
import json
import sseclient
import dotenv
import sys
import time

dotenv.load_dotenv()

token = dotenv.get_key(".env", "TOKEN") if dotenv.get_key(".env", "TOKEN") else input("Enter token: ")

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'een-US,en;q=0.8',
    'Origin': 'https://fish.audio',
    'Priority': 'u=1, i',
    'Referer': 'https://aihumanize.io/',
    'Sec-Ch-Ua': '"Not;A=Brand";v="99", "Brave";v="139", "Chromium";v="139"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Gpc': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Cookie': f'token={token}',
    'Content-Type': 'application/json'
}
while True:
    print("\n\n")
    prompt = input("Enter your prompt: ")
    conn = http.client.HTTPSConnection("aihumanize.io")
    payload = json.dumps({
        "prompt": prompt,
        "token": "eyJhbGciOiJIUzUxMiJ9.eyJpZCI6MTc1NjM1OTUyNjAyMjA3NzgxLCJuYW1lIjoiVGVtcG9yYXJ5IHVzZXIiLCJ0eXBlIjoyLCJkZXZpY2UiOjEsInN1cGVyUGFzc3dvcmRGbGFnIjpmYWxzZSwiaWF0IjoxNzU2MzU5NTI3LCJleHAiOjE3NTY5NjQzMjd9.YscMmBCouxGlW7V4XZIYnauldrLmXRHYFI_yDdNe6_U1m5Gtk6-LC4FI1ehROI8sWbkDIpAtvF7_1JNcB19RHA",
        "auto": 0,
        "cjtype": 0,
        "model": 0
    })
    conn.request("POST", "/dev/outstream", payload, headers)
    res = conn.getresponse()
    print("\nResponse:\n")
    
    sys.stdout.flush()
    
    client = sseclient.SSEClient(res) #type:ignore
    for event in client.events():
        event_data = json.loads(event.data)
        if event_data.get("type") == "success":
            print(event_data.get("msg"), end="", flush=True)
        if event_data.get("type") == "final_words":
            print(f"\n\nFinal word count: {event_data.get('msg')}")
        if event_data.get("type") == "language":
            print(f"Language: {event_data.get('msg')}")
        if event_data.get("type") == "final_ai_score":
            print(f"Final AI score: {event_data.get('msg')}")