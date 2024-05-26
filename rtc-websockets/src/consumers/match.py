from channels.generic.websocket import AsyncJsonWebsocketConsumer


class MatchConsumer(AsyncJsonWebsocketConsumer):
    """
    Consumer to serve match updates.
    """
    async def connect(self):
        self.match_id = f"match_{self.scope['url_route']['kwargs']['match_id']}"
        await self.channel_layer.group_add(self.match_id, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.match_id, self.channel_name)

    async def receive_json(self, content):
        await self.channel_layer.group_send(self.match_id, {'type': 'match.updated', **content})

    async def match_updated(self, event):
        await self.send_json(content=event)
