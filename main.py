import openai
import json
import mysql.connector

if __name__ == '__main__':
    openAiFile = open('openaiauth.json')
    openai.api_key =  json.load(openAiFile)["key"]
    openAiFile.close()

    dbInfoFile = open('db.json')
    dbInfo = json.load(dbInfoFile)
    dbInfoFile.close()

    dbConn = mysql.connector.connect(
        host=dbInfo['address'],
        user=dbInfo['user'],
        password=dbInfo['password']
    )
    dbCursor = dbConn.cursor()


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
