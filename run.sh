#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install Python on Debian-based systems
install_python_debian() {
    echo "Installing Python on Debian-based system..."
    sudo apt update
    sudo apt install -y python3 python3-venv python3-pip
}

# Function to install Python on Fedora-based systems
install_python_fedora() {
    echo "Installing Python on Fedora-based system..."
    sudo dnf install -y python3 python3-venv python3-pip
}

# Function to install Python on Arch-based systems
install_python_arch() {
    echo "Installing Python on Arch-based system..."
    sudo pacman -Syu --noconfirm python python-virtualenv python-pip
}

# Check the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux OS"
    if command_exists apt; then
        install_python_debian
    elif command_exists dnf; then
        install_python_fedora
    elif command_exists pacman; then
        install_python_arch
    else
        echo "Unsupported Linux distribution"
        exit 1
    fi
    PYTHON=python3
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

# Create and activate virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Go in the app directory
cd vark_quiz

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

# Run the development server
echo "Starting the development server..."
python manage.py runserver