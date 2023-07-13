from channels.generic.websocket import AsyncWebsocketConsumer
import random
import json
import uuid
class DetectionWebSocket(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = uuid.uuid4()
        self.room_group_name = "room_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user = text_data_json["user"]
        type=text_data_json['type']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": type,"user":user}
        )

    # Receive message from room group
    async def counts(self, event):
        user=event['user']
        jsonreturn = {
            "user":user,
            "counts": {
                "violence": random.randint(1, 11),
                "violence_percent": round(random.uniform(-5.0, 5.0) * 10, 3),
                "weapons": random.randint(1, 11),
                "weapons_percent": round(random.uniform(-5.0, 5.0) * 10, 3),
                "intrusion": random.randint(1, 11),
                "intrusion_percent": round(random.uniform(-5.0, 5.0) * 10, 3),
                "class_labels": random.randint(1, 11),
                "labels_percent": round(random.uniform(-5.0, 5.0) * 10, 3),
            },
        }
        data = json.dumps(jsonreturn)
        # Send message to WebSocket
        await self.send(text_data=data)
    # async def receive(self,text_data):
    #     cccc
    #     await self.send(text_data=data)
    
    # async def disconnect(self, close_code):
    #     await self.close()

