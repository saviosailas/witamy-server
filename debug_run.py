#! .venv/bin/python
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.getcwd(), ".env"), verbose=True, override=True)

from witamy_server import app

if __name__ == "__main__":
    app.run(debug=True)
