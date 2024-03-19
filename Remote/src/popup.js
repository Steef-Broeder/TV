const connectButton = document.getElementById('connectButton');
const ipAddressInput = document.getElementById('ipAddressInput');

connectButton.addEventListener('click', () => {
    const ipAddress = ipAddressInput.value;

    const socket = new WebSocket(`ws://${ipAddress}:5555`);

    // WebSocket event listeners
    socket.addEventListener('open', () => {
        console.log('WebSocket connection established');
        // Perform actions after the connection is established
        // ...

        // Send a message to the server
        socket.send('Hello, server!');
    });

    socket.addEventListener('message', (event) => {
        console.log('Received message:', event.data);
        // Handle incoming messages
        // ...
    });

    socket.addEventListener('close', () => {
        console.log('WebSocket connection closed');
        // Perform actions after the connection is closed
        // ...
    });

    socket.addEventListener('error', (error) => {
        console.error('WebSocket error:', error);
        // Handle WebSocket errors
        // ...
    });
});