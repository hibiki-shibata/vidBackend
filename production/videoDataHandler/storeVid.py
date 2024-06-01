from flask import jsonify
import os


class StoreVid:
    def __init__(self, app) -> None:
        self.app = app

        UPLOAD_FOLDER: str = 'uploadedVideos'
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    def index(self, request) -> tuple:
        videofile = request.files['video']
        
        if self.validate_file(videofile) is not False:
            return  jsonify({'error': 'No file part in the request'}), 400
        else:
            return self.store_file(videofile)



    def validate_file(self, file) -> bool:
        if 'video' not in file:
            return False
        elif file.filename == '':
            return False
        else:
            return True
                

    def store_file(self, file) -> tuple:
        if file:
            filename = file.filename
            file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return jsonify({'filename': filename}), 200