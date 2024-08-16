// apps/messenger/static/js/chat.js

document.addEventListener('DOMContentLoaded', function() {
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const chatLog = document.querySelector('#chat-log');
        chatLog.innerHTML += '<div><strong>' + data.sender + ':</strong> ' + data.message + '</div>';
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.querySelector('#chat-form').onsubmit = function(e) {
        e.preventDefault();
        const messageInputDom = document.querySelector('#message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({'message': message}));
        messageInputDom.value = '';
    };
});