# Example Queries for Candidate RAG Chatbot

This document provides curated example queries to test the capabilities of the Candidate RAG Chatbot. These examples showcase how hiring managers can use natural language to search for and evaluate candidates.

## Basic Queries

### Skills-Based Queries
```
Find candidates who know React
```

```
Who has experience with both Docker and AWS?
```

```
Find candidates with microservices experience
```

```
Show me all candidates with Python skills
```

### Education-Based Queries
```
Find candidates with a Computer Science degree
```

```
Show me candidates from top 50 universities
```

```
Who has a Master's degree or higher?
```

```
Find candidates with law degrees
```

### Experience-Based Queries
```
Find candidates with project management experience
```

```
Show me candidates who have worked at tech companies
```

```
Who has been a software engineer for multiple companies?
```

```
Find candidates with leadership experience
```

### Location-Based Queries
```
Find candidates located in the United States
```

```
Show me candidates from Brazil
```

```
Which candidates are in Argentina?
```

### Salary-Based Queries
```
Find candidates with salary expectations under $100,000
```

```
Who is asking for more than $120,000?
```

```
Show candidates with the lowest salary expectations
```

## Advanced Queries

### Compound Criteria
```
Find software engineers who know React and have salary expectations under $100,000
```

```
Show me candidates with Computer Science degrees who know Docker
```

```
Find full-stack developers from top schools with experience in startups
```

```
Who has both legal and technical skills?
```

### Specialized Searches
```
Find the most experienced candidate in web development
```

```
Who would be best for a lead developer position?
```

```
Find candidates with diverse educational backgrounds but strong technical skills
```

```
Which candidate has the most comprehensive skill set for cloud engineering?
```

### Follow-up Questions
After searching for candidates with specific criteria, try these follow-up questions:

```
Which of those candidates has the highest education level?
```

```
Can you tell me more about their work experiences?
```

```
Who has the most skills among them?
```

```
Which one would you recommend based on their overall profile?
```

## Using with the API

To use these queries with the API:

1. Start the Flask server:
   ```
   python app.py
   ```

2. Use one of these methods to test:

   **A. With test_queries.py (interactive):**
   ```
   python test_queries.py
   ```
   Then select a test category.

   **B. Direct API call with curl:**
   ```
   curl -X POST http://localhost:5000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Find candidates who know React"}'
   ```

   **C. Copy and paste any query into your frontend application connected to this API.**
