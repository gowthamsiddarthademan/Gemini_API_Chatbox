import google.generativeai as genai

genai.configure(api_key='AIzaSyDetObjfBkDqRNAoBII_s0ibrPMUc8mC0s')

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat()

while True:
    message = input("You: ")
    response = chat.send_message(message)

    print("Gemini: " + response.text)