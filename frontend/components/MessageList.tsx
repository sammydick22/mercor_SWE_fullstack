import type { Message } from "@/types"
import FormattedMessage from "./FormattedMessage"
import LoadingIndicator from "./LoadingIndicator"

interface MessageListProps {
  messages: Message[]
}

export default function MessageList({ messages }: MessageListProps) {
  return (
    <div className="space-y-4">
      {messages.map((message) => (
        <div key={message.id} className={`flex ${message.sender === "user" ? "justify-end" : "justify-start"}`}>
          <div
            className={`max-w-[80%] rounded-lg px-4 py-2 ${
              message.sender === "user" ? "bg-primary text-primary-foreground" : "bg-muted"
            } ${message.error ? "border border-destructive" : ""}`}
          >
            {message.isLoading ? <LoadingIndicator /> : <FormattedMessage content={message.content} />}

            {message.error && <div className="mt-2 text-xs text-destructive">{message.error}</div>}

            {message.metadata?.resultCount !== undefined && (
              <div className="mt-2 text-xs opacity-70">
                {message.metadata.resultCount > 0
                  ? `Found ${message.metadata.resultCount} candidates`
                  : "No candidates found"}
                {message.metadata.isPartial && " (partial results)"}
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}

