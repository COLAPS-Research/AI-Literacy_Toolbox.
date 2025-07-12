AI Literacy Toolbox 🤖

![alt text](https://img.shields.io/badge/License-MIT-blue.svg)
![alt text](https://img.shields.io/badge/build-passing-brightgreen.svg)
![alt text](https://img.shields.io/badge/Docker-Powered-blue?logo=docker)
![alt text](https://img.shields.io/badge/Node.js-Fullstack-green?logo=nodedotjs)

The AI Literacy Toolbox is a comprehensive web platform designed to empower students, educators, and enthusiasts with the knowledge and skills to understand, evaluate, and effectively use Artificial Intelligence. Developed as a project at the University of Duisburg-Essen, this application combines educational content with interactive tools in a fully containerized, easy-to-deploy package.

Our mission is to close the AI knowledge gap by providing a collaborative platform where the community can learn and contribute.

✨ Core Features

📚 Educational Content: Interactive modules and resources explaining key AI concepts, ethics, and applications.

🛠️ Interactive Tools: A curated collection of games and tools designed to teach AI principles in a hands-on way.

🚀 Community Submissions: A simple and secure form for users to submit their own AI literacy tools to the platform.

📫 Automated Email Notifications: A backend service that sends email confirmations for successful tool submissions.

📦 Self-Contained Deployment: The entire application is designed to run under a specific URL path (/ai-literacy-toolbox/), making it easy to deploy on a shared server without complex proxy rules.

🐳 Fully Containerized: The entire stack (Node.js Fullstack App + Database) is managed with Docker and Docker Compose for a one-command setup.

🚀 Live Demo

You can access a live version of the project deployed on our university's server:

https://demo.colaps.team/ai-literacy-toolbox/

🛠️ Technology Stack

This project is built with a modern, reliable stack where the Node.js server handles both API and frontend duties.

Component	Technology
Frontend	
![alt text](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white)
![alt text](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white)
![alt text](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black)

Backend	
![alt text](https://img.shields.io/badge/-Node.js-339933?logo=nodedotjs&logoColor=white)
![alt text](https://img.shields.io/badge/-Express.js-000000?logo=express&logoColor=white)

Database	
![alt text](https://img.shields.io/badge/-MongoDB-47A248?logo=mongodb&logoColor=white)

Containerization	
![alt text](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white)

Development Tools	
![alt text](https://img.shields.io/badge/-ESLint-4B32C3?logo=eslint&logoColor=white)
![alt text](https://img.shields.io/badge/-Prettier-F7B93E?logo=prettier&logoColor=black)
![alt text](https://img.shields.io/badge/-Nodemon-76D04B?logo=nodemon&logoColor=white)


📂 Project Structure

The project uses a clean, separated structure for frontend and backend concerns, making it easy to navigate and maintain.

    /ai_toolbox_project/
    │
    ├──  public/                # All static frontend files (HTML, CSS, JS, assets)
    │
    ├──  models/                # Mongoose database schemas
    │   └──  dbTools.js
    │
    ├──  server.js              # The main Node.js/Express backend server
    ├──  logger.js              # Winston logger configuration
    │
    ├──  Dockerfile.backend     # Docker instructions for the backend
    ├──  nginx.conf             # Nginx configuration for serving frontend & proxying API
    ├──  docker-compose.yml     # Orchestrates all services
    │
    ├──  package.json           # Project dependencies and scripts
    ├──  package-lock.json      # Exact dependency versions for reproducible builds
    │
    ├──  .env.example          # Example environment variables (rename to .env)
    └──  .dockerignore          # Files to exclude from the Docker build


⚙️ Getting Started: Local Development Setup

Follow these steps to get the entire application running on your local machine.

Prerequisites

Git

Docker Desktop

Installation Steps

Clone the repository:

git clone https://github.com/your-username/your-new-repo.git

Navigate to the project directory:

cd your-new-repo

Create the environment file (.env):
Create a new file named .env in the project root. Copy the contents of .env.example into it and fill in your actual credentials.

<details>
<summary>Click to see `.env` template</summary>

Generated env
# --- Application Path ---
BASE_PATH=/ai-literacy-toolbox

# --- Email Server (SMTP) Configuration ---
# WARNING: Use a 16-character Google App Password, not your main account password.
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_16_character_app_password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587

# --- Database Configuration ---
# This is correctly configured for Docker. Do not change.
MONGO_URI=mongodb://mongo:27017/AItoolboxes

# --- Application Server Port ---
# The internal port for the Node.js app. Do not change.
PORT=8080

</details>

Run npm install (First time only):
This command will generate your package-lock.json file based on package.json.

npm install

Build and Run the Application:
This single command will build the Docker image and start both the application and database containers.

docker-compose up --build

Access the Application:
Your entire application is exposed on port 80, the standard web port.

Main Entry Point: Open your browser to http://localhost/ai-literacy-toolbox/

To check the backend status: Visit http://localhost/ai-literacy-toolbox/api/status

Note: You do not need to use port 8080 in your browser. Docker handles the mapping for you.

▶️ Running the Application

To start all services: docker-compose up

To stop all services: Press Ctrl + C in the terminal, then run docker-compose down.

🤝 How to Contribute

We welcome contributions! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-awesome-feature).

Make your changes.

Commit your changes (git commit -m 'Add some awesome feature').

Push to the branch (git push origin feature/your-awesome-feature).

Open a Pull Request.

👥 The Team

This project was brought to life by a dedicated team of students:

Khan Sohail

Kevin Flotow

Mohammadreza Zahedizadehgan

Rabia Karabulut

Tharani Uruthirakumar

Gousiha Rammohan

Supervised by:

Prof. Dr. Irene-Angelica Chounta

📜 License

This project is licensed under the MIT License - see the LICENSE.md file for details.


This project is licensed under the MIT License - see the LICENSE.md file for details.
