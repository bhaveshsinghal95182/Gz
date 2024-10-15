from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__, 
            template_folder='.',  # Use current directory for templates
            static_folder='.')     # Use current directory for static files

@app.route("/")
def index():
    return render_template('chat.html')  # This will now correctly find chat.html

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]  # Get the message from the form
    response = get_chat_response(msg)  # Get the chat response
    return response  # Return JSON response

def get_chat_response(text):
    try:
        response = ollama.chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': text}])
        return response["message"]["content"]  # Return the model's response
    
    except Exception as e:
        return str(e)  # Return error message

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for better error messages
