const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000"

export async function sendMessage(message: string, conversationId?: string | null) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
        ...(conversationId && { conversation_id: conversationId }),
      }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.error || "Failed to send message")
    }

    return await response.json()
  } catch (error) {
    console.error("Error sending message:", error)
    throw error
  }
}

export async function clearConversation(conversationId?: string | null) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/conversation/clear`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...(conversationId && { conversation_id: conversationId }),
      }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.error || "Failed to clear conversation")
    }

    return await response.json()
  } catch (error) {
    console.error("Error clearing conversation:", error)
    throw error
  }
}

export async function checkHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/api/health`)

    if (!response.ok) {
      throw new Error("Health check failed")
    }

    return await response.json()
  } catch (error) {
    console.error("Error checking health:", error)
    throw error
  }
}

