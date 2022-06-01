from channels.generic.websocket import AsyncWebsocketConsumer

import json
from random import randint
from asyncio import sleep
class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for i in range(100):
            await sleep(1)
            await self.send(json.dumps({
                'value': randint(-20, 20)})
                )
    