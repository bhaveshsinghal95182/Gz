from flask import Flask, render_template, request, jsonify
import replicate

# Directly set your Replicate API key
replicate_api_key = "r8_BFv7JexN1572Q4gt2Kjp0vWcb1Hd2gz2YCZlQ"
replicate_client = replicate.Client(api_token=replicate_api_key)

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
    return jsonify({'response': response})  # Return JSON response

def get_chat_response(text):
    try:
        # Use Replicate to run the LLaMA-2 model
        model = replicate.models.get("meta/llama-2-13b-chat")
        
        # Run the model
        prediction = replicate_client.run(
            model,
            input={"prompt": text, "max_length": 150}  
        )
        
        return prediction  # Return the model's response
    
    except Exception as e:
        return str(e)  # Return error message

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for better error messages
