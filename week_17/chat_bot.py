from google import genai
import os 
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("gemini_key")

client = genai.Client(api_key=api)

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain how AI works in a few words",
# )

# print(response.text)

# variable for persona
# persona = """
# you are a loan agent, only answer relating to that
# - always answer briefly
# """


# while True:
#     userInput = input("user: ")
#     final_input=f"{persona}\n\n {userInput}"

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents= final_input
#     )


#     print(f"{response.text}")




persona = """
you are a translator, translating from language to another language.
"""

# prompt = "Translate the following English sentence into French: 'The weather is nice today.'"

while True:
    userInput = input("user: ")
    final_input=f"{persona}\n\n {userInput}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= final_input
    )


    print(f"{response.text}")
