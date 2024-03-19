import asyncio
import websockets
import socket

async def receive_command(websocket, path):
    data = await websocket.recv()
    command = data.get('command')
        
    # Handle different commands
    if command == 'open':
        video_url = data.get('video_url')
        play_video(video_url)
    elif command == 'stop':
        stop_video()
    elif command == 'volume_up':
        volume_up()
    elif command == 'volume_down':
        volume_down()

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

start_server = websockets.serve(receive_command, ip_address, 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
