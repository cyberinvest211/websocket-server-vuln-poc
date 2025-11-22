# vuln.py
from websocket_server import WebsocketServer
import json

print("WebSocket weak server: ws://127.0.0.1:9001")

def on_message(client, server, message):
    print("[Server] Accaept :", message)
    try:
        # ❌ Zaiflik: kiruvchi xabar bevosita json.loads() ga yuborilmoqda
        # Hech qanday filtering, size check, try/except yo‘q
        data = json.loads(message)
    except:
        pass

server = WebsocketServer(9001, host="127.0.0.1")
server.set_fn_message_received(on_message)
server.run_forever()
