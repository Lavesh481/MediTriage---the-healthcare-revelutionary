
import sys
import os

# Simulate Vercel environment: CWD is project root
print(f"CWD: {os.getcwd()}")
print(f"PYTHONPATH: {sys.path}")

try:
    # This is what api/index.py does
    from BACKEND.app import app
    print("SUCCESS: Imported app")
except Exception as e:
    print(f"FAILURE: {e}")
