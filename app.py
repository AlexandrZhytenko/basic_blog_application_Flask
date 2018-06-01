from flaskr import create_app
from flaskr.db import init_db

if __name__ == "__main__":
    init_db()
    app = create_app()
    app.run()