import os
from flask import Flask

from presentation.view.login_view import login_view

app = Flask(__name__)

app.register_blueprint(login_view)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
