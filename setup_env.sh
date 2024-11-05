#!/bin/bash

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install required libraries
pip install -r requirements.txt
