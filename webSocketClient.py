import websockets
import asyncio

uri = "ws://10.6.72.83:5050"

class WebSocketClient():

    def __init__(self):
        pass

    async def connect(self):
        self.connection = await websockets.client.connect(uri)
        if self.connection.open:
            print('Connection stablished. Client correcly connected')
            await self.sendMessage('It is a test messge')


    async def sendMessage(self, message):
        await self.connection.send(message)

    async def receiveMessage(self):
        while True:
            try:
                message = await self.connection.recv()
                print('Received message from server: ' + str(message))
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break

    async def heartbeat(self):
        '''
        Sending heartbeat to server every 5 seconds
        Ping - pong messages to verify connection is alive
        '''
        while True:
            try:
                await self.connection.send('ping')
                await asyncio.sleep(5)
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break

    def printConnectionInfo(self):
        print(self.connection)