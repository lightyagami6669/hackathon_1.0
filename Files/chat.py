import os
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

#API
os.environ["GOOGLE_API_KEY"] = "AIazaSyDEsDalbVbGWGMSPpw4GgPoDBAlDd_NA1k"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# os.environ["ELEVEN_API_KEY"] = "sk_d3a8e7a9160b943467e55bd1887a7e8fd7406a6ba9471824"
# client = ElevenLabs(
    # api_key=os.environ["ELEVEN_API_KEY"]
# )

#basic config
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat()

# Text-to-Speech Setup
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech Recognition Setup
recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Speech Recognition request failed; {e}")
        except sr.WaitTimeoutError:
            print("Listening timed out.")
    return None


# Main Loop
while True:
    user_input = recognize_speech()

    if user_input is None:
        continue

    if user_input.lower() == "bye":
        print("Goodbye!")
        speak("Goodbye!")
        break

    response = chat_session.send_message(user_input)
    print(f"Assistant: {response.text}")
    speak(response.text)