def format_chatbot_response(agent_response):
    """
    Formats a Weaviate Query Agent response into a chatbot-friendly format.
    
    Args:
        agent_response: The response object from a Weaviate Query Agent.
        
    Returns:
        A dictionary containing the formatted response.
    """
    if not agent_response or not hasattr(agent_response, 'final_answer') or not agent_response.final_answer:
        return {
            "response": "I'm sorry, I couldn't find an answer to your query. Could you try rephrasing it?",
            "success": False
        }
    
    # Extract the main answer
    main_answer = agent_response.final_answer.strip()
    
    # Extract information about whether the answer is partial
    is_partial = agent_response.is_partial_answer if hasattr(agent_response, 'is_partial_answer') else False
    missing_info = []
    if hasattr(agent_response, 'missing_information') and agent_response.missing_information:
        missing_info = [item for item in agent_response.missing_information]
    
    # Determine if there were searches that found results
    has_results = False
    search_results = []
    if hasattr(agent_response, 'searches') and agent_response.searches:
        for collection_searches in agent_response.searches:
            if collection_searches:
                has_results = True
                for result in collection_searches:
                    search_results.append(result)
    
    # Prepare the response object
    response = {
        "response": main_answer,
        "success": True,
        "meta": {
            "is_partial": is_partial,
            "missing_information": missing_info,
            "has_results": has_results,
            "result_count": len(search_results) if has_results else 0
        }
    }
    
    # If this is a follow-up question and it refers to previous candidates, note this
    if hasattr(agent_response, 'original_query') and agent_response.original_query:
        if "previous query" in agent_response.original_query.lower() or "earlier" in agent_response.original_query.lower():
            response["meta"]["is_followup"] = True
    
    return response

def enhance_candidate_response(response_text):
    """
    Enhances candidate-focused responses with structured formatting and highlighting.
    
    Args:
        response_text: The text response from the query agent.
        
    Returns:
        Enhanced text with better formatting.
    """
    # Define markers for candidate information
    markers = [
        ("name:", "👤 **Name:**"),
        ("email:", "📧 **Email:**"),
        ("phone:", "📱 **Phone:**"),
        ("location:", "📍 **Location:**"),
        ("current company:", "🏢 **Current Company:**"),
        ("current role:", "💼 **Current Role:**"),
        ("skills:", "🛠️ **Skills:**"),
        ("education:", "🎓 **Education:**"),
        ("salary expectation:", "💰 **Salary Expectation:**"),
        ("score:", "⭐ **Score:**")
    ]
    
    # Replace markers with enhanced formatting
    enhanced_text = response_text
    for marker, replacement in markers:
        enhanced_text = enhanced_text.replace(marker, replacement)
        # Also check for capitalized version
        enhanced_text = enhanced_text.replace(marker.capitalize(), replacement)
    
    return enhanced_text
