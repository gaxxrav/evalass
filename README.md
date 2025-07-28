Feedback Management System

A full-featured feedback management application built with Django REST Framework and React. Designed for collaborative teams to collect, track, and manage user feedback efficiently.

⸻

Key Features

Backend – Django REST Framework
	•	User Authentication & Roles: Secure JWT-based login system with role-specific permissions (Admin, Moderator, Contributor)
	•	Board Management: Create and manage public or private feedback boards
	•	Feedback Handling: Full CRUD support for feedback, including status tracking, priority levels, upvoting, and tagging
	•	Comment System: Threaded discussions on feedback entries
	•	Analytics Dashboard: Visual insights with feedback trends, top-voted items, and overall stats
	•	Tagging: Organize feedback items using tags for better filtering and categorization

Frontend – React with Tailwind CSS
	•	Modern Interface: Clean, responsive UI optimized for both desktop and mobile
	•	Role-Based Access Control: Tailored views and actions depending on user roles
	•	Dashboard Overview: Quick summary of boards, feedback stats, and recent activity
	•	Multiple Feedback Views: Toggle between table and Kanban board formats; includes drag-and-drop functionality for feedback status
	•	Live Updates: Real-time UI updates for actions like voting or status changes
	•	Theme Support: Toggle between light and dark modes

⸻

Getting Started

Prerequisites
	•	Python 3.11 or later
	•	Node.js 18 or later
	•	npm or yarn

⸻

Backend Setup
	1.	Navigate to the backend directory:

cd backend


	2.	Install Python dependencies:

uv install


	3.	Apply database migrations:

uv run python manage.py migrate


	4.	Create a superuser:

uv run python manage.py createsuperuser


	5.	Start the development server:

uv run python manage.py runserver



Backend API runs at http://localhost:8000/.

⸻

Frontend Setup
	1.	Navigate to the frontend directory:

cd frontend


	2.	Install JavaScript dependencies:

npm install


	3.	Launch the frontend development server:

npm run dev



Frontend app runs at http://localhost:5173/.

⸻

Default Roles and Access

User Roles
	•	Admin: Full administrative access, including user and board management
	•	Moderator: Board-level control and feedback moderation
	•	Contributor: Can create feedback and participate in discussions

Setup Instructions
	1.	Use createsuperuser to create the first admin account
	2.	Log in via the frontend
	3.	Create boards and manage visibility/access settings
	4.	Invite users or enable public access

⸻

API Endpoints Overview

Core endpoints provided:
	•	Authentication:
/api/users/login/, /api/users/register/
	•	Users:
/api/users/, /api/users/me/
	•	Boards:
/api/boards/ (supports join/leave)
	•	Feedback:
/api/feedback/ (supports filtering and voting)
	•	Comments:
/api/comments/
	•	Tags:
/api/tags/
	•	Analytics:
/api/feedback/counts/, /api/feedback/top_voted/, /api/feedback/trends/

Full documentation available in API_DOCUMENTATION.md.

⸻

Project Structure

Frontend Pages
	•	Authentication: Login and registration pages
	•	Dashboard: Overview of statistics and recent activity
	•	Feedback List: Table and Kanban-style display with drag-and-drop
	•	Feedback Details: In-depth view with comments and voting
	•	Create Feedback: Submit new feedback forms
	•	Board Management: Admin view for managing boards and members
	•	Create Board: Form for new boards (admin/moderator access)

Notable Features
	•	Consistent top navigation across all pages
	•	UI adjusts based on user roles
	•	Feedback items support real-time status and vote updates
	•	Drag-and-drop Kanban for changing feedback status
	•	Filter and search support by tag, status, and priority
	•	Light and dark mode theme switch

⸻

Environment Variables

Backend (.env)

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:5173

Frontend (.env)

VITE_API_URL=http://localhost:8000/api


⸻

Architecture Overview

Backend
	•	Framework: Django with Django REST Framework
	•	Auth: JWT-based authentication
	•	Database: SQLite (easily switchable to PostgreSQL or MySQL)
	•	Security: CORS enabled for frontend integration

Frontend
	•	Framework: React 19 with functional components and hooks
	•	Routing: React Router
	•	Styling: Tailwind CSS
	•	API Handling: Axios
	•	Build Tool: Vite

⸻

Development Commands

Backend

# Start server
python manage.py runserver

# Migrate database
python manage.py migrate

# Make new migrations
python manage.py makemigrations

# Create admin user
python manage.py createsuperuser

# Run tests
python manage.py test

Frontend

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint the codebase
npm run lint


⸻

Deployment Guidelines
	•	Backend:
	•	Use a production database (PostgreSQL or MySQL)
	•	Set DEBUG=False
	•	Configure ALLOWED_HOSTS appropriately
	•	Frontend:
	•	Build using npm run build
	•	Serve static files from a web server (e.g., Nginx)
	•	Environment Config:
	•	Set proper API base URLs and CORS policies for production
