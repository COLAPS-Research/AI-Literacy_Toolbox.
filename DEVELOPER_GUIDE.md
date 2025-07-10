
Developer Documentation: AI Literacy Toolbox
1. Introduction

This document provides a comprehensive technical overview of the AI Literacy Toolbox project. It is intended for developers who need to set up the project locally, understand its architecture, extend its features, or perform maintenance. For a general overview and user-facing information, please see the README.md file.

2. Architecture Overview

This project uses a modern, multi-container architecture orchestrated by Docker Compose. This design separates concerns, improves security, and enhances performance by letting each component do what it does best.

The request lifecycle is as follows:

A user's browser sends a request to the server (e.g., https://demo.colaps.team/ai-literacy-toolbox/).

The main server's reverse proxy forwards the request to our frontend (Nginx) container.

The frontend container immediately serves any static files (HTML, CSS, JS, images).

If the browser makes an API call (e.g., to /api/add-entry), the frontend container acts as a reverse proxy and forwards this specific request to our backend (Node.js) container.

The backend container processes the API request, interacts with the mongo (Database) container, and returns a JSON response.

Generated code
+----------------+      +---------------------------+      +--------------------------+      +----------------------+
| User's Browser | ---> |   Frontend (Nginx)        | ---> |   Backend (Node.js)      | ---> |   Database (Mongo)   |
|                |      |   (Serves HTML, CSS, JS)  |      |   (Handles API Logic)    |      |   (Stores Data)      |
|                |      |   (Proxies API calls)     |      |                          |      |                      |
+----------------+      +---------------------------+      +--------------------------+      +----------------------+


This architecture is highly scalable and efficient, as the high-performance Nginx server handles all static asset delivery, freeing up the Node.js process to focus solely on application logic.

3. Local Development Setup

For a step-by-step guide, please see the "Getting Started" section in the README.md. The key command to remember is:

Generated bash
# To build fresh images and start all services
docker-compose up --build
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

This command must be run from the project's root directory (where docker-compose.yml is located).

Frontend is accessible at: http://localhost:80

Backend is accessible at: http://localhost:8080 (but the frontend proxy handles this connection for you).

4. Project Structure Deep Dive

/public: Contains all client-side code. This is the only folder the frontend container knows about. All links and paths within these files should be root-relative (e.g., href="/about.html", src="/assets/logo.png").

/models: Contains all Mongoose schemas that define the structure of our data in MongoDB.

server.js: The entry point for our Node.js backend. Its main jobs are to connect to the database, define the API router, and start the Express server.

Dockerfile.backend: Instructions to build the Node.js API server image. It copies the necessary source code and runs npm install.

Dockerfile.frontend: Instructions to build the Nginx web server image. Its primary jobs are to copy the /public folder and our custom nginx.conf.

nginx.conf: This is a key file. It configures our Nginx server to:

Serve static files from the /public directory.

Proxy any request whose URL starts with /api/ to the backend service.

docker-compose.yml: The master orchestration file. It defines the three services (frontend, backend, mongo), how they connect to each other, which ports they use, and which volumes they mount.

5. API Endpoint Documentation

All API routes are defined in server.js and are prefixed with /api.

Endpoint: POST /api/add-entry

Description: Submits a new AI literacy tool to be saved in the database.

Request Body (JSON):

Generated json
{
  "toolTitle": "My Awesome Tool",
  "email": "user@example.com",
  "github": "https://github.com/user/repo",
  "description": "A brief description of the tool.",
  "type": "Game"
}
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Json
IGNORE_WHEN_COPYING_END

Success Response: 200 OK with a success message.

Error Response: 400 Bad Request if validation fails, or 500 Internal Server Error.

Endpoint: GET /api/quiz/:topic

Description: Fetches all quiz questions for a specific topic (e.g., "Deepfakes").

Success Response: 200 OK with a JSON array of question objects.

Generated json
[
  {
    "question": "What is a deepfake?",
    "options": ["A", "B", "C", "D"],
    "correctAnswer": "A"
  }
]
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Json
IGNORE_WHEN_COPYING_END

Endpoint: POST /api/quiz/submit

Description: Submits a user's answers for grading.

Request Body (JSON):

Generated json
{
  "userId": "someUserId",
  "topic": "Deepfakes",
  "answers": ["A", "C", ...]
}
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Json
IGNORE_WHEN_COPYING_END

Success Response: 200 OK with a JSON object containing the score. {"score": 85}.

6. Database Schemas

The data structure is defined using Mongoose in the /models directory.

Tool Schema:

toolTitle: String, Required

email: String, Required

github: String, Required

description: String, Required

type: String, Enum ['Game', 'Education', 'Other']

createdAt: Date, Default: Date.now

ratings: [Number]

Quiz Schema:

topic: String, Required, Unique

questions: Array of objects containing question, options, correctAnswer.

7. Environment Variables (.env)

The backend requires the following environment variables to be set in a .env file:

Variable	Description	Example
EMAIL_USER	The Gmail account used to send confirmation emails.	youremail@gmail.com
EMAIL_PASS	A 16-character Google App Password for the email account.	abcdefghijklmnop
SMTP_HOST	The SMTP server for the email provider.	smtp.gmail.com
SMTP_PORT	The port for the SMTP server.	587
MONGO_URI	The connection string for the MongoDB database. Must use the Docker service name.	mongodb://mongo:27017/AItoolboxes
PORT	The internal port the Node.js server will listen on.	8080
8. Common Development Workflows

To modify the frontend (HTML, CSS, JS):

Edit files inside the /public directory.

Simply refresh your browser. Nginx serves the updated files directly. No container restart is needed.

To modify the backend (server.js, API routes):

Edit the relevant .js files in the project root or /models.

You must rebuild and restart the backend container for the changes to take effect.

In your terminal, press Ctrl + C and run docker-compose up --build.

To add a new NPM dependency:

Run the install command locally: npm install <package-name> --save.

This will update your package.json and package-lock.json.

Rebuild the backend image to include the new package: docker-compose up --build.

To debug a container:

View logs: docker-compose logs -f backend

Open a shell inside a running container: docker-compose exec backend sh
