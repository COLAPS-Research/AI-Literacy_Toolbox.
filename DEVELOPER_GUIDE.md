
# Developer Documentation: AI Literacy Toolbox

### Version 1.0 | Last Updated: 2025-07-10

This document is the official technical guide for the AI Literacy Toolbox project. It is intended for developers responsible for local setup, maintenance, feature development, and troubleshooting. For a general project overview, please consult the `README.md`.

---

## Table of Contents

1.  [Architectural Overview](#1-architectural-overview)
2.  [Local Environment Setup](#2-local-environment-setup)
3.  [Codebase Structure](#3-codebase-structure)
4.  [API Endpoint Reference](#4-api-endpoint-reference)
5.  [Database Schema](#5-database-schema)
6.  [Environment Variables](#6-environment-variables)
7.  [Development Workflows](#7-development-workflows)
8.  [Coding Standards & Best Practices](#8-coding-standards--best-practices)
9.  [Troubleshooting Common Issues](#9-troubleshooting-common-issues)

---

## 1. Architectural Overview

The application employs a decoupled, multi-container architecture orchestrated by Docker Compose. This design isolates services for security, performance, and scalability. The system comprises three core services:

*   **`frontend` (Nginx):** A high-performance web server that acts as the sole public-facing entry point. It serves all static assets (HTML, CSS, JS) and functions as a reverse proxy for the backend.
*   **`backend` (Node.js/Express):** A dedicated API server responsible for all business logic, database interactions, and email notifications. It is not directly exposed to the internet.
*   **`mongo` (MongoDB):** The database service, which persists all application data.

### Request Flow Diagram

This diagram illustrates the flow of information from the user to the database:


```mermaid
graph LR
    A["User's Browser<br/>(localhost:80)"] --> B["Frontend (Nginx)<br/>- Serves static files<br/>- Proxies /api/ to backend"];
    B --> C["Backend (Node.js)<br/>(API Logic @ Port 8080)"];
    C --> D["Database (Mongo)<br/>(Data Persistence)"];

    style B fill:#e6ffed,stroke:#333,stroke-width:2px
    style C fill:#e3f2fd,stroke:#333,stroke-width:2px
    style D fill:#fef0e3,stroke:#333,stroke-width:2px


This pattern ensures that the Node.js process is not burdened with serving static files, allowing it to focus exclusively on processing API requests efficiently.

---

## 2. Local Environment Setup

### Prerequisites
*   Git
*   Docker Desktop (running and stable)

### Procedure
1.  **Clone Repository:**
    ```bash
    git clone https://github.com/ksohailwa/AI-literacy.git
    cd "AI-literacy/AI-Literacy (css upgrade)/ai_toolbox_project"
    ```
2.  **Configure Environment:**
    Create a `.env` file in the project root by copying `.env.example`. Populate it with the required credentials as defined in the [Environment Variables](#6-environment-variables) section.

3.  **Build and Launch:**
    Execute the following command from the project root. This will build fresh images for all services and start the containers in detached mode.
    ```bash
    docker-compose up --build -d
    ```

4.  **Access Services:**
    *   **Main Website:** `http://localhost:80`
    *   **Backend API Status:** `http://localhost:8080/api/status` (direct access for testing)

---

## 3. Codebase Structure

The project is organized to maintain a clear separation of concerns between frontend, backend, and configuration code.
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END

## 📂 Project Structure

The project uses a clean, separated structure for frontend and backend concerns, making it easy to navigate and maintain.

    /ai_toolbox_project/
    │
    ├── 📂 public/                # All static frontend files (HTML, CSS, JS, assets)
    │
    ├── 📂 models/                # Mongoose database schemas
    │   └── 📜 dbTools.js
    │
    ├── 📜 server.js              # The main Node.js/Express backend server
    ├── 📜 logger.js              # Winston logger configuration
    │
    ├── 🐳 Dockerfile.backend     # Docker instructions for the backend
    ├── 🐳 Dockerfile.frontend    # Docker instructions for the frontend
    ├── 📜 nginx.conf             # Nginx configuration for serving frontend & proxying API
    ├── 🐳 docker-compose.yml     # Orchestrates all services
    │
    ├── 📦 package.json           # Project dependencies and scripts
    ├── 📦 package-lock.json      # Exact dependency versions for reproducible builds
    │
    ├── 🔒 .env.example          # Example environment variables (rename to .env)
    └── 📄 .dockerignore          # Files to exclude from the Docker build


## 4. API Endpoint Reference

All API routes are prefixed with `/api`. This is configured in `nginx.conf` and `server.js`.

### Tool Submission
*   `POST /api/add-entry`
    *   **Description:** Submits a new tool for review. Validates input before processing.
    *   **Request Body (JSON):**
        ```json
        {
          "toolTitle": "string (required)",
          "email": "string (email, required)",
          "github": "string (uri, required)",
          "description": "string (required)"
        }
        ```
    *   **Responses:** `200 OK` (Success), `400 Bad Request` (Validation Error), `500 Internal Server Error`.

### Quiz System
*   `GET /api/quiz/:topic`
    *   **Description:** Retrieves quiz questions for a given topic.
    *   **URL Parameter:** `:topic` - The name of the quiz topic (e.g., "Deepfakes").
    *   **Response:** `200 OK` with a JSON array of question objects.

---

## 5. Database Schema

Schemas are defined in `/models` using Mongoose.

*   **Tool Schema (`dbTools.js`):**
    *   `toolTitle`: { type: String, required: true }
    *   `email`: { type: String, required: true }
    *   `github`: { type: String, required: true }
    *   `description`: { type: String, required: true }
    *   `type`: { type: String, enum: ['Game', 'Education', 'Other'] }
    *   `ratings`: { type: [Number], default: [] }
    *   `createdAt`: { type: Date, default: Date.now }

---

## 6. Environment Variables

These variables must be defined in the `.env` file for the backend to function correctly.

| Variable      | Description                                                          | Example                                    |
| :------------ | :------------------------------------------------------------------- | :----------------------------------------- |
| `EMAIL_USER`  | The Gmail account used for Nodemailer.                               | `youremail@gmail.com`                      |
| `EMAIL_PASS`  | **Security:** A 16-character Google App Password. Do not use your main password. | `abcdefghijklmnop`                         |
| `MONGO_URI`   | The MongoDB connection string. **Must use the Docker service name.** | `mongodb://mongo:27017/AItoolboxes`        |
| `PORT`        | The internal port the Node.js server listens on.                     | `8080`                                     |

---

## 7. Development Workflows

*   **Frontend Changes (in `/public`):**
    *   Edit HTML, CSS, or JS files. Refresh your browser to see changes. No container restart is needed.

*   **Backend Changes (`server.js`, `/models`):**
    *   Edit the necessary files. You **must** rebuild the `backend` image for changes to take effect.
    *   Run `docker-compose up --build -d backend`.

*   **Adding a New NPM Dependency:**
    1.  Install locally and save to `package.json`: `npm install <package-name> --save`.
    2.  This updates `package-lock.json`. Commit both files to Git.
    3.  Rebuild the backend image: `docker-compose up --build -d`.

---

## 8. Coding Standards & Best Practices

*   **Code Style:** This project uses Prettier for automatic code formatting and ESLint for static analysis. Please run `npm run format` and `npm run lint` before committing changes.
*   **Git Commits:** Write clear, descriptive commit messages that explain the *why* behind a change, not just the *what*.
*   **Dependencies:** Do not add a package without team consensus. All new packages must have a clear purpose.

---

## 9. Troubleshooting Common Issues

*   **Problem:** `Error: Cannot find module '...'`
    *   **Solution:** This means an NPM package is missing from `package.json` or a local file (like `./logger.js`) was not copied into the image.
    1.  For NPM packages, run `npm install <package-name> --save`.
    2.  For local files, ensure the file exists and check your `Dockerfile` and `.dockerignore` file.
    3.  You **must** run `docker-compose up --build` after fixing the files.

*   **Problem:** `docker-compose` command fails with a "cannot connect to Docker daemon" error.
    *   **Solution:** Docker Desktop is not running or has crashed. Open the Docker Desktop application, wait for its status icon to turn green, and try the command again.

*   **Problem:** `backend` container exits with `code 1` immediately after starting.
    *   **Solution:** This is a startup error. Check the container's logs immediately for the specific error message.
    *   Run `docker-compose logs backend`. The error will be near the bottom of the log output.
