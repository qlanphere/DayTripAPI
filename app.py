from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from controllers import trips

app = Flask(__name__)



CORS(app)

@app.route('/')
def home():
    return 'Welcome to London Day Trip Planner'

@app.route('/trips', methods = ['GET', 'POST'])
def trips_handler():
    fns = {
        'GET': trips.index,
        'POST': trips.create
    }
    resp = fns[request.method](request)
    return jsonify(resp)


# @app.route('/trips/<int:trip_id>')
# def trip_handler(trip_id):
#     pass

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({f'message': f"Oops...{err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"it's not you its us"}), 500



if __name__ == '__main__':
    app.run(debug=True)
