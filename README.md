# Quave Code Challenge

Want to join Quave as a developer? 

Great! Read this document and submit your solution.

We hire full stack developers only, so you must be comfortable with both front-end and back-end development.

Good luck!

> Not sure if we have open positions right now? Check our [Join repository](https://github.com/quavedev/join/issues/).

# Submission

## Getting Started

Create a private github repository from this template and share it with us: @renanccastro @filipenevola @rafaportobraga.

## Review

Ready for review? Fill out this [form](https://forms.gle/m2FTwSG8bcMfhS3JA).

You will provide a link to your solution repository in the form and also a cover letter. In the letter you should explain why you're a great fit and what you'll bring to Quave

## Feedback

We'll give you feedback based on the position description. Check the timeline section in the job posting for feedback deadlines.

# Code Stack and Environment

## Introduction

At Quave, we use Vue.js and .NET for some clients, projects, and products.

Vue.js is a progressive JavaScript framework that makes building user interfaces a breeze, while .NET provides a robust and scalable backend platform.

Our stack leverages Vue.js 2.x for the frontend, providing excellent component-based architecture and reactivity system, paired with .NET's powerful features including:
- Authentication
- Background Jobs
- Entity Framework Core
- REST APIs
- Email Services
- And more

## Required Stack

We want to see your Vue.js and .NET skills.

Your solution must use:
- Frontend: Vue.js 2.x
- Backend: .NET 8 (or latest stable version)
- Database: SQL Server or PostgreSQL
- Styling: Tailwind CSS

The solution must:
- Use the same data structure as provided in the seed data
- Work with `npm i && npm start` for the frontend
- Work with standard .NET CLI commands for the backend
- Include clear instructions for setting up the database
- Be compatible with the latest LTS version of Node.js

## Machine Setup

1. Install Node.js
   - Use [nvm](https://github.com/nvm-sh/nvm#installing-and-updating)
2. Install [.NET SDK](https://dotnet.microsoft.com/download)
3. Install your chosen database system

## Install Dependencies

```bash
# Frontend
cd frontend
npm install

# Backend
cd backend
dotnet restore
```

## Run the App

```bash
# Frontend
cd frontend
npm start

# Backend
cd backend
dotnet run
```

# Scope

## Requirements

Build a mini-app for event check-ins. The home page needs:

1. Event selector showing event names from the `communities` table
   - Default text: "Select an event"

2. List of registered people from the `people` table showing:
   - Full name (first + last name)
   - Company name
   - Title
   - Check-in date (MM/DD/YYYY, HH:mm or N/A)
   - Check-out date (MM/DD/YYYY, HH:mm or N/A)
   - "Check-in {person name}" button
   - "Check-out {person name}" button (shows 5 seconds after check-in)

3. Event summary showing:
   - Current attendee count
   - Company breakdown of current attendees
   - Number of people not checked in

The page should maintain an up-to-date view of the data, ensuring users see changes promptly.

## Implementation Rules

1. Use:
   - .NET for the backend API
   - Vue.js 2.x for frontend views
   - SQL Server or PostgreSQL for data
   - TailwindCSS for styling

2. App must:
   - Have clear setup instructions in README
   - Run frontend on port `3000`
   - Include database migrations and seed data
   - Include API documentation (Swagger/OpenAPI recommended)

# AI Tools

You can use AI tools to generate code, but you must:
1. Understand all generated code
2. Explain why it's the best solution
3. Answer any related questions in the interview

Not understanding your code = disqualification.

# Note

We won't answer questions about this challenge to ensure fair evaluation.
