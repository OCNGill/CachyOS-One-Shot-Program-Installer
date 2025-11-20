#!/bin/bash

# CachyOS One-Shot Program Installer Launcher
# Checks dependencies and launches the Streamlit app

echo "🚀 Initializing CachyOS One-Shot Program Installer..."

# 1. Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install it first."
    exit 1
fi

# 2. Check for AUR helper
AUR_HELPER=""
if command -v paru &> /dev/null; then
    AUR_HELPER="paru"
elif command -v yay &> /dev/null; then
    AUR_HELPER="yay"
else
    echo "⚠️ No AUR helper (paru/yay) found. AUR support will be disabled."
fi

echo "✅ AUR Helper detected: $AUR_HELPER"

# 3. Check/Install Python dependencies
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found!"
    exit 1
fi

# Create venv if it doesn't exist (optional but recommended)
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "📦 Checking python dependencies..."
pip install -r requirements.txt > /dev/null

# 4. Sudo Authentication (Cache credentials)
echo "🔐 Requesting sudo privileges for installation tasks..."
if sudo -v; then
    echo "✅ Sudo privileges acquired."
else
    echo "❌ Sudo authentication failed."
    exit 1
fi

# Keep sudo alive in background
(while true; do sudo -v; sleep 60; done) &
SUDO_PID=$!

# Trap to kill sudo keepalive on exit
trap "kill $SUDO_PID" EXIT

# 5. Launch Streamlit App
echo "🌟 Launching Interface..."
streamlit run app.py
