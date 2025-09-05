# aileens_musing

## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

###### 
Poetry package (like lerna for python)
####

(setting up in vscode)[https://www.markhneedham.com/blog/2023/07/24/vscode-poetry-python-interpreter/]

Why Poetry for Python Projects?
Each technology stack uses a standard build and dependency management process and framework. For example, Java/Kotlin uses Maven, NodeJS uses npm, JavaScript/TypeScript monorepo uses Lerna, and Docker builds use Make. Similarly, Python projects use poetry as their project dependencies, build, and packaging tool. 

Simplified Dependency Management:

Poetry provides a more straightforward and standardized way to declare and manage Python project dependencies. It simplifies the process of adding, updating, and locking dependencies in a project.

Integrated Virtual Environments:

Poetry automatically creates and manages virtual environments for your projects, isolating dependencies to avoid conflicts with system-wide packages. This ensures a clean and consistent development environment for all team members.

Enhanced Packaging and Distribution:

Poetry streamlines the process of packaging and distributing Python projects. It generates pyproject.toml files, which can be used to create distribution packages, making it easier to share your code with others.

Structured Project Metadata:

With Poetry, project metadata like the project name, version, author, and description is stored in a structured and user-friendly pyproject.toml file. This ensures consistency and makes it easier to manage project information.

Active Community and Continuous Development:

Poetry has gained widespread adoption in the Python community, and it is actively maintained and developed. This means you can expect ongoing improvements, bug fixes, and support.

Built-in Scripts and Plugins:

Poetry allows you to define custom scripts and plugins, making it flexible for different project needs. You can easily create and manage scripts for tasks like testing, documentation generation, and more.

Dependency Resolution and Locking:

Poetry uses a reliable dependency resolver to ensure consistent and predictable dependency management. It generates a poetry.lock file that guarantees that all team members use the exact same versions of dependencies.

Unified and Python-Centric Approach:

Poetry is designed specifically for Python projects, which means it understands Python's unique requirements and nuances. This Python-centric approach can lead to fewer headaches and better compatibility.

Ease of Onboarding:

Poetry's user-friendly approach simplifies onboarding for new team members, as they don't need to learn custom build scripts or makefile syntax.

Ecosystem Alignment:

Poetry aligns with modern Python packaging practices and is recommended by the Python Packaging Authority (PyPA). It keeps your project in sync with industry best practices.