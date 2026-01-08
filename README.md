# websocket-server 0.6.4 — Input Validation Issue

This repository contains a simple proof of concept demonstrating an
input handling issue in the Python package `websocket-server`
version 0.6.4.

## Overview
The WebSocket server processes client-supplied messages without proper
input validation. Incoming messages are decoded and passed directly to
JSON parsing logic without sufficient checks.

## Technical Details
The issue occurs when untrusted WebSocket messages are handled without:

- Input size limits
- Format or schema validation
- Robust exception handling

This may lead to unexpected server behavior when malformed or specially
crafted payloads are sent by a remote client.

## Affected Component
websocket_server/websocket_server.py
WebSocketServer._message_received



## Impact
A remote client may:
- Trigger server-side exceptions
- Cause unstable or unexpected behavior
- Potentially expose internal error states depending on configuration

## Proof of Concept
Included files:
- `vuln.py` — minimal vulnerable WebSocket server example
- `poc.py` — client sending crafted input to the server

The PoC demonstrates how unvalidated input is processed by the server.

## Affected Version
- websocket-server 0.6.4

## Status
- No official fix at the time of writing

## Notes
This repository is intended for educational and security research
purposes only.
