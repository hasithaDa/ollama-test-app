import ollama

client = ollama.Client()

model ="deepseek-r1:1.5b"

question = "Waht is the capital of France?"

response = client.generate(model=model,prompt=question)

print(response.response)
