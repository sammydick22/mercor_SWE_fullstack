"use client"

import type React from "react"

import { useState } from "react"
import { Send } from "lucide-react"

interface InputAreaProps {
  onSendMessage: (message: string) => void
  isLoading: boolean
}

const EXAMPLE_QUERIES = [
  "Find software engineers with React and AWS experience",
  "Show candidates with Master's degrees from top schools",
  "Find candidates with salary expectations under $100,000",
  "Who are the project managers with technical backgrounds?",
  "Show me candidates from Brazil with Python skills",
]

export default function InputArea({ onSendMessage, isLoading }: InputAreaProps) {
  const [message, setMessage] = useState("")
  const [showExamples, setShowExamples] = useState(false)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (message.trim() && !isLoading) {
      onSendMessage(message)
      setMessage("")
    }
  }

  const handleExampleClick = (example: string) => {
    setMessage(example)
    setShowExamples(false)
  }

  return (
    <div className="relative">
      <form onSubmit={handleSubmit} className="flex gap-2">
        <div className="relative flex-1">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask about candidates..."
            className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
            disabled={isLoading}
          />
          <button
            type="button"
            onClick={() => setShowExamples(!showExamples)}
            className="absolute right-3 top-1/2 -translate-y-1/2 text-sm text-muted-foreground hover:text-foreground"
          >
            Examples
          </button>
        </div>
        <button
          type="submit"
          disabled={!message.trim() || isLoading}
          className="inline-flex h-10 w-10 items-center justify-center rounded-md border border-input bg-background text-sm font-medium ring-offset-background transition-colors hover:bg-accent hover:text-accent-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
          aria-label="Send message"
        >
          <Send className="h-5 w-5" />
        </button>
      </form>

      {showExamples && (
        <div className="absolute left-0 right-0 top-full z-10 mt-1 rounded-md border border-border bg-background p-2 shadow-md">
          <div className="text-xs font-medium text-muted-foreground">Example queries:</div>
          <ul className="mt-1 space-y-1">
            {EXAMPLE_QUERIES.map((example, index) => (
              <li key={index}>
                <button
                  onClick={() => handleExampleClick(example)}
                  className="w-full rounded px-2 py-1 text-left text-sm hover:bg-accent"
                >
                  {example}
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}

