
import asyncio
from socket import *

port = 2558
bufsize = 1024

async def handler(conn, addr):
    while True:
        data = await asyncio.to_thread(conn.recv, bufsize)
        if not data:
            break
        print(f"{addr} Received message: ", data.decode())
        conn.send(data)
    conn.close()
    print(f"{addr} Connection closed")

async def main():
    sock = socket()
    sock.bind(('', port))
    sock.listen()
    print(f"Server started on port {port}")

    while True:
        client, addr = await asyncio.to_thread(sock.accept)
        print(f"{addr} accepted")
        asyncio.create_task(handler(client, addr))

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Server stopped by user")
