from channels.generic.websocket import AsyncWebsocketConsumer

class DetectionWebSocket(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def receive(self,text_data):
        for i in text_data:
            await self.send(text_data=i)
    
    async def disconnect(self, close_code):
        await self.close()