document.addEventListener('DOMContentLoaded', function() {
    const roomNameElement = document.querySelector('#room-name');
    if (!roomNameElement) {
        console.error('Room name element not found');
        return;
    }
    
    const roomName = roomNameElement.dataset.roomName;
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/messenger/' + roomName + '/'
    );

    const messageInput = document.querySelector('#chat-message-input');
    const messageSubmitButton = document.querySelector('#chat-message-submit');
    
    if (!messageInput || !messageSubmitButton) {
        console.error('Message input or submit button not found');
        return;
    }

    chatSocket.onopen = function(e) {
        console.log('WebSocket is open now.');
    };

    chatSocket.onerror = function(e) {
        console.error('WebSocket error:', e);
    };

    messageSubmitButton.addEventListener('click', function() {
        const message = messageInput.value;
        if (message.trim()) {
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            console.log('Message sent:', message);
            messageInput.value = '';  // 메시지 전송 후 입력 필드 초기화
        }
    });

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log('Received message:', data);
        const message = data['message'];
        const sender = data['sender'];

        const chatLog = document.querySelector('#chat-log');
        if (chatLog) {
            chatLog.innerHTML += (
                `<div class="chat-message">
                    <strong>${sender}:</strong> ${message}
                </div>`
            );
        } else {
            console.error('Chat log element not found');
        }
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
});
