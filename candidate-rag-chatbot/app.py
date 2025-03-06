import json
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

# Import configuration and utilities
from config import DEBUG, PORT, HOST
from utils.weaviate_client import run_query
from utils.response_formatter import format_chatbot_response, enhance_candidate_response

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Store conversation history - in production this would use a database
# For simplicity, we're using an in-memory dictionary here
conversation_history = {}

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Process a chatbot query and return a formatted conversational response with candidate recommendations.
    
    Request body should contain:
    {
        "message": "Find top full-stack candidates with diverse backgrounds",
        "conversation_id": "optional-uuid-for-conversation-tracking"
    }
    """
    try:
        data = request.json
        
        if not data or 'message' not in data:
            return jsonify({"error": "Missing required field: message"}), 400
        
        message = data['message']
        
        # Get or create conversation ID
        conversation_id = data.get('conversation_id')
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
        
        # Get previous context if available
        context = None
        if conversation_id in conversation_history:
            context = conversation_history[conversation_id]['last_response']
        
        # Run the query through the Weaviate Query Agent
        agent_response = run_query(message, context)
        
        # Format the response for the chatbot interface
        formatted_response = format_chatbot_response(agent_response)
        
        # Enhance the text with better formatting for candidate information
        if formatted_response['success']:
            formatted_response['response'] = enhance_candidate_response(formatted_response['response'])
        
        # Store the response in conversation history
        conversation_history[conversation_id] = {
            'last_query': message,
            'last_response': agent_response
        }
        
        # Include conversation_id in the response
        formatted_response['conversation_id'] = conversation_id
        
        return jsonify(formatted_response)
    
    except Exception as e:
        print(f"Error processing chat request: {str(e)}")
        traceback.print_exc()
        return jsonify({
            "error": f"Failed to process request: {str(e)}",
            "success": False
        }), 500

@app.route('/api/conversation/clear', methods=['POST'])
def clear_conversation():
    """
    Clear the conversation history for a specific conversation ID or all conversations.
    
    Request body should contain:
    {
        "conversation_id": "optional-uuid-for-specific-conversation"
    }
    
    If conversation_id is not provided, all conversations are cleared.
    """
    try:
        data = request.json or {}
        conversation_id = data.get('conversation_id')
        
        if conversation_id:
            if conversation_id in conversation_history:
                del conversation_history[conversation_id]
                return jsonify({"success": True, "message": f"Conversation {conversation_id} cleared"})
            else:
                return jsonify({"success": False, "message": "Conversation ID not found"}), 404
        else:
            # Clear all conversations
            conversation_history.clear()
            return jsonify({"success": True, "message": "All conversations cleared"})
    
    except Exception as e:
        print(f"Error clearing conversation: {str(e)}")
        return jsonify({
            "error": f"Failed to clear conversation: {str(e)}",
            "success": False
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({"status": "healthy"})

@app.route('/', methods=['GET'])
def homepage():
    """Simple homepage with basic information about the API"""
    api_info = {
        "name": "Candidate RAG Chatbot API",
        "description": "RESTful API for a chat-based interface to query candidate profiles",
        "endpoints": [
            {"path": "/api/chat", "method": "POST", "description": "Process chat messages"},
            {"path": "/api/conversation/clear", "method": "POST", "description": "Clear conversation history"},
            {"path": "/api/health", "method": "GET", "description": "Health check endpoint"}
        ],
        "version": "1.0.0"
    }
    return jsonify(api_info)

if __name__ == '__main__':
    print(f"Starting Candidate RAG Chatbot API on {HOST}:{PORT}")
    app.run(debug=DEBUG, host=HOST, port=PORT)
