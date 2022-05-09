import os

from flask import Flask
from flask_cors import CORS

# Blueprints
from presentation.view.login_view import login_view
from presentation.view.register_view import register_view
from presentation.view.list_view import list_view
from presentation.view.task_view import task_view

app = Flask(__name__)

cors_config = {
    'Access-Control-Allow-Credentials': 'true'
}


CORS(app, supports_credentials=True, resources={r"/api/*": {
    "origins": "*",
    "methods": ["GET", "POST"],
    "allow-headers": ["Authorization", "Content-Type", "multipart/form-data"]
}})

app.register_blueprint(login_view)
app.register_blueprint(register_view)
app.register_blueprint(list_view)
app.register_blueprint(task_view)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
