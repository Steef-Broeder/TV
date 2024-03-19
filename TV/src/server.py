import asyncio
import websockets
import socket

async def receive_command(websocket, path):
    try:
        data = await websocket.recv()
        print(f"Data received as: {data}!")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # command = data.get('command')
        
    # # Handle different commands
    # if command == 'open':
    #     video_url = data.get('video_url')
    #     play_video(video_url)
    # elif command == 'stop':
    #     stop_video()
    # elif command == 'volume_up':
    #     volume_up()
    # elif command == 'volume_down':
    #     volume_down()

def play_video(video_url):
    print(f"Playing video: {video_url}")
    pass

def stop_video():
    print("Stopping video")
    pass

def volume_up():
    print("Increasing volume")
    pass

def volume_down():
    print("Decreasing volume")
    pass

ip_address = socket.gethostbyname(socket.gethostname())
print(f"Server running on IP: {ip_address}")

async def main():
    async with websockets.serve(receive_command, ip_address, 5555):
        await asyncio.Future()  # run forever

asyncio.run(main())