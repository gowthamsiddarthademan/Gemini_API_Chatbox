import google.generativeai as genai

genai.configure(api_key='AIzaSyDetObjfBkDqRNAoBII_s0ibrPMUc8mC0s')

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(response.text)