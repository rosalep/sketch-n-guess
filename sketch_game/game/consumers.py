import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self): # accepts incoming connections
        self.room_group_name = "guess_chat"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
       
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        guess = text_data_json["guess"]
        username = text_data_json["username"]

        await self.channel_layer.group_send(
            self.room_group_name, {
            "type": "sendGuess",
            "guess": guess, # users can send in any length "guesses"; technically more of a "message"
            "username": username,
        })

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def sendGuess(self,event):
        guess = event["guess"]
        username = event["username"]
        await self.send(
            text_data = json.dumps({"guess":guess, "username":username})
        )