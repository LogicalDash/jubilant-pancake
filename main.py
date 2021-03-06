"""Flask app for edit distance

For debugging, run like:

PYTHONPATH=$PWD FLASK_APP=main.py flask run

Then access it at:

http://localhost:5000/

"""

from flask import Flask, request, Response
from editd import edit_distance


def create_app():
    """Create and return a Flask app for computing edit distance"""
    app = Flask("jubilant-pancake", static_url_path='/static')

    @app.route("/editd/<source>/<target>")
    def edit_distance_service(source, target):
        return str(edit_distance(source, target))

    @app.route("/editd")
    def edit_distance_request():
        if 'source' not in request.args or 'target' not in request.args:
            return Response('Requires source and target', status=500)
        return str(edit_distance(request.args['source'], request.args['target']))

    @app.route("/")
    def root():
        return app.send_static_file("index.html")

    return app


if __name__ == '__main__':
    create_app()
