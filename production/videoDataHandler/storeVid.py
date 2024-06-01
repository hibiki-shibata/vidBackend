from flask import jsonify
import os


class StoreVid:
    def __init__(self, app) -> None:
        self.app = app

        UPLOAD_FOLDER: str = 'uploadedVideos'
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    async def index(self, request) -> tuple:
        videofile = request.files['video']

        isValidFile: bool = await self.validate_file(videofile)
        
        if isValidFile is not True:
            return  jsonify({'error': 'No file part in the request'}), 400
        else:
            return await self.store_file(videofile)



    async def validate_file(self, file) -> bool:
    
        if 'video' not in file.content_type:
            return False
        elif file.filename == '':
            return False
        else:
            return True
                

    async def store_file(self, file) -> tuple:
        if file:
            filename = file.filename
            file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return jsonify({'filename': filename}), 200