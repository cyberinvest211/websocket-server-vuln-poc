# poc.py
import websocket
import json
import time

print("[*] PoC is starting...")

ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:9001")

payload = {"check": "poc_test"}

ws.send(json.dumps(payload))
print("[PoC result]")
print(payload)

time.sleep(1)
ws.close()
