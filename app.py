import os
from flask import g, Flask, request

from presentation.view.login_view import login_view

app = Flask(__name__)

app.register_blueprint(login_view)


@app.before_request
def before_request():
    g.locale = request.headers.get('Accept-Language')
    g.user_agent = request.headers.get('User-Agent')


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
