import openai
import json

if __name__ == '__main__':
    openAiFile = open('openaiauth.json')
    openai.api_key =  json.load(openAiFile)["key"]
    openAiFile.close()

    botPerson = "An AI Assistant named Angie"

    chatMessages=[
                {"role": "system", "content": f"You are {botPerson}. You should respond to all messages in the speaking style of {botPerson}"}
            ]
    print(f"Your current chatbot personality is {botPerson}")
    print("\nTo change your chatbot personality, enter \'#changeperson [personality you choose]\'")
    print("\nFor example, to change your chatbot's personality to Donald Trump you would type:")
    print("#changeperson Donald Trump")
    print("\nOr to change it to a grouchy old lady, you'd type:")
    print("#changeperson A grouchy old lady")
    print("\nOr to change it to Ted from Bill and Ted's Excellent Adventure, you'd type:")
    print("#changeperson Ted from Bill and Ted's Excellent Adventure")
    print("\nTo reset the chatbot to default, type:")
    print("#default")
    while True:
        userInput = input("\nEnter a message to send: ")

        # Check for command
        if userInput[0:1] == "#":
            if userInput[1:].split()[0] == "changeperson":
                botPerson = ' '.join(userInput.split()[1:])

                chatMessages=[
                {"role": "system", "content": f"You are {botPerson}. You should respond to all messages in the speaking style of {botPerson}"}
                ]

                print(f"Your chatbot personality was successfully changed to {botPerson}. All chat history has been deleted.")

            elif userInput[1:].split()[0] == "default":
                botPerson = "An AI assistant named Angie"

                chatMessages=[
                {"role": "system", "content": f"You are {botPerson}. You should respond to all messages in the speaking style of {botPerson}"}
                ]

                print(f"Your chatbot personality was successfully changed to {botPerson}. All chat history has been deleted.")
                
        else:
            chatMessages.append({"role": "user", "content": userInput})
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=chatMessages
            )
            chatMessages.append({"role": response['choices'][0]['message']['role'], "content": response['choices'][0]['message']['content']})
            print("Response: " + response['choices'][0]['message']['content'])