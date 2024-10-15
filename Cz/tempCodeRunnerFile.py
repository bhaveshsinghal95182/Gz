from flask import Flask, render_template, request
import replicate

# Directly set your Replicate API key
replicate_api_key = "r8_BFv7JexN1572Q4gt2Kjp0vWcb1Hd2gz2YCZlQ"
replicate_client = replicate.Client(api_token=replicate_api_key)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input_text = msg
    return get_Chat_response(input_text)

def get_Chat_response(text):
    try:
        # Use Replicate to run the LLaMA-2 model
        model = replicate.models.get("meta/llama-2-13b-chat")
        
        # Run the model
        prediction = replicate_client.run(
            model,
            input={"prompt": text, "max_length": 150}  
        )

        
        return prediction  
    
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
