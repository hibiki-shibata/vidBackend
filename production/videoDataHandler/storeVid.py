from flask import jsonify
import os


class StoreVid:
    def __init__(self, app) -> None:
        self.app = app

        UPLOAD_FOLDER: str = 'production/Database/uploaded'
        if not os.path.exists(UPLOAD_FOLDER):
            
            os.makedirs(UPLOAD_FOLDER)
            

        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    async def index(self, request) -> tuple:
        videofile = request.files['video']

        isValidFile: bool = await self.validate_file(videofile)
        
        if isValidFile is not True:
            return  jsonify({'error': 'No uploadedFile part in the request'}), 400
        else:
            return await self.store_file(videofile)



    async def validate_file(self, uploadedFile) -> bool:
    
        if 'video' not in uploadedFile.content_type:
            return False
        elif uploadedFile.filename == '':
            return False
        else:
            return True
                

    async def store_file(self, uploadedFile) -> tuple:
        if uploadedFile:
            filename = uploadedFile.filename
            # UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))

            file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
            uploadedFile.save(file_path)
            return jsonify({'filename': filename}), 200