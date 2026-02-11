# MediTriage

MediTriage is an AI-powered self-triage tool designed to help users identify potential conditions based on their symptoms.

## Project Structure
- **BACKEND/**: Flask API for disease prediction.
- **FRONTEND/**: HTML/CSS/JS frontend.
- **ML/**: Machine learning scripts (and dataset).

## How to Run

### Prerequisite
Ensure you have the virtual environment set up:
```bash
python3 -m venv venv
./venv/bin/pip install -r BACKEND/requirements.txt
```

### 1. Start the Backend Server
Open a terminal in the project root (`MediTriage/`) and run:
```bash
./venv/bin/python3 BACKEND/app.py
```
You should see output indicating the server is running on `http://127.0.0.1:5000`.

### 2. Open the Frontend
Open the `FRONTEND/sick_page/sick.html` file in your web browser.
You can do this by double-clicking the file in your file explorer or running:
```bash
xdg-open FRONTEND/sick_page/sick.html  # Linux
open FRONTEND/sick_page/sick.html      # macOS
start FRONTEND/sick_page/sick.html     # Windows
```

## Mock Mode
Since no dataset was provided, the app runs in **Smart Mock Mode**:
- **Fever + Cough** → **Flu**
- **Chest Pain / Shortness of Breath** → **Pneumonia**
- **Headache + Nausea** → **Migraine**
- **Runny Nose** → **Common Cold**
