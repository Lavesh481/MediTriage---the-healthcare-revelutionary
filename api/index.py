import sys
import os

# Add the parent directory to sys.path so we can import BACKEND
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BACKEND.app import app

if __name__ == "__main__":
    app.run()
