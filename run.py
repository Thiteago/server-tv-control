from app import create_app
from dotenv import load_dotenv
import os

app = create_app()
load_dotenv()

if __name__ == '__main__':
  app.run(host=f"{os.getenv('IP_LOCAL_MACHINE')}", port=5000)