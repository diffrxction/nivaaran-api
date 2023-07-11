from channels.generic.websocket import AsyncWebsocketConsumer
import random
import json

class DetectionWebSocket(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def receive(self,text_data):
        jsonreturn = {
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
        await self.send(text_data=data)
    
    async def disconnect(self, close_code):
        await self.close()


class ViewWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="Connected")
    
    async def receive(self,text_data):
        for i in text_data:
            await self.send(text_data=i)
    
    async def disconnect(self, close_code):
        await self.close()