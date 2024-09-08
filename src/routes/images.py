import io
import os
import zipfile

from flask import Blueprint, request, jsonify, Response
from flask.views import MethodView

images_bp = Blueprint("images", __name__, url_prefix="/images")

class ImageAPI(MethodView):
    
    def get(self):
        theme = request.args.get('theme', '')
        subtheme = request.args.get('subtheme', '')
        
        print(theme)
        print(subtheme)

        image_directory = f'src/static/images/{theme}/{subtheme}'
        zip_filename = 'display_images.zip'
        matching_files = []

        for filename in os.listdir(image_directory):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                matching_files.append(filename)
        
        if not matching_files:
            return jsonify({"error": "No images found matching the keyword."}), 404

        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zip_file:
            for filename in matching_files:
                zip_file.write(os.path.join(image_directory, filename), filename)
        
        memory_file.seek(0)
        return Response(memory_file, mimetype='application/zip', headers={"Content-Disposition": f"attachment;filename={zip_filename}"})    
    
image_view = ImageAPI.as_view('image_api')
images_bp.add_url_rule('/', view_func=image_view, methods=['GET'])