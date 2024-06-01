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




from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio

from videoDataHandler.storeVid import StoreVid
# import os

app: Flask = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
async def upload_file() -> jsonify:
    storevid = StoreVid(app) 
    return await storevid.index(request)

if __name__ == '__main__':
    app.run(port=4000, debug=True)

