# chatgpt-test
This repo contains code used to test the ChatGPT API. 

## Instructions

### Getting The Code

You can get the code for this project using git on the command line. Simply run this command:

```
git clone https://github.com/masoncfrancis/chatgpt-test.git
```

You can also download a zip of the code from the GitHup repo, but I personally think using git to get it is easier. 
Plus, if you use git, you can grab any updates I make by running `git pull` from inside the folder.

### Prerequisites

Python 3.8+ is required for this project. If Python is not installed on your computer, please follow 
[these instructions](https://wiki.python.org/moin/BeginnersGuide/Download) to download and install it. 

Specific Python packages are required to run this project. More details are found in the following section. 


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

#### Deactivating The Virtual Environment

When you're done playing with this program, you can deactivate the virtual environment.

On Linux, run:

```
deactivate
```

On Windows, in the root project folder run:

```
Scripts/deactivate
```

You can reactivate the virtual environment when you feel like using the program again by running the commands 
mentioned above for your specific operating system. FYI, you only need to create the virtual environment once. 
You can activate it and deactivate it as many times as you need to. 

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
