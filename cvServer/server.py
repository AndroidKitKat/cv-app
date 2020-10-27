from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/identify", methods=["PUT"])
@cross_origin()
def identify():
    data = request.json
    # data contains a base64 encoded JPEG of the user submitted photo
    # do the actual CV work here
    if data:
        print(data)
        
    return "This is from a post"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8008)