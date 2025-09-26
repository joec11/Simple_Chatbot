# Import required tools from the transformers library
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Choose the pretrained model name (BlenderBot distilled version, suitable for conversations)
model_name = "facebook/blenderbot-400M-distill"

# Load the pretrained model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize a list to store the conversation history (alternating user and bot messages)
conversation_history = []

# Start a continuous conversation loop
while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)

    # Get the input data from the user
    input_text = input("> ")

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Print the bot's response
    print(response)

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
