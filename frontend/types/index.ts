export interface Message {
  id: string
  content: string
  sender: "user" | "bot"
  timestamp: Date
  isLoading?: boolean
  error?: string
  metadata?: {
    resultCount?: number
    isPartial?: boolean
    isFollowup?: boolean
  }
}

export interface ConversationState {
  conversationId: string | null
  messages: Message[]
  isLoading: boolean
  error: string | null
}

export interface ApiResponse {
  response: string
  success: boolean
  meta?: {
    is_partial: boolean
    missing_information: string[]
    has_results: boolean
    result_count: number
  }
  conversation_id: string
}

export interface ClearConversationResponse {
  success: boolean
  message: string
}

export interface HealthCheckResponse {
  status: string
}

