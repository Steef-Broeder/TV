from flask import Flask, request

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
    print(f"App is running on port 5555")
