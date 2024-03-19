const connectButton = document.getElementById('connectButton');
const ipAddressInput = document.getElementById('ipAddressInput');
const volumeUpButton = document.getElementById('volumeUpButton');
const volumeDownButton = document.getElementById('volumeDownButton');
const castButton = document.getElementById('castButton');

let socket = null;

connectButton.addEventListener('click', () => {
    const ipAddress = ipAddressInput.value;

    socket = new WebSocket(`ws://${ipAddress}:5555`);

    // WebSocket event listeners
    socket.addEventListener('open', () => {
        console.log('WebSocket connection established');
        // Perform actions after the connection is established

        socket.send('Hello, server!');
    });

    socket.addEventListener('message', (event) => {
        console.log('Received message:', event.data);
    });

    socket.addEventListener('close', () => {
        console.log('WebSocket connection closed');
    });

    socket.addEventListener('error', (error) => {
        console.error('WebSocket error:', error);
    });
});

volumeUpButton.addEventListener('click', () => {
    if (socket) {
        socket.send(JSON.stringify({ command: 'volume_up' }));
    }
});

volumeDownButton.addEventListener('click', () => {
    if (socket) {
        socket.send(JSON.stringify({ command: 'volume_down' }));
    }
});

castButton.addEventListener('click', () => {
    if (socket) {
        socket.send(JSON.stringify({ command: 'video' }));
    }
});