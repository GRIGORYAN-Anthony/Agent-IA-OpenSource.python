import json
import requests
from pathlib import Path



conversation = [{"role": "system", "content": "tu es un simple assistant qui a des reponses courtes et rapide"}]


run=True
while run:

    mes = input("entrer votre message : ")

    if mes == "sortir":
        quit()



    def Message(mesage):
        return {"role": "user", "content": mesage}

    def Agent(conv):
        res = requests.post(url="http://localhost:11434/api/chat", json={"model":"mistral:7b ",
                                                            "messages": conv,
                                                            "stream": False
                                                            })
        res.raise_for_status()
        return [res.json()["message"]["content"], res.json()["message"]]

    conversation.append(Message(mes))
    affichage = Agent(conversation)
    conversation.append(affichage[1])
    print(affichage[0])

