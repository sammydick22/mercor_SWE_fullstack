import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.agents.query import QueryAgent
from weaviate.exceptions import WeaviateQueryError

# Import configuration
from config import WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY, CANDIDATE_COLLECTION, CANDIDATE_COLLECTION_DESCRIPTION

def get_weaviate_client():
    """
    Establishes a connection to the Weaviate cluster.
    
    Returns:
        A Weaviate client instance.
    """
    try:
        # Validate required API keys
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required but not provided")
        
        # Connect to Weaviate
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url=WEAVIATE_URL,
            auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
            headers={
                "X-OpenAI-Api-Key": OPENAI_API_KEY
            }
        )
        
        # Update collection description if it exists
        try:
            candidates = client.collections.get(CANDIDATE_COLLECTION)
            candidates.config.update(description=CANDIDATE_COLLECTION_DESCRIPTION)
            print(f"Updated collection description for {CANDIDATE_COLLECTION}")
        except Exception as e:
            print(f"Note: Could not update collection description: {e}")
        
        return client
    
    except Exception as e:
        print(f"Error connecting to Weaviate: {str(e)}")
        raise

def get_query_agent(client=None):
    """
    Creates a Weaviate Query Agent for the Candidates collection.
    
    Args:
        client: An existing Weaviate client instance or None to create a new one.
        
    Returns:
        A QueryAgent instance.
    """
    if client is None:
        client = get_weaviate_client()
        
    try:
        # Create the Query Agent with access to the Candidates collection
        query_agent = QueryAgent(
            client=client,
            collections=[CANDIDATE_COLLECTION]
        )
        
        return query_agent
    
    except Exception as e:
        print(f"Error creating Query Agent: {str(e)}")
        raise

def run_query(query, context=None):
    """
    Executes a natural language query using the Weaviate Query Agent.
    
    Args:
        query: The natural language query string.
        context: Optional previous query response for follow-up questions.
        
    Returns:
        The QueryAgent response.
    """
    try:
        # Get the Query Agent
        agent = get_query_agent()
        
        # Run the query
        response = agent.run(query, context=context)
        
        return response
    
    except WeaviateQueryError as e:
        print(f"Weaviate query error: {str(e)}")
        raise
    except Exception as e:
        print(f"Error executing query: {str(e)}")
        raise
