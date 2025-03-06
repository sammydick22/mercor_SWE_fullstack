#!/usr/bin/env python3
"""
Test queries for the Candidate RAG Chatbot API.
This script provides specific tests for different candidate selection scenarios.
"""

import requests
import json
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Base URL
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

def send_query(message, conversation_id=None):
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

# ======================================================================
# Test Categories
# ======================================================================

def test_skill_based_queries():
    """Test queries related to candidate skills"""
    print("\n" + "="*80)
    print("TEST CATEGORY: SKILL-BASED QUERIES")
    print("="*80 + "\n")
    
    # Test 1: Basic skill search
    print("\nTEST 1: Basic skill search")
    print("-"*80)
    conversation_id = send_query("Find candidates who know React")
    
    time.sleep(1)  # Small delay between requests
    
    # Test 2: Multiple skills
    print("\nTEST 2: Multiple skills")
    print("-"*80)
    send_query("Find candidates who know both Docker and AWS")
    
    time.sleep(1)
    
    # Test 3: Skill with experience level
    print("\nTEST 3: Skills with implied experience")
    print("-"*80)
    send_query("Find experienced developers with Python skills")
    
    time.sleep(1)
    
    # Test 4: Niche skill combinations
    print("\nTEST 4: Niche skill combinations")
    print("-"*80)
    send_query("Who has experience with both microservices and Docker?")
    
    return conversation_id

def test_education_based_queries():
    """Test queries related to candidate education"""
    print("\n" + "="*80)
    print("TEST CATEGORY: EDUCATION-BASED QUERIES")
    print("="*80 + "\n")
    
    # Test 1: Degree type
    print("\nTEST 1: Specific degree type")
    print("-"*80)
    conversation_id = send_query("Find candidates with a Master's degree")
    
    time.sleep(1)
    
    # Test 2: Field of study
    print("\nTEST 2: Field of study")
    print("-"*80)
    send_query("Show me candidates who studied Computer Science")
    
    time.sleep(1)
    
    # Test 3: Prestigious schools
    print("\nTEST 3: Top schools")
    print("-"*80)
    send_query("Find candidates from top 50 universities")
    
    time.sleep(1)
    
    # Test 4: Education + skills
    print("\nTEST 4: Education with skills")
    print("-"*80)
    send_query("Find law school graduates with technical skills")
    
    return conversation_id

def test_experience_based_queries():
    """Test queries related to work experience"""
    print("\n" + "="*80)
    print("TEST CATEGORY: EXPERIENCE-BASED QUERIES")
    print("="*80 + "\n")
    
    # Test 1: Current role
    print("\nTEST 1: Current role")
    print("-"*80)
    conversation_id = send_query("Find current software engineers")
    
    time.sleep(1)
    
    # Test 2: Specific company experience
    print("\nTEST 2: Company experience")
    print("-"*80)
    send_query("Which candidates have worked at tech companies?")
    
    time.sleep(1)
    
    # Test 3: Job title search
    print("\nTEST 3: Job title search")
    print("-"*80)
    send_query("Find candidates with project manager experience")
    
    time.sleep(1)
    
    # Test 4: Career progression
    print("\nTEST 4: Career progression")
    print("-"*80)
    send_query("Find candidates who have had multiple engineering roles")
    
    return conversation_id

def test_salary_based_queries():
    """Test queries related to salary expectations"""
    print("\n" + "="*80)
    print("TEST CATEGORY: SALARY-BASED QUERIES")
    print("="*80 + "\n")
    
    # Test 1: Salary range
    print("\nTEST 1: Salary range")
    print("-"*80)
    conversation_id = send_query("Find candidates with salary expectations between $80,000 and $100,000")
    
    time.sleep(1)
    
    # Test 2: Maximum salary
    print("\nTEST 2: Maximum salary")
    print("-"*80)
    send_query("Show candidates with salary expectations under $120,000")
    
    time.sleep(1)
    
    # Test 3: Salary with skills
    print("\nTEST 3: Salary with skills")
    print("-"*80)
    send_query("Find React developers with salary expectations under $100,000")
    
    return conversation_id

def test_location_based_queries():
    """Test queries related to candidate locations"""
    print("\n" + "="*80)
    print("TEST CATEGORY: LOCATION-BASED QUERIES")
    print("="*80 + "\n")
    
    # Test 1: Specific location
    print("\nTEST 1: Specific location")
    print("-"*80)
    conversation_id = send_query("Find candidates from the United States")
    
    time.sleep(1)
    
    # Test 2: Location with skills
    print("\nTEST 2: Location with skills")
    print("-"*80)
    send_query("Find developers in Brazil who know Python")
    
    time.sleep(1)
    
    # Test 3: Remote work implication
    print("\nTEST 3: Remote work implication")
    print("-"*80)
    send_query("Which candidates are located internationally but have technical skills?")
    
    return conversation_id

def test_complex_queries():
    """Test complex queries with multiple criteria"""
    print("\n" + "="*80)
    print("TEST CATEGORY: COMPLEX MULTI-CRITERIA QUERIES")
    print("="*80 + "\n")
    
    # Test 1: Skills + Education + Salary
    print("\nTEST 1: Skills + Education + Salary")
    print("-"*80)
    conversation_id = send_query("Find candidates with Computer Science degrees who know AWS and have salary expectations under $120,000")
    
    time.sleep(1)
    
    # Test 2: Experience + Location + Skills
    print("\nTEST 2: Experience + Location + Skills")
    print("-"*80)
    send_query("Find experienced engineers from Brazil or Argentina who know React")
    
    time.sleep(1)
    
    # Test 3: Complete profile analysis
    print("\nTEST 3: Complete profile evaluation")
    print("-"*80)
    send_query("Find the most qualified full-stack developer based on skills, experience, and education")
    
    time.sleep(1)
    
    # Test 4: Diversity-focused
    print("\nTEST 4: Diversity-focused")
    print("-"*80)
    send_query("Find candidates with diverse educational backgrounds who have technical skills")
    
    return conversation_id

def test_followup_questions():
    """Test follow-up questions that reference previous queries"""
    print("\n" + "="*80)
    print("TEST CATEGORY: FOLLOW-UP QUESTIONS")
    print("="*80 + "\n")
    
    # Initial query
    print("\nInitial Query: Find software engineers with React experience")
    print("-"*80)
    conversation_id = send_query("Find software engineers with React experience")
    
    if not conversation_id:
        print("Failed to get conversation ID, can't test follow-ups")
        return None
    
    time.sleep(1)
    
    # Follow-up 1: Further filtering
    print("\nFollow-up 1: Further filtering")
    print("-"*80)
    send_query("Which ones have experience with AWS?", conversation_id)
    
    time.sleep(1)
    
    # Follow-up 2: Additional information
    print("\nFollow-up 2: Additional information")
    print("-"*80)
    send_query("Tell me more about their education backgrounds", conversation_id)
    
    time.sleep(1)
    
    # Follow-up 3: Comparison
    print("\nFollow-up 3: Comparison")
    print("-"*80)
    send_query("Who has the highest salary expectations among them?", conversation_id)
    
    time.sleep(1)
    
    # Follow-up 4: Recommendation
    print("\nFollow-up 4: Recommendation")
    print("-"*80)
    send_query("Which one would you recommend as the best candidate?", conversation_id)
    
    return conversation_id

if __name__ == "__main__":
    if not health_check():
        print("Please start the API server first by running 'python app.py'")
        exit(1)
    
    print("\n" + "="*80)
    print("CANDIDATE RAG CHATBOT TEST QUERIES")
    print("="*80)
    print("\nRunning comprehensive tests to evaluate the chatbot's capabilities...")
    
    try:
        # Get test selection
        print("\nAvailable test categories:")
        print("1. Skill-based queries")
        print("2. Education-based queries")
        print("3. Experience-based queries")
        print("4. Salary-based queries")
        print("5. Location-based queries")
        print("6. Complex multi-criteria queries")
        print("7. Follow-up questions")
        print("8. Run ALL tests")
        
        choice = input("\nSelect a test category (1-8): ")
        
        if choice == '1':
            test_skill_based_queries()
        elif choice == '2':
            test_education_based_queries()
        elif choice == '3':
            test_experience_based_queries()
        elif choice == '4':
            test_salary_based_queries()
        elif choice == '5':
            test_location_based_queries()
        elif choice == '6':
            test_complex_queries()
        elif choice == '7':
            test_followup_questions()
        elif choice == '8':
            # Run all tests sequentially
            print("\nRunning ALL test categories...\n")
            test_skill_based_queries()
            time.sleep(2)
            test_education_based_queries()
            time.sleep(2)
            test_experience_based_queries()
            time.sleep(2)
            test_salary_based_queries()
            time.sleep(2)
            test_location_based_queries()
            time.sleep(2)
            test_complex_queries()
            time.sleep(2)
            test_followup_questions()
        else:
            print("Invalid selection. Please run the script again.")
        
        print("\n" + "="*80)
        print("TESTS COMPLETE")
        print("="*80 + "\n")
    
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user. Exiting...")
