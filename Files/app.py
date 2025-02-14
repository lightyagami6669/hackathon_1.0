from flask import Flask, request, render_template, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
os.environ["GOOGLE_API_KEY"] = "AIzaSyDEsDalbVbGWGMSPpw4GgPoDBAlDd_NA1k"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 65535,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-01-21",
    generation_config=generation_config,
)

chat_session = model.start_chat()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message')

    if user_input.lower() == "bye":
        response_text = "Goodbye!"
    else:
        response = chat_session.send_message(user_input)
        response_text = response.text

    return jsonify({'response': response_text})


if __name__ == '__main__':
    app.run(debug=True)
