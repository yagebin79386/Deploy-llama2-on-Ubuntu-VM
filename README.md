# Deploy-llama2-on-Ubuntu-VM
How to deploy the llama2 model and initiate the chat on the Ubuntu VMware on Macbook intel

## 1. Preparation step on your Intel Macbook
find the ubuntu image on the website https://www.linuxvmimages.com/images/ubuntu-2004/, download the ubuntu newest version file for VMware.
Then use the VMware to load the image and install all the system updates using following command on terminal within Ubuntu.
"sudo apt full-upgrade -y"
Then reboot the system
"sudo reboot"

## 2. prepare the python env. for deployment

### 2.1 install Python 3
Check if Python 3 is installed:
"python3 --version"
If it’s not installed, install Python 3 and python3-pip:
"sudo apt install -y python3 python3-pip"

### 2.2 prepare virtual environment isolation for llama2 installation
To keep your project dependencies isolated, use a virtual environment. Install venv if it’s not already available:
"sudo apt install -y python3-venv"

Create a Virtual Environment
Navigate to your project directory or create a new one:
"mkdir llama2_CPU"
"cd llama2_CPU"
Create a virtual environment called llama2_CPU
"python3 -m venv llama2_CPU"
Activate the Virtual Environment
Activate the environment to install dependencies within it:
"source llama2_env/bin/activate"

## 3. Install dependencies for running LLaMA locally
llama-cpp-python is a project based on lama.cpp which allow you to run Llama models on your local Machine by 4-bits Quantization.

👁️ Quantization: Quantization refers to the process of reducing the precision of a model’s weights and activations from floating-point numbers to integers. This can be useful for deploying models on devices with limited computational resources, as it can reduce memory usage and improve computational efficiency.

First we go to the project directory
"cd ~/llama_CPU"

we install the library which is python friendly for python
"pip3 install llama-cpp-python"

## 4. Access the llama2 model from hugging face website "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main"
here because we use the Intel CPU based VM without independent GPU, with a minimum 8GB RAM and 8GM shared graphic memory, so we choose the most lightweighted llama2 model llama-2–7b-chat.Q2_K.gguf.

But before you can download the model from hugging face, you need to regisery an acount and get your private token, which we will need in the following curl command

About GGUF
👁️ GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp. GGUF offers numerous advantages over GGML, such as better tokenisation, and support for special tokens. It is also supports metadata, and is designed to be extensible.

go to the subfolder models
"cd ./models"

use the curl to download our chosen model from the download link (go on that hugging face website provided above and find that model, copy the download link)
"curl -L -o llama-2-7b-chat.Q2_K.gguf -H "Authorization: Bearer YOUR_TOKEN" "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf"

## 5. Test the model using jupyter notebook
after the model is downloaded, we can use jupyter notebook to test the model.

With the virtual environment activated, install Jupyter Notebook
"pip install jupyter"

To use the virtual environment as a kernel in Jupyter, install ipykernel:
"pip install ipykernel"

Use the following command to add your virtual environment to Jupyter Notebook’s list of available kernels:
"python -m ipykernel install --user --name=llama2_CPU --display-name "Python (llama2_CPU)"

Now that everything is set up, start Jupyter Notebook:
"jupyter notebook"
On the jupyter notebook interface, you can choose on the right upper corner to kernel to the one we created "llama2_CPU"

Then run the python script test_run_llama_CPU.py provided to test if the model has all its dependencies, if any is missing, just install them.

## 6. Running the model using Langchain
One of the most useful features of LangChain is the ability to create prompt templates. 
👁️A prompt template is a string that contains a placeholder for input variable(s).
Otherwise it can provide the token-wise streaming, whcih provides bette interaction with the user.

install the langchain library
pip3 install langchain

Then you can open the jupyter notebook and run the script langchain_run.py provided. You can change the prompt template within the script and other parameters of the model referencing.
