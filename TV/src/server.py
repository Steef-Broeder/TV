from flask import Flask, request
import socket

app = Flask(__name__)

# Endpoint to receive commands from the browser extension
@app.route('/command', methods=['POST'])
def receive_command():
    data = request.json
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
    return 'OK'

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

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    local_ip = get_local_ip()
    app.run(host=local_ip, port=5555)
