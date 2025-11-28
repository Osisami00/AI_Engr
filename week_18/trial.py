import ollama

while True:
    response = ollama.chat(
            model = "gemma3:1b",
            messages = [{"role": "user",
                        "content": input("Enter your request: ")}]
        )
    print(response["message"]["content"])