# we import the necessary libraries 
from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp

# define the prompt template to generate role-based response
from langchain import PromptTemplate
 
template = """
<s>[INST] <<SYS>>
Act as an american politican like Donald Trumph.
<</SYS>>
 
{text} [/INST]
"""
 
prompt = PromptTemplate(
    input_variables=["text"],
    template=template,
)

# Callbacks support token-wise streaming (instead of completing the brewing the whole response, it will reply token by token as it conpire it out)
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Input the inference here
text = "Explain the newest model of Porche car with electric engine, its pro and cons against traditional one"

#call the function and run the model
model_path = "models/llama-2-7b-chat.Q2_K.gguf"
llm = LlamaCpp(
    model_path=model_path,
    temperature=0.5,
    max_tokens=500,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

output = llm.invoke(prompt.format(text=text))
print(output)
