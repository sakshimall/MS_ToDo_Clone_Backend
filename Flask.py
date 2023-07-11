from flask import Flask, request
from flask_cors import CORS, cross_origin
from database import getDataFromMongo, postDataFromMongo

app = Flask(__name__)
CORS(app)

@cross_origin
@app.route('/', methods = ['POST', 'GET'])
def home_page():
    if request.method == 'GET':
        print("flask get = ",getDataFromMongo())
        return getDataFromMongo()
    if request.method == 'POST':
       post_data = request.json
       print("flask post = ",post_data)
       postDataFromMongo(post_data)
       return post_data

if __name__ == "__main__":
    app.run(debug=True, port=9999)