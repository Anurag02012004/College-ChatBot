"""
Flask Web Application for College Chatbot
Provides REST API and web interface for the chatbot
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

# Try to import structured chatbot (best), then enhanced, then basic
try:
    from structured_chatbot import StructuredCollegeChatbot as ChatbotClass
    print("✅ Using Structured Chatbot with formatted responses!")
except:
    try:
        from enhanced_chatbot import EnhancedCollegeChatbot as ChatbotClass
        print("Using Enhanced Chatbot")
    except:
        from chatbot_model import CollegeChatbot as ChatbotClass
        print("Using Basic Chatbot")

app = Flask(__name__)
CORS(app)  # Enable CORS for API access

# Initialize chatbot
print("Starting Flask application...")
chatbot = None

def init_chatbot():
    """Initialize the chatbot (lazy loading)."""
    global chatbot
    if chatbot is None:
        chatbot = ChatbotClass()
    return chatbot


@app.route('/')
def home():
    """Serve the main chat interface."""
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    API endpoint for chatbot interaction.
    
    Expected JSON: {"message": "user query"}
    Returns: {"response": "chatbot response"}
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
        
        user_message = data['message'].strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Initialize chatbot if needed
        bot = init_chatbot()
        
        # Get response
        response = bot.get_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'College Chatbot API'
    })


@app.route('/api/info', methods=['GET'])
def info():
    """Get basic college information."""
    try:
        bot = init_chatbot()
        return jsonify({
            'college_name': bot.data['college_info']['name'],
            'location': bot.data['college_info']['location'],
            'website': bot.data['college_info']['website'],
            'departments': [dept['name'] for dept in bot.data['departments']],
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500


if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get('PORT', 5001))
    debug_mode = os.environ.get('FLASK_ENV', 'development') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
