#!/usr/bin/env python3
"""
Test script for the Candidate RAG Chatbot API.
This script demonstrates how to interact with the API using Python requests.
"""

import requests
import json
import os
import time
from dotenv import load_dotenv

# Load environment variables to get the API URL
load_dotenv()

# API Base URL (default to localhost if not specified)
API_BASE_URL = os.getenv("API_URL", "http://localhost:5000")

def print_response(response):
    """Pretty print API response"""
    if response.status_code == 200:
        data = response.json()
        
        print("\n" + "="*80)
        print("CHAT RESPONSE")
        print("="*80)
        
        if data.get('success'):
            print("\n" + data.get('response', 'No response text') + "\n")
            
            # Print metadata
            if 'meta' in data:
                print("-"*80)
                print("METADATA:")
                for key, value in data['meta'].items():
                    print(f"- {key}: {value}")
                
            # Print conversation ID
            print("-"*80)
            print(f"Conversation ID: {data.get('conversation_id', 'N/A')}")
        else:
            print(f"\nError: {data.get('error', 'Unknown error')}")
        
        print("="*80 + "\n")
    else:
        print(f"\nError: {response.status_code} - {response.text}\n")

def chat_query(message, conversation_id=None):
    """Send a chat query to the API"""
    url = f"{API_BASE_URL}/api/chat"
    
    payload = {
        "message": message
    }
    
    if conversation_id:
        payload["conversation_id"] = conversation_id
    
    print(f"Sending query: '{message}'")
    if conversation_id:
        print(f"With conversation ID: {conversation_id}")
    
    try:
        response = requests.post(url, json=payload, timeout=60)
        print_response(response)
        
        # Return conversation ID if successful
        if response.status_code == 200:
            return response.json().get('conversation_id')
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def clear_conversation(conversation_id=None):
    """Clear a conversation or all conversations"""
    url = f"{API_BASE_URL}/api/conversation/clear"
    
    payload = {}
    if conversation_id:
        payload["conversation_id"] = conversation_id
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            if conversation_id:
                print(f"Conversation {conversation_id} cleared successfully.")
            else:
                print("All conversations cleared successfully.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def health_check():
    """Check if the API is running"""
    url = f"{API_BASE_URL}/api/health"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("API is healthy and running!")
            return True
        else:
            print(f"API health check failed: {response.status_code} - {response.text}")
            return False
    
    except requests.exceptions.RequestException as e:
        print(f"API health check failed: {e}")
        return False

def run_demo():
    """Run a demonstration of the chatbot with several example queries"""
    print("\n" + "="*80)
    print("CANDIDATE RAG CHATBOT API DEMO")
    print("="*80 + "\n")
    
    # Check if API is running
    if not health_check():
        print("Please start the API server first by running 'python app.py'")
        return
    
    # Example 1: Basic candidate query
    print("\nEXAMPLE 1: Finding software engineers with specific skills")
    print("-"*80)
    conversation_id = chat_query("Find me software engineers with experience in React and Python")
    
    time.sleep(1)  # Small delay between requests
    
    # Example 2: Follow-up question using conversation context
    if conversation_id:
        print("\nEXAMPLE 2: Follow-up question (using previous context)")
        print("-"*80)
        chat_query("Which ones have the highest salary expectations?", conversation_id)
        
        time.sleep(1)  # Small delay between requests
        
        # Example 3: Another follow-up
        print("\nEXAMPLE 3: Another follow-up question")
        print("-"*80)
        chat_query("Can you tell me more about their education?", conversation_id)
        
        # Clear this conversation when done
        time.sleep(1)
        clear_conversation(conversation_id)
    
    # Example 4: New conversation with education filter
    print("\nEXAMPLE 4: Filtering by education")
    print("-"*80)
    conversation_id = chat_query("Show candidates with degrees from top schools who know Docker")
    
    time.sleep(1)
    
    # Clear all conversations at the end
    print("\nClearing all conversations...")
    clear_conversation()
    
    print("\n" + "="*80)
    print("DEMO COMPLETE")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_demo()
