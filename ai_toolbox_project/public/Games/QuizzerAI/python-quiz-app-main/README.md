[![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=fff)](#)
[![Markdown](https://img.shields.io/badge/Markdown-%23000000.svg?logo=markdown&logoColor=white)](#)
[![JSON](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![PyCharm](https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=fff)](#)
![BlackFormatBadge](https://img.shields.io/badge/code%20style-black-000000.svg)

# python-quiz-app

## AI Literacy (theoretical background)
This quiz is designed to provide young people with a better understanding of AI and to raise awareness
about it. It can be used as a learning aid for educational purposes or pursued independently out of personal interest.
The quiz focuses specifically on two specific key points: deepfakes and myths versus facts about AI.
Especially Teenagers encounter AI-generated media daily, which makes it even more important to promote AI literacy within
this target group. The advantage of a quiz format lies in its ability to deliver concise, engaging, and informative content.
Therefore it is possible to ensure the audience's attention while achieving a significant learning effect.

## Overview
The Tkinter Quiz Project is an interactive application designed for learning and testing knowledge on various topics.
Users can select a topic, review relevant learning materials, take quizzes, and view their results.

## Requirements
| Requirement              | Link                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------|
| Python 3.11             | [Download](https://www.python.org/downloads/)                                         |
| Pycharm (preferred)      | [Download](https://www.jetbrains.com/pycharm/download/?section=mac)                   |
| VSCode (alternative)     | [Download](https://code.visualstudio.com/download)                                    |

## Features
| Feature               | Description                                                      |
|-----------------------|------------------------------------------------------------------|
| **Topic Selection**   | Choose from multiple available topics to start the learning journey. |
| **Learning Materials**| Review curated materials for the selected topic.                |
| **Quizzes**           | Test your knowledge with topic-specific quizzes.                |
| **Results**           | View your performance and restart the quiz as needed.           |

## Inner structure of the application
### Directory tree
This is not a complete tree, but should give a quick overview about the more relevant contents in this project.
```bash
python-quiz-app/
├── src/
│   ├── data/                # Data files for topics, learning materials, and questions
│   ├── settings/            # Application settings - home of `settings.py`
│   ├── loggers_home/        # Logging decorators
│   ├── main_application.py  # Main application logic
│   ├── pages/               # Contains all visible page components
│   ├── tests/               # Unit and integration tests
│   ├── utils/               # General utility scripts
│   └── images/              # Image assets for the application
├── setup/                   # Setup configurations and scripts
│   ├── Mac_Linux_Setup.md   # Step-by-step-guide to run the installation of packages on your Mac/Linux system
│   └── Windows_Setup.md     # Step-by-step-guide to run the installation of packages on your Windows system
├── scripts/                 # Utility scripts for managing the application
│   ├── setup_mac_linux.sh   # Script to start the application
│   └── setup_windows.sh     # Script to build the project
│── requirements.txt         # Dependencies for the project
│── setup.py                 # Installation script
└── README.md                # README and Wiki in one shot (relevant for contributing to the project)
  # Supporting utilities
```

### Pages
| Page                    | Description                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------------------|
| **Start Page**          | The entry point of the application where users can select a topic. Topics are displayed as buttons, potentially with associated images. |
| **Learning Material Page** | Displays learning materials related to the selected topic. Users can navigate through the content and proceed to quizzes.              |
| **Quiz Page**           | Contains topic-specific questions with multiple-choice options. Feedback is provided after each question, indicating whether the answer was correct or incorrect. |
| **Result Page**         | Shows the user's score after completing the quizzes. A restart button allows users to select another topic and retake the quizzes.      |

## Contribution
### **Setup the development-environment (**IMPORTANT**)**

* If you're a **Windows** user, please refer to this step-by-step guide: [Windows-User-Setup-Guide](setup/Windows_Setup.md#setup-only-needed-once)
* If you're a **MacOS or Linux** user, please refer to this step-by-step guide: [Mac-Linux-User-Setup-Guide](setup/Mac_Linux_Setup.md#setup-only-needed-once)

With these steps completed, you’re all set to start coding and enhancing the games! 🎉

### Git Hooks
To maintain code quality and enforce project standards, this repository uses Git hooks that run automatically on commits. These hooks help catch common issues, such as linting errors or formatting inconsistencies, before changes are committed.

We use [pre-commit](https://pre-commit.com/) to manage our commit hooks. This tool ensures a consistent development workflow by running checks on your staged files during the commit process.

- **Learn More**: [General Git-Hooks Documentation](https://git-scm.com/docs/githooks)
- **Installation Guide**: [Installing pre-commit](https://pre-commit.com/index.html#install)
- **Enhance existing hooks using some predefined**: [Out-of-the-box-hooks](https://github.com/pre-commit/pre-commit-hooks)

To set up the Git hooks locally, run the following command after cloning the repository:

```bash
pre-commit install
```

### Generate executable
Run from project root.
```bash
pyinstaller --onefile --paths=./src src/main.py
```

Run the executable:
`./dist/main` from repository root.

## Gitlab-CI Pipeline
GitLab CI/CD provides an automated and consistent way to build, test, and deploy applications. Its key advantages include:

- **Automation**: Streamlines repetitive tasks such as testing and deployment.
- **Efficiency**: Jobs run in parallel stages, reducing build and test time.
- **Consistency**: Ensures that builds are performed in a clean environment, avoiding "works on my machine" issues.
- **Traceability**: Provides clear logs and artifact management for debugging and review.
- **Flexibility**: Supports a variety of runners for different operating systems and environments.

### Automated Binary Creation After Merge
After merging a feature branch into the `main` branch, an automated CI/CD pipeline task is triggered to create an executable
for the application. This executable can be downloaded from the pipeline artifacts.

Currently, the pipeline includes two tasks for binary creation:

1. **Linux-compatible Executable**:
   - A `create-binary` task generates a standalone executable for Linux systems.
   - The resulting file can be downloaded from the pipeline artifacts.

2. **INACTIVE - Windows-compatible Executable**:
   - A `create-windows-binary` task is defined to create a Windows-compatible executable using a Windows runner.
   - However, this task is currently **inactive** due to the unavailability of a Windows runner in the CI/CD setup.
   - Once a Windows runner becomes available, this task will be enabled, and Windows executables can be generated automatically.

### Current Pipeline Jobs
| Job Name                 | Stage       | Description                                                    | Status                |
|--------------------------|-------------|----------------------------------------------------------------|-----------------------|
| **black**                | Lint        | Checks code formatting using `black`.                         | Active                |
| **unit-tests**           | Test        | Runs all unit tests for the application.                      | Active                |
| **create-binary**        | Deployment  | Creates a standalone Linux-compatible executable.             | Active                |
| **create-windows-binary**| Deployment  | Creates a standalone Windows-compatible executable (inactive).| Inactive (no runner)  |

## Additional Notes
- **Customization**: Update `src/settings.py` to configure themes, labels, and other settings.
- **Future Enhancements**
  - Add database (suggestion `MongoDB` or `redis`) and move data there
    - will need to fix unit-tests afterwards
  - Add support for more topics and quizzes.
  - Improve the UI/UX with modern themes.
  - Implement progress tracking and detailed performance analytics.

## License
This project is licensed under the MIT License.

Feel free to update the README further to suit your specific requirements or provide additional details about the project!
