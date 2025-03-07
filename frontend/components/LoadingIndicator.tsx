export default function LoadingIndicator() {
  return (
    <div className="flex items-center space-x-2">
      <div className="text-sm">Thinking</div>
      <div className="flex space-x-1">
        <div className="h-2 w-2 animate-bounce rounded-full bg-current"></div>
        <div className="h-2 w-2 animate-bounce rounded-full bg-current [animation-delay:0.2s]"></div>
        <div className="h-2 w-2 animate-bounce rounded-full bg-current [animation-delay:0.4s]"></div>
      </div>
    </div>
  )
}

