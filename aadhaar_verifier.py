import os
from dotenv import load_dotenv
from config import BASE_DIR


dotenv_path = os.path.join(BASE_DIR, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from backend import create_app, api

app = create_app(os.getenv(key="FLASK_CONFIG", default="default"))
api.init_app(app)

PORT = app.config["PORT"]
DEBUG = app.config["DEBUG"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
