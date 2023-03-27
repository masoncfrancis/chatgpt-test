# chatgpt-test
This repo contains code used to test the ChatGPT API. 

## Instructions

### Prerequisites

Python 3.8+ is required for this project. If Python is not installed on your computer, please follow 
[these instructions](https://wiki.python.org/moin/BeginnersGuide/Download) to download and install it. 

Specific Python packages are required to run this project. More details are found in the following section. 

Code for the project may be cloned or downloaded from this GitHub repo.

### Create a Virtual Environment

Once the code has been downloaded or cloned to a folder, it is recommended (but not required) to create a Python virtual environment. If you decide not to, please skip to the 'Install Project Dependencies' section. 
Otherwise, continue following the instructions in this section. 

Open a terminal in the project folder and run this command (replacing `python3` with `python` as necessary for your installation):

```
python3 -m venv venv
```

Next, you will need to activate the virtual environment. To activate the virtual environment on a UNIX style operating system (Linux, macOS, etc.), run this command:

```
source venv/bin/activate
```

To activate the virtual environment in Windows, run this command from the project folder root:

```
.\venv\Scripts\activate
```

You will need to have this virtual environment activated in order to run the code in this project. If your virtual environment ever becomes deactivated, you may run the above command (for your 
applicable OS) again from the project folder root. 

### Install Project Dependencies

This project requires a few packages to run properly.

With your Python virtual environment activated (if you are using one), run the following command from the project folder root (replacing `python3` with `python` as necessary for your installation):

```
python3 -m pip install -r requirements.txt
```

The project's required dependencies are now installed.

### Get OpenAI API key

The file `openaiauth.json` holds your OpenAI API Key. You will need to generate an API key at
[https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) and
place it in the `openaiauth.json` file. As of this writing, new accounts are provided free trial
credits. This application will not use many of your credits at all, so don't worry about using them up
by trying this program out. 

### Start the application

To start the project server, run this command from the project folder root (replacing `python3` with `python` as necessary for your installation):

```
python3 main.py
```
