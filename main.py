# from flask import Flask
# import time
# import asyncio

# app = Flask(__name__)

# @app.get("/")
# async def hello_world():
#     print("request comes!")
#     await asyncio.sleep(10000)
#     print("awoke from the sleep")
#     a = "<p>Hello, World!!!!!</p>"
#     return a


# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=4000)




from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
# import asyncio

from production.videoDataHandler.storeVid import StoreVid
# import os

app: Flask = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
async def upload_file() -> jsonify:
    storevid = StoreVid(app) 
    return await storevid.index(request)

@app.route('/video', methods=['GET'])
def get_video():
    try:
        print("requst arrived!!!")
        filename = "test.mov"
        UPLOAD_FOLDER: str = 'production/Database/uploaded'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(port=4000, debug=True)

