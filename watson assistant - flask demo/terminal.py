from main import connect, disconnect, bot_message

connect()
print("\n-- Dites 'Au revoir' pour quitter. --\n")
input_usr = input("Bonjour, en quoi puis-je vous aider ? ")
while input_usr.lower()[0:9] != "au revoir":
    msg = {'text' : input_usr}
    dict_msg = bot_message(msg)
    lim = len(dict_msg)
    cpt = 0
    for i in dict_msg:
        msg = dict_msg[cpt]
        cpt += 1
        if(cpt == lim):
            if(msg['response_type'] == 'text'):
                input_usr = input(msg['text'] + " ")
            elif(msg['response_type'] == 'option'):
                print(msg["title"])
                dict_rep = {}
                for val in msg["options"]:
                    label = val["label"].lower()
                    print("- "+label)
                    dict_rep[label] = val["value"]["input"]
                input_usr = input("Votre réponse ? ").lower()
                while(not input_usr in dict_rep.keys()):
                    if(input_usr[0:9] == "au revoir"):
                        break
                    print("Indiquez-moi une réponse parmis celles-ci :")
                    for key in dict_rep.keys():
                        print("- "+key)
                    print("Si vous souhaitez partir dites juste 'Au revoir'")
                    input_usr = input("Votre réponse ? ")
                if(input_usr[0:9] == "au revoir"):
                    break
                input_usr = dict_rep[input_usr]["text"]
                print(input_usr)
        else:
            print(msg['text'])
disconnect()
print("Au revoir !")
