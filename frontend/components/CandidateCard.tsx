"use client"

import { Copy } from "lucide-react"

interface CandidateCardProps {
  name: string
  email: string
  skills: string[]
  experience: string
  education: string
  salary?: string
  location?: string
}

export default function CandidateCard({
  name,
  email,
  skills,
  experience,
  education,
  salary,
  location,
}: CandidateCardProps) {
  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text)
    // You could add a toast notification here
  }

  return (
    <div className="rounded-lg border border-border bg-card p-4 shadow-sm">
      <div className="mb-4 flex items-start justify-between">
        <h3 className="text-xl font-bold">{name}</h3>
        <button
          onClick={() => copyToClipboard(email)}
          className="inline-flex h-8 w-8 items-center justify-center rounded-md border border-input bg-background text-sm font-medium ring-offset-background transition-colors hover:bg-accent hover:text-accent-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
          aria-label={`Copy ${name}'s email`}
        >
          <Copy className="h-4 w-4" />
        </button>
      </div>

      <div className="mb-2 flex items-center gap-2">
        <span className="text-muted-foreground">📧</span>
        <a href={`mailto:${email}`} className="text-primary hover:underline">
          {email}
        </a>
      </div>

      {location && (
        <div className="mb-2 flex items-center gap-2">
          <span className="text-muted-foreground">📍</span>
          <span>{location}</span>
        </div>
      )}

      {salary && (
        <div className="mb-2 flex items-center gap-2">
          <span className="text-muted-foreground">💰</span>
          <span>{salary}</span>
        </div>
      )}

      <div className="mb-2">
        <div className="mb-1 font-medium">Skills</div>
        <div className="flex flex-wrap gap-1">
          {skills.map((skill, index) => (
            <span key={index} className="rounded-full bg-primary/10 px-2 py-1 text-xs font-medium text-primary">
              {skill}
            </span>
          ))}
        </div>
      </div>

      <div className="mb-2">
        <div className="mb-1 font-medium">Experience</div>
        <p className="text-sm">{experience}</p>
      </div>

      <div>
        <div className="mb-1 font-medium">Education</div>
        <p className="text-sm">{education}</p>
      </div>
    </div>
  )
}

