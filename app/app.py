from flask import Flask, jsonify
from api import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)

    @app.errorhandler(404)
    def not_found(error):
        err = {'message': "Resource doesn't exist."}
        return jsonify(**err)

    return app


app = create_app()

if __name__ == "__main__":
    app.run()

