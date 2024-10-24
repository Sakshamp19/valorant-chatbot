document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== '') {
        addMessage(userInput, 'user');
        document.getElementById('user-input').value = ''; // Clear input field
        console.log(userInput)
        // Send POST request to Flask backend
        fetch('http://127.0.0.1:5000/run-script', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ selectedOption: userInput })
        })
        .then(response => response.json())
        .then(data => {
            // Add bot's response from the backend
            console.log(data);
            const outputLines = data.output.trim().split('\n');
            const iglLine = outputLines.find(line => line.startsWith('IGL:'));
            const iglValue = iglLine ? iglLine.split(': ')[1] : null;
            let d,c,s,i;
            let ct=0;
            const handles = data.players.map(player => player.handle);
            const roles = handles.filter(player=>player!=iglValue);
            console.log("roles : ",roles)
            c=roles[0];
            d=roles[1];
            i=roles[2];
            s=roles[3];
            let response=`\nProposed Pro Team :<br> Duelist : ${d} <br> Controller : ${c}<br>Sentinel : ${s} <br> Initiator : ${i} <br>IGL: Vania\n`;
            addMessage(response || 'No output returned', 'bot');
        })
        .catch(error => {
            addMessage('Error: ' + error.message, 'bot');
        });
    }
});

function addMessage(message, sender) {
    const messageContainer = document.getElementById('chat-messages');
    const messageElement = document.createElement('div');
    
    messageElement.classList.add('chat-message');
    messageElement.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    
    messageElement.innerHTML = message;
    messageContainer.appendChild(messageElement);
    messageContainer.scrollTop = messageContainer.scrollHeight; // Auto scroll to the bottom
}
