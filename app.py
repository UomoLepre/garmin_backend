# flask-api/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
#import multimodal_garment_designer 


app = Flask(__name__)
CORS(app, resources={r"/generate-design": {"origins": "*"}})

app.config['DEBUG'] = True

@app.route('/generate-design', methods=['POST'])
def generate_design():
    #data = request.json
    #text_input = data["text"]  
    #draw_input = data["drawing"]

    #return output
    return jsonify(output="Hello world")
    #call to the model
    #output = multimodal_garment_designer.generate(input_data)
    
 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
