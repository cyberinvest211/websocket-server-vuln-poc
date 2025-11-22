# websocket-server 0.6.4 — Input Validation Vulnerability (PoC)

This repository contains a proof‑of‑concept demonstrating an input
validation flaw in the Python package **websocket-server (v0.6.4)**.

## Description
The server blindly decodes untrusted WebSocket messages using:

    opcode_handler(self, message_bytes.decode('utf8'))

and passes them directly into JSON parsing without any validation:

    data = json.loads(message)

No size limits, no schema validation and no exception control are used.
A remote client may send specially crafted payloads that cause:

- Server-side exceptions
- Denial of Service (DoS)
- Unexpected handling of malformed frames

## Files
- `vuln.py` — vulnerable websocket server
- `poc.py` — proof‑of‑concept client exploiting the issue

## Discoverer
Muhammadrasul (your name)

## Version
Affected: websocket-server 0.6.4
Fixed: No official fix as of now
