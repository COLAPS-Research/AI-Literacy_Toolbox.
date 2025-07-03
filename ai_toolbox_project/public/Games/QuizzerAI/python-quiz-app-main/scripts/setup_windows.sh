#!/bin/bash

cd "$(git rev-parse --show-toplevel)"

if command -v python3.11 >/dev/null 2>&1; then
    # If python3.11 is directly available
    PYTHON_CMD="python3.11"
else
    # Fall back to "python" and check its version
    if command -v py -3.11 >/dev/null 2>&1; then
        PY_VERSION=$(python --version 2>&1 | awk '{print $2}')
        IFS='.' read -ra VER <<< "$PY_VERSION"

        # Check that the major version is 3 and minor is at least 11
        if [ "${VER[0]}" -eq 3 ] && [ "${VER[1]}" -ge 11 ]; then
            PYTHON_CMD="python"
        else
            echo "Python 3.11 or newer is required. Found: $PY_VERSION"
            exit 1
        fi
    else
        echo "No suitable Python (3.11+) found. Please install Python 3.11 or newer."
        exit 1
    fi
fi

if [ -d "venv" ]; then
    echo "Activating existing venv..."
    source venv/Scripts/activate
elif [ -d ".venv" ]; then
    echo "Activating existing .venv..."
    source .venv/Scripts/activate
else
    echo "No virtual environment found. Creating one..."
    py -3.11 -m venv venv
    source venv/Scripts/activate
fi

pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Virtual environment is activated, and dependencies are installed."
