#!/bin/bash
echo "Launching HarmonyHub AI..."
uvicorn harmonyhub_ai_agents:app --host 0.0.0.0 --port 8000
