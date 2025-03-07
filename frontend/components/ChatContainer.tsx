"use client"

import { useState, useRef, useEffect } from "react"
import { v4 as uuidv4 } from "uuid"
import MessageList from "./MessageList"
import InputArea from "./InputArea"
import { sendMessage, clearConversation } from "@/services/chatService"
import type { Message } from "@/types"

export default function ChatContainer() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      content: "👋 Welcome to the Candidate RAG Chatbot! Ask me about candidates using natural language queries.",
      sender: "bot",
      timestamp: new Date(),
    },
  ])
  const [conversationId, setConversationId] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  const handleSendMessage = async (text: string) => {
    if (!text.trim()) return

    const userMessage: Message = {
      id: uuidv4(),
      content: text,
      sender: "user",
      timestamp: new Date(),
    }

    setMessages((prev) => [...prev, userMessage])
    setIsLoading(true)
    setError(null)

    // Add a loading message
    const loadingMessageId = uuidv4()
    setMessages((prev) => [
      ...prev,
      {
        id: loadingMessageId,
        content: "",
        sender: "bot",
        timestamp: new Date(),
        isLoading: true,
      },
    ])

    try {
      const response = await sendMessage(text, conversationId)

      // Remove the loading message
      setMessages((prev) => prev.filter((msg) => msg.id !== loadingMessageId))

      const botMessage: Message = {
        id: uuidv4(),
        content: response.response,
        sender: "bot",
        timestamp: new Date(),
        metadata: {
          resultCount: response.meta?.result_count,
          isPartial: response.meta?.is_partial,
          isFollowup: !!conversationId,
        },
      }

      setMessages((prev) => [...prev, botMessage])
      setConversationId(response.conversation_id)
    } catch (err) {
      // Remove the loading message
      setMessages((prev) => prev.filter((msg) => msg.id !== loadingMessageId))

      setError("Failed to get response. Please try again.")
      const errorMessage: Message = {
        id: uuidv4(),
        content: "Sorry, I encountered an error processing your request. Please try again.",
        sender: "bot",
        timestamp: new Date(),
        error: "Failed to get response",
      }
      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleClearConversation = async () => {
    try {
      if (conversationId) {
        await clearConversation(conversationId)
      }

      setMessages([
        {
          id: "welcome",
          content: "👋 Welcome to the Candidate RAG Chatbot! Ask me about candidates using natural language queries.",
          sender: "bot",
          timestamp: new Date(),
        },
      ])
      setConversationId(null)
      setError(null)
    } catch (err) {
      setError("Failed to clear conversation. Please try again.")
    }
  }

  return (
    <div className="flex h-[calc(100vh-8rem)] flex-col rounded-lg border border-border bg-background shadow-sm">
      <div className="flex items-center justify-between border-b border-border p-4">
        <h2 className="text-lg font-semibold">Candidate Search</h2>
        <button
          onClick={handleClearConversation}
          className="inline-flex h-9 items-center justify-center rounded-md border border-input bg-background px-4 py-2 text-sm font-medium ring-offset-background transition-colors hover:bg-accent hover:text-accent-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
          disabled={isLoading}
        >
          Clear Conversation
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-4">
        <MessageList messages={messages} />
        <div ref={messagesEndRef} />
      </div>

      <div className="border-t border-border p-4">
        <InputArea onSendMessage={handleSendMessage} isLoading={isLoading} />
      </div>
    </div>
  )
}

