from flask import Flask, render_template_string, request, jsonify
import json
import os
from simple_chat_faq_bot_with_memory import normalize, get_response, load_memory, remember
from pyngrok import ngrok
import socket

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 C!pher School Bot</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        .chat-container {
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            height: 600px;
            display: flex;
            flex-direction: column;
        }
        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 10px;
            margin-bottom: 20px;
        }
        .message {
            margin-bottom: 15px;
            padding: 12px;
            border-radius: 10px;
            max-width: 70%;
        }
        .user-message {
            background: #007bff;
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .bot-message {
            background: #f8f9fa;
            color: #333;
            border-left: 4px solid #ff6b6b;
        }
        .input-container {
            display: flex;
            gap: 10px;
        }
        .message-input {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
        }
        .message-input:focus {
            border-color: #007bff;
        }
        .send-button {
            padding: 12px 25px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            transition: background 0.3s;
        }
        .send-button:hover {
            background: #0056b3;
        }
        .welcome-message {
            text-align: center;
            color: #666;
            font-style: italic;
            margin: 20px 0;
        }
        .stats {
            text-align: center;
            color: #666;
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
            <div class="brand">C!PHER SCHOOL BOT</div>
            <h1>🤖 Your AI Learning Assistant</h1>
            <p>Expert in Cybersecurity, Python, Git, and School Registration</p>
        </div>

        <div class="chat-container">
            <div id="chat-messages" class="chat-messages">
                <div class="welcome-message">
                    <h3>👋 Welcome to C!pher School Bot!</h3>
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
                messageDiv.innerHTML = `<strong>🤖 C!pher:</strong> ${content}`;
                conversationCount++;
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

            // Send message to server
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

        // Focus on input when page loads
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

        # Load memory and get response
        memory = load_memory()
        bot_reply = get_response(user_input)

        # Save to memory
        remember(memory, user_input, bot_reply)

        return jsonify({'reply': bot_reply})

    except Exception as e:
        return jsonify({'reply': f'Sorry, there was an error: {str(e)}'})

def setup_ngrok():
    """Setup ngrok tunnel with custom subdomain"""
    try:
        # Kill any existing tunnels
        ngrok.kill()

        # For free tier, use random subdomain
        # For custom subdomain like 'cipherschoolbot', you need ngrok paid plan
        print("🚀 Setting up ngrok tunnel...")

        # Option 1: Free tier (random subdomain)
        tunnel = ngrok.connect(5000)
        public_url = tunnel.public_url

        print(f"✅ Free tunnel created: {public_url}")
        print("💡 For custom subdomain 'cipherschoolbot', upgrade to ngrok paid plan")
        print("   Visit: https://dashboard.ngrok.com/billing/subscription")

        return public_url

    except Exception as e:
        print(f"❌ Ngrok setup failed: {e}")
        return None

if __name__ == '__main__':
    # Setup ngrok tunnel
    public_url = setup_ngrok()

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("\n🤖 C!PHER SCHOOL BOT is running!")
    print("=" * 50)
    print(f"💻 Local access: http://localhost:5000")
    print(f"📱 Network access: http://{local_ip}:5000")

    if public_url:
        print(f"🌐 Public access: {public_url}")
        print("   (Share this link to access from anywhere!)")

    print("\n🔥 Custom Domain Options:")
    print("   1. Ngrok Paid: cipherschoolbot.ngrok.io (requires payment)")
    print("   2. Deploy to Render/Heroku for free custom domain")
    print("   3. Use services like 000webhost, infinityfree, etc.")

    print("\n❌ Press Ctrl+C to stop the server")
    print("=" * 50)

    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
        ngrok.kill()