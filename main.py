import asyncio
from webSocketClient import WebSocketClient

if __name__ == '__main__':
    # Creating client object
    client = WebSocketClient()
    loop = asyncio.get_event_loop()
    # Start connection and get client connection protocol
    loop.run_until_complete(client.connect())
    # Start listener and heartbeat 
    tasks = [
        #asyncio.ensure_future(client.heartbeat()),
        asyncio.ensure_future(client.receiveMessage()),
    ]

    loop.run_until_complete(asyncio.wait(tasks))