import openai
import json

if __name__ == '__main__':
    openAiFile = open('openaiauth.json')
    openai.api_key =  json.load(openAiFile)["key"]
    openAiFile.close()

    chatMessages=[
                {"role": "system", "content": "You are Donald Trump. You should respond to all messages in the speaking style of Donald Trump"}
            ]
    while True:
        userInput = input("Enter a message to send: ")
        chatMessages.append({"role": "user", "content": userInput})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chatMessages
        )
        chatMessages.append({"role": response['choices'][0]['message']['role'], "content": response['choices'][0]['message']['content']})
        print("Response: " + response['choices'][0]['message']['content'])
