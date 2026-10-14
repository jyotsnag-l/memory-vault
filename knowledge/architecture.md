# Atlas Project Architecture

Atlas is a project management platform used by small development teams.

The frontend is built using React.

The backend is built using Python and FastAPI.

PostgreSQL is used as the main database.

Redis is used for caching frequently requested information.

The application is divided into three major parts:

1. Frontend
2. Backend API
3. Database

The frontend communicates with the backend through REST APIs.

The backend handles authentication, project management, and task management.