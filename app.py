from flask import Flask, render_template, request, jsonify , send_from_directory
import os
from chat import get_response

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("base.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/favicon.ico', '', as_static=True)


@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Extract message from JSON payload
        text = request.get_json().get('message')
        
        # Call chatbot function to get response
        response = get_response(text)
        
        # Construct response message
        message = {'answer': response}
        
        # Return response as JSON
        return jsonify(message), 200
    except Exception as e:
        # Return error message if an exception occurs
        error_message = {'error': str(e)}
        return jsonify(error_message), 500


