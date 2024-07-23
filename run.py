from app import create_app

import os

app = create_app()

if __name__ == '__main__':
  app.run(host=f"{os.getenv('IP_LOCAL_MACHINE')}", port=5000)