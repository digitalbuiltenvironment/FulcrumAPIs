# O2 Bot Assistant
Program that uses Fulcrum APIs to automatically perform certain tasks

## Project Setup
In the project base directory, create a .env file and input the service account credentials:
```
SVC_USERNAME='<svc_username>'
SVC_PASSWORD='<svc_password>'
```
Create Python virtual environment in the base directory:
```
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat  # cmd
# or
source .venv/bin/activate   # bash

# Install requirements
pip install -r requirements.txt
```

## Running the Script
Run `python main.py`

GUI will automatically pop out.

Functions right now include:
1) Create Form
2) Add Users (coming soon)
