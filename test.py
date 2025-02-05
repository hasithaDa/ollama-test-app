import ollama

# Initialize the Ollama client
client = ollama.Client()

# Specify the model to use
model = "deepseek-r1:1.5b"

# Function to get user input and generate a response
def ask_question():
    while True:
        # Get the user's question
        question = input("Please enter your question (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if question.lower() == 'exit':
            print("Exiting...")
            break
        
        # Generate a response using the Ollama client
        response = client.generate(model=model, prompt=question)
        
        # Print the response
        print("Response:", response.response)
        print()  # Add a blank line for better readability

# Run the function to start the interactive session
ask_question()