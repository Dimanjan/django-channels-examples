import json
from channels.generic.websocket import AsyncWebsocketConsumer
import requests
url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
from asyncio import sleep

class PositionsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            data= requests.get(url).json()
            await self.send(text_data=json.dumps({
                'data':data
            }))
            await sleep(60*3)



