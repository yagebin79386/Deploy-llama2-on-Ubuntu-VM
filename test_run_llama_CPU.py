from llama_cpp import Llama

# Put the location of to the GGUF model that you've download from HuggingFace here
model_path = "YOUR_PATH/llama-2-7b-chat.Q2_K.gguf"
llm = Llama(model_path=model_path)

# Prompt creation
system_message = "Help to people to get to know the general knowledge"
user_message = "Q: Whare are all the ocean systems on the earth ?"

prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""

# Run the model
output = llm(
  prompt, # Prompt
  max_tokens=32, # Generate up to 32 tokens
  stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
  echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion

print(output)
