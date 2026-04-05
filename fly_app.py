from flask import Flask, render_template_string, request, jsonify
import os
from simple_chat_faq_bot_with_memory import normalize, get_response, load_memory, remember

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>🤖 cipherschool Chat Bot</title>
    <style>
        body {
            font-family: 'Bookman Old Style', Bookman, serif;
            margin: 0;
            padding: 0;
            background: radial-gradient(circle at top left, #b84bff 0%, #541d7d 40%, #270b3f 100%);
            min-height: 100vh;
            color: white;
        }
        .container {
            max-width: 840px;
            margin: 0 auto;
            padding: 26px;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 28px;
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.28);
        }
        .header {
            text-align: center;
            color: #f6f0ff;
            margin-bottom: 28px;
        }
        .header h1,
        .header p,
        .welcome-message,
        .message {
            font-weight: 700;
        }
        .chat-container {
            background: rgba(255, 255, 255, 0.16);
            border-radius: 22px;
            padding: 20px;
            box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.18), 0 12px 30px rgba(0, 0, 0, 0.16);
            height: 600px;
            display: flex;
            flex-direction: column;
        }
        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
            margin-bottom: 18px;
            background: #ffffff;
            border-radius: 18px;
            color: #1a1a1a;
        }
        .message {
            margin-bottom: 15px;
            padding: 14px;
            border-radius: 14px;
            max-width: 72%;
            font-family: 'Bookman Old Style', Bookman, serif;
            font-weight: 700;
            line-height: 1.5;
        }
        .user-message {
            background: #6b3cc2;
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .bot-message {
            background: #f5f5f8;
            color: #2d2d33;
            border-left: 4px solid #9a4dff;
        }
        .input-container {
            display: flex;
            gap: 12px;
        }
        .message-input {
            flex: 1;
            padding: 14px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 28px;
            font-size: 16px;
            font-weight: 700;
            outline: none;
            background: rgba(255, 255, 255, 0.95);
            color: #1a1a1a;
        }
        .message-input::placeholder {
            color: #7a6d9d;
        }
        .message-input:focus {
            border-color: #d7b4ff;
        }
        .send-button {
            padding: 14px 28px;
            background: #8e44ff;
            color: white;
            border: none;
            border-radius: 28px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 700;
            transition: background 0.3s ease;
        }
        .send-button:hover {
            background: #6e34c1;
        }
        .welcome-message {
            text-align: center;
            color: #4c3b63;
            font-style: italic;
            margin: 20px 0;
        }
        .stats {
            text-align: center;
            color: #e8e0ff;
            margin-top: 10px;
            font-size: 14px;
        }
        .brand {
            font-size: 24px;
            font-weight: bold;
            color: #ff6b6b;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="brand">cipherschool Chat Bot</div>
            <h1>🤖 Your AI Learning Assistant</h1>
            <p>Expert in Cybersecurity, Python, Git, and School Registration</p>
        </div>

        <div class="chat-container">
            <div id="chat-messages" class="chat-messages">
                <div class="welcome-message">
                    <h3>👋 Welcome to cipherschool Chat Bot!</h3>
                    <p>I'm your AI assistant specialized in:</p>
                    <ul style="text-align: left; display: inline-block;">
                        <li>🔐 Cybersecurity fundamentals</li>
                        <li>🐍 Python programming</li>
                        <li>📚 Git & GitHub workflows</li>
                        <li>📝 School registration & admissions</li>
                    </ul>
                    <p><strong>Ask me anything!</strong></p>
                </div>
            </div>

            <div class="input-container">
                <input type="text" id="message-input" class="message-input"
                       placeholder="Ask about cybersecurity, Python, Git, or registration..."
                       onkeypress="handleKeyPress(event)">
                <button onclick="sendMessage()" class="send-button">Send</button>
            </div>

            <div id="stats" class="stats">💬 Conversations: 0</div>
        </div>
    </div>

    <script>
        let conversationCount = 0;

        function addMessage(content, isUser = false) {
            const messagesDiv = document.getElementById('chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

            if (isUser) {
                messageDiv.innerHTML = `<strong>You:</strong> ${content}`;
            } else {
                    messageDiv.innerHTML = `<strong>🤖 cipherschool:</strong> ${content}`;
                document.getElementById('stats').innerHTML = `💬 Conversations: ${conversationCount}`;
            }

            messagesDiv.appendChild(messageDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        function sendMessage() {
            const input = document.getElementById('message-input');
            const message = input.value.trim();

            if (!message) return;

            addMessage(message, true);
            input.value = '';

            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.reply, false);
            })
            .catch(error => {
                addMessage('Sorry, there was an error processing your message.', false);
                console.error('Error:', error);
            });
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('message-input').focus();
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '').strip()

        if not user_input:
            return jsonify({'reply': 'Please type a message!'})

        memory = load_memory()
        bot_reply = get_response(user_input)
        remember(memory, user_input, bot_reply)

        return jsonify({'reply': bot_reply})

    except Exception as e:
        return jsonify({'reply': f'Sorry, there was an error: {str(e)}'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
