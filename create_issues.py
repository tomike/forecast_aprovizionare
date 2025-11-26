#!/usr/bin/env python3
"""
Script to create GitHub issues from the backlog
Prerequisites:
1. Install requests: pip install requests
2. Create a GitHub Personal Access Token:
   - Go to https://github.com/settings/tokens
   - Generate new token (classic)
   - Select scopes: repo (full control)
3. Set environment variables:
   export GITHUB_TOKEN="your_token_here"
   export GITHUB_REPO="username/forecast_aprovizionare"
4. Run: python create_issues.py
"""

import os
import requests
import json

# Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")  # Format: "username/repo-name"

if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set")
    print("Create a token at: https://github.com/settings/tokens")
    exit(1)

if not GITHUB_REPO:
    print("Error: GITHUB_REPO environment variable not set")
    print("Format: username/repo-name")
    exit(1)

API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_issue(title, body, labels):
    """Create a GitHub issue"""
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }

    response = requests.post(API_URL, headers=HEADERS, json=data)

    if response.status_code == 201:
        issue = response.json()
        print(f"✓ Created: {title} (#{issue['number']})")
        return issue
    else:
        print(f"✗ Failed to create: {title}")
        print(f"  Status: {response.status_code}")
        print(f"  Response: {response.text}")
        return None

# Epic 1: Project Setup & Infrastructure
print("=" * 80)
print("Creating Epic 1 issues: Project Setup & Infrastructure")
print("=" * 80)

create_issue(
    "TASK-001: Initialize Python project with FastAPI",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Initialize the Python backend project with FastAPI framework.

### Tasks
- [ ] Create backend directory structure
- [ ] Initialize virtual environment
- [ ] Install FastAPI and uvicorn
- [ ] Create main.py with basic FastAPI app
- [ ] Test server startup

### Acceptance Criteria
- FastAPI application runs successfully
- Can access http://localhost:8000
- Basic health check endpoint works""",
    ["backend", "setup", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-002: Set up project structure",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Create proper Python project structure for the backend.

### Tasks
- [ ] Create app/ directory and subdirectories (models, schemas, api, services, ml_models)
- [ ] Create __init__.py files in all packages
- [ ] Set up proper Python package structure

### Acceptance Criteria
- All directories exist
- Python can import modules correctly""",
    ["backend", "setup", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-003: Configure SQLite database",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Set up SQLite database with SQLAlchemy ORM.

### Tasks
- [ ] Install SQLAlchemy
- [ ] Create database.py with database connection logic
- [ ] Set up session management
- [ ] Create Base model for ORM

### Acceptance Criteria
- Database connection works
- Session management is implemented
- Base model is ready for inheritance""",
    ["backend", "database", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-004: Create database models with SQLAlchemy",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Implement all database models using SQLAlchemy ORM.

### Tasks
- [ ] Implement Product model (models/product.py)
- [ ] Implement SalesData model (models/sales.py)
- [ ] Implement Forecast model (models/forecast.py)
- [ ] Implement ModelMetadata model (models/model_metadata.py)
- [ ] Create database initialization script

### Acceptance Criteria
- All models are defined
- Tables are created in database
- Relationships are properly configured""",
    ["backend", "database", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-005: Set up CORS for frontend communication",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Configure CORS middleware to allow frontend-backend communication.

### Tasks
- [ ] Install python-cors
- [ ] Configure CORS middleware in main.py
- [ ] Set allowed origins for development

### Acceptance Criteria
- CORS is configured
- Frontend can make requests to backend""",
    ["backend", "setup", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-006: Create requirements.txt",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Document all Python dependencies in requirements.txt.

### Tasks
- [ ] List all Python dependencies
- [ ] Pin versions for reproducibility
- [ ] Include: fastapi, uvicorn, sqlalchemy, pandas, numpy, prophet, tensorflow, xgboost, scikit-learn, python-multipart, openpyxl

### Acceptance Criteria
- requirements.txt exists
- All dependencies are listed with versions
- `pip install -r requirements.txt` works""",
    ["backend", "setup", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-007: Initialize React project with Vite",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Set up the React frontend project using Vite.

### Tasks
- [ ] Run `npm create vite@latest frontend -- --template react`
- [ ] Navigate to frontend directory
- [ ] Install dependencies

### Acceptance Criteria
- React app is initialized
- Development server runs
- Can access http://localhost:5173""",
    ["frontend", "setup", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-008: Set up frontend project structure",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Create organized folder structure for React application.

### Tasks
- [ ] Create src/components directory with subdirectories (Upload, Training, Dashboard, common)
- [ ] Create src/pages directory
- [ ] Create src/services directory
- [ ] Set up folder organization

### Acceptance Criteria
- All directories exist
- Structure follows best practices""",
    ["frontend", "setup", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-009: Configure API client (Axios)",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Set up Axios for API communication with backend.

### Tasks
- [ ] Install axios
- [ ] Create services/api.js with base configuration
- [ ] Set up API base URL
- [ ] Create API helper functions

### Acceptance Criteria
- Axios is configured
- API base URL is set
- Helper functions are ready""",
    ["frontend", "setup", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-010: Set up routing (React Router)",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Configure React Router for navigation.

### Tasks
- [ ] Install react-router-dom
- [ ] Configure routes in App.jsx
- [ ] Create route structure for Upload, Training, Dashboard pages

### Acceptance Criteria
- Routing is configured
- Navigation works between pages""",
    ["frontend", "setup", "epic-1", "sprint-1", "P0"]
)

create_issue(
    "TASK-011: Configure styling framework",
    """**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P1 - High

### Description
Set up CSS framework for consistent styling.

### Tasks
- [ ] Choose between Material-UI or Tailwind CSS
- [ ] Install chosen framework
- [ ] Set up basic theme/configuration
- [ ] Create common styling utilities

### Acceptance Criteria
- CSS framework is installed
- Basic theme is configured""",
    ["frontend", "setup", "epic-1", "sprint-1", "P1"]
)

print("\n" + "=" * 80)
print("Sample issues created successfully!")
print("=" * 80)
print("\nThis script created the first 11 issues as examples.")
print("You can extend it to create all 130+ issues from the BACKLOG.md")
print("\nNext steps:")
print("1. Check your GitHub repository for the created issues")
print("2. Extend this script to include all tasks from BACKLOG.md")
print("3. Organize issues with milestones and projects (optional)")
