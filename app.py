from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app, resources={r"/generate-design": {"origins": "*"}})


@app.route('/generate-design', methods=['POST'])
def generate_design():
    data = request.json

    # Extract image and json
    image_data = data.get('image')
    design_data = data.get('designData')

    ## Extract image
    if image_data:
        image_bytes = base64.b64decode(image_data.split(',')[1])  # Decodifica la parte base64
        with open("received_design.png", "wb") as image_file:
            image_file.write(image_bytes)
    
    # Update JSON
    design_data['status'] = 'success'
    design_data['message'] = 'Design received and processed'
    
    return jsonify(design_data)
    
 

if __name__ == '__main__':
    app.run()
