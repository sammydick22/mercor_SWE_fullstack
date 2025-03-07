import ReactMarkdown from "react-markdown"

interface FormattedMessageProps {
  content: string
}

export default function FormattedMessage({ content }: FormattedMessageProps) {
  return (
    <div className="message-content">
      <ReactMarkdown
        components={{
          h1: ({ node, ...props }) => <h1 className="mb-2 text-xl font-bold" {...props} />,
          h2: ({ node, ...props }) => <h2 className="mb-2 text-lg font-bold" {...props} />,
          h3: ({ node, ...props }) => <h3 className="mb-1 text-base font-bold" {...props} />,
          p: ({ node, ...props }) => <p className="mb-2" {...props} />,
          ul: ({ node, ...props }) => <ul className="mb-2 list-inside list-disc" {...props} />,
          ol: ({ node, ...props }) => <ol className="mb-2 list-inside list-decimal" {...props} />,
          li: ({ node, ...props }) => <li className="mb-1" {...props} />,
          a: ({ node, ...props }) => (
            <a
              className="text-primary underline hover:text-primary/80"
              target="_blank"
              rel="noopener noreferrer"
              {...props}
            />
          ),
          strong: ({ node, ...props }) => <strong className="font-bold" {...props} />,
          em: ({ node, ...props }) => <em className="italic" {...props} />,
          code: ({ node, ...props }) => <code className="rounded bg-muted px-1 py-0.5 font-mono text-sm" {...props} />,
          pre: ({ node, ...props }) => (
            <pre className="mb-2 overflow-x-auto rounded bg-muted p-2 font-mono text-sm" {...props} />
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
}

