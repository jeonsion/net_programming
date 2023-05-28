import asyncio
from socket import *

port = 2530
bufsize = 1024

async def handler(data, addr, sock):
    print(f"{addr} Received message: ", data.decode())
    sock.sendto(data, addr)

async def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('', port))
    print(f"Server started on port {port}")

    while True:
        data, addr = await asyncio.to_thread(sock.recvfrom, bufsize)
        print(f"{addr} accepted")
        asyncio.create_task(handler(data, addr, sock))

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Server stopped by user")
