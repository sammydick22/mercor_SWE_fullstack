# Candidate RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for candidate selection, built with Flask and Weaviate. This API provides a natural language interface to query candidate profiles stored in a Weaviate vector database.

## Overview

This chatbot enables hiring managers to interact with candidate data using natural language queries. The system leverages Weaviate's Query Agent to perform semantic searches, retrieve relevant candidate profiles, and generate conversational responses.

Key features:
- Natural language queries for candidate selection
- Contextual follow-up questions
- Automated candidate scoring and evaluation
- Conversation history tracking

## Prerequisites

- Python 3.9+
- [Weaviate Cloud](https://weaviate.io/cloud) account with a running instance
- OpenAI API key for the LLM component

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd candidate-rag-chatbot
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file to add your OpenAI API key and adjust other settings as needed.

## Running the API

Start the Flask server:
```
python app.py
```

The API will be available at: `http://localhost:5000`

## API Endpoints

### `POST /api/chat`

Process a chatbot query and return candidate recommendations.

**Request Body:**
```json
{
  "message": "Find top full-stack candidates with diverse backgrounds",
  "conversation_id": "optional-uuid-for-conversation-tracking"
}
```

**Response:**
```json
{
  "response": "👤 **Name:** John Doe\n📧 **Email:** john@example.com\n...",
  "success": true,
  "meta": {
    "is_partial": false,
    "missing_information": [],
    "has_results": true,
    "result_count": 3
  },
  "conversation_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

### `POST /api/conversation/clear`

Clear conversation history.

**Request Body:**
```json
{
  "conversation_id": "optional-uuid-for-specific-conversation"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Conversation 123e4567-e89b-12d3-a456-426614174000 cleared"
}
```

### `GET /api/health`

Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Example Queries

Here are some example queries you can use with the chatbot:

### Finding candidates by skills
```
Find me software engineers with experience in React and Python
```

### Filtering by education
```
Show candidates with degrees from top 50 schools who know Docker
```

### Salary-based queries
```
Who are the full-stack developers with salary expectations under $100,000?
```

### Experience-based queries
```
Find candidates with more than 3 work experiences in the tech industry
```

### Follow-up queries
```
Which of those candidates have experience with AWS?
```

## Weaviate Schema

This project works with a Weaviate collection named "Candidates" that has the following properties:

- `name`: Candidate's full name
- `email`: Contact email address
- `phone`: Contact phone number
- `location`: Geographic location
- `submitted_at`: Timestamp of application submission
- `work_availability`: List of availability options (full-time, part-time)
- `salary_expectation`: Expected salary
- `work_experiences`: Array of work experience objects
- `current_company`: Current/most recent employer
- `current_role`: Current/most recent job title
- `education_highest_level`: Highest degree obtained
- `education_degrees`: Array of education degree objects
- `primary_degree_subject`: Field of study for primary degree
- `primary_degree_school`: Institution name for primary degree
- `skills`: Array of skills
- `skills_text`: Comma-separated string of skills
- `is_top_school`: Boolean indicating if candidate attended a top-ranked school

## License

[Your License Information]
