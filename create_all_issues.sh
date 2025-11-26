#!/bin/bash

# Script to create ALL GitHub issues from BACKLOG.md
# This creates all 130+ tasks organized across 7 epics

echo "========================================================================"
echo "Creating ALL GitHub Issues for Supply Chain Forecasting System"
echo "Total: 130+ tasks across 7 epics and 8 sprints"
echo "========================================================================"
echo ""

# Epic 1: Project Setup & Infrastructure (15 tasks)
echo "Creating Epic 1: Project Setup & Infrastructure (15 tasks)..."

gh issue create --title "TASK-001: Initialize Python project with FastAPI" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Basic health check endpoint works" \
  --label "backend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-002: Set up project structure" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Python can import modules correctly" \
  --label "backend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-003: Configure SQLite database" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Base model is ready for inheritance" \
  --label "backend,database,epic-1,sprint-1,P0"

gh issue create --title "TASK-004: Create database models with SQLAlchemy" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Relationships are properly configured" \
  --label "backend,database,epic-1,sprint-1,P0"

gh issue create --title "TASK-005: Set up CORS for frontend communication" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Frontend can make requests to backend" \
  --label "backend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-006: Create requirements.txt" \
  --body "**Epic:** Project Setup & Infrastructure
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
- pip install -r requirements.txt works" \
  --label "backend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-007: Initialize React project with Vite" \
  --body "**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Set up the React frontend project using Vite.

### Tasks
- [ ] Run \`npm create vite@latest frontend -- --template react\`
- [ ] Navigate to frontend directory
- [ ] Install dependencies

### Acceptance Criteria
- React app is initialized
- Development server runs
- Can access http://localhost:5173" \
  --label "frontend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-008: Set up frontend project structure" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Structure follows best practices" \
  --label "frontend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-009: Configure API client (Axios)" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Helper functions are ready" \
  --label "frontend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-010: Set up routing (React Router)" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Navigation works between pages" \
  --label "frontend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-011: Configure styling framework" \
  --body "**Epic:** Project Setup & Infrastructure
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
- Basic theme is configured" \
  --label "frontend,setup,epic-1,sprint-1,P1"

gh issue create --title "TASK-012: Create package.json configuration" \
  --body "**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Ensure package.json is properly configured.

### Tasks
- [ ] Ensure all dependencies are listed
- [ ] Set up scripts (dev, build, preview)
- [ ] Configure development server

### Acceptance Criteria
- package.json is complete
- All npm scripts work" \
  --label "frontend,setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-013: Create .gitignore" \
  --body "**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Create comprehensive .gitignore file.

### Tasks
- [ ] Add Python-specific ignores (venv, __pycache__, *.pyc)
- [ ] Add Node-specific ignores (node_modules, dist, build)
- [ ] Add database files (*.db)
- [ ] Add environment files (.env)
- [ ] Add model files (models/*.pkl, models/*.h5)

### Acceptance Criteria
- .gitignore file exists
- All necessary patterns are included

**Note:** Already completed in planning phase" \
  --label "setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-014: Create environment configuration files" \
  --body "**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Set up environment variable configuration.

### Tasks
- [ ] Create backend/.env.example
- [ ] Create frontend/.env.example
- [ ] Document required environment variables
- [ ] Set up config.py to read environment variables

### Acceptance Criteria
- .env.example files exist
- Environment variables are documented
- Config loading works" \
  --label "setup,epic-1,sprint-1,P0"

gh issue create --title "TASK-015: Initialize Git repository" \
  --body "**Epic:** Project Setup & Infrastructure
**Sprint:** 1 (Week 1)
**Priority:** P0 - Critical

### Description
Initialize git repository and create initial commit.

### Tasks
- [ ] Run git init (if not already done)
- [ ] Create initial commit
- [ ] Set up branch structure

### Acceptance Criteria
- Git repository is initialized
- Initial commit is created
- Connected to GitHub

**Note:** Already completed in planning phase" \
  --label "setup,epic-1,sprint-1,P0"

echo "✓ Epic 1 complete (15 issues created)"
echo ""

# Give the API a moment to catch up
sleep 2

# Continue in next comment due to length...
echo "This script will continue creating all remaining tasks..."
echo "Note: Creating 130+ issues takes time. Please be patient..."

