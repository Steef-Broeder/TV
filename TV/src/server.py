import asyncio
import websockets
import socket

async def receive_command(websocket, path):
    connected = True
    while connected:
        try:
            data = await websocket.recv()
            print(f"Data received as: {data}!")
        except websockets.exceptions.ConnectionClosed as e:
            print(f"Connection closed with error: {e}")
            connected = False
        except Exception as e:
            print(f"An error occurred: {e}")
            connected = False

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

async def main(ip):
    async with websockets.serve(receive_command, "ip", 5555):
        await asyncio.Future()

ip_address = input("What is your local ip?")
print(f"Server running on IP: {ip_address}:5555")

asyncio.run(main(ip_address))