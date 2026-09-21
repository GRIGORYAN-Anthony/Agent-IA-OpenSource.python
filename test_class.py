import requests


class Agent_IA():
    def __init__(self, config):
        self.conversation = [{
            "role":"system",
            "message": config
        }]

    def Message(self, message):
        return {"role":"user", "content": message}


    def Conversation(self):
        res = requests.post(url="http://localhost:11434/api/chat", json={"model": "mistral:7b ",
                                                                         "messages": self.conversation,
                                                                         "stream": False
                                                                         })
        res.raise_for_status()
        return [res.json()["message"]["content"], res.json()["message"]]

    def init_conversation(self, mes):
        message = self.Message(mes)
        self.conversation.append(message)
        print(self.conversation)
        affichage = self.Conversation()
        self.conversation.append(affichage[1])
        print(affichage[0])



conf = input("configure le modèle : ")
agent = Agent_IA(conf)

run=True
while run:

    envoie = input("Entrez votre message : ")
    agent.init_conversation(envoie)
