import openai
import json
import mysql.connector

if __name__ == '__main__':
    openAiFile = open('openaiauth.json')
    openai.api_key =  json.load(openAiFile)["key"]
    openAiFile.close()

    # dbInfoFile = open('db.json')
    # dbInfo = json.load(dbInfoFile)
    # dbInfoFile.close()

    # dbConn = mysql.connector.connect(
    #     host=dbInfo['address'],
    #     user=dbInfo['user'],
    #     password=dbInfo['password']
    # )
    # dbCursor = dbConn.cursor()

    # phoneNumber = "+13135551234"

    # getQuery = f"SELECT * FROM rejection.dynamic_chatbot where phoneNumber = '{phoneNumber}' ORDER BY timeGenerated DESC"

    botPerson = "Joe Biden"

    while True:

        chatMessages = [{"role": "system", "content": f"You are {botPerson}. You should respond to all messages in the speaking style of {botPerson}"}]

        # dbCursor.execute(getQuery)

        # getResult = dbCursor.fetchone()


        # chatMessages = []
        # if getResult == None:
        #     chatMessages = [{"role": "system", "content": f"You are {botPerson}. You should respond to all messages in the speaking style of {botPerson}"}]
        # else:
        #     strList = getResult[2].split('&')
        #     jsonList = []
        #     for x in strList:
        #         jsonList.append(json.loads(x))
        #     chatMessages = jsonList
    

        userInput = input("Enter a message to send: ")
        chatMessages.append({"role": "user", "content": userInput})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chatMessages
        )
        chatMessages.append({"role": response['choices'][0]['message']['role'], "content": response['choices'][0]['message']['content']})

        # saveQuery = "INSERT INTO rejection.dynamic_chatbot (conversation, phoneNumber) VALUES (%s, %s)"
        # valueStrList = []
        # for x in chatMessages:
        #     valueStrList.append(str(x))
        # valueStr = '&'.join(valueStrList)
        # saveValues = (valueStr, phoneNumber)
        # dbCursor.execute(saveQuery, saveValues)
        # dbConn.commit()

        print("Response: " + response['choices'][0]['message']['content'])
