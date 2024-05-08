import os
from dotenv import load_dotenv
from flask_cors import CORS

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.run("0.0.0.0",port=5001)