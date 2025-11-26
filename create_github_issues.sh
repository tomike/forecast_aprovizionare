#!/bin/bash

# Script to create GitHub issues from the backlog
# Prerequisites:
# 1. Install GitHub CLI: brew install gh (on macOS)
# 2. Authenticate: gh auth login
# 3. Create GitHub repository: gh repo create forecast_aprovizionare --public (or --private)
# 4. Run this script: bash create_github_issues.sh

echo "Creating GitHub issues for Supply Chain Forecasting System..."

# Epic 1: Project Setup & Infrastructure
echo "Creating Epic 1 issues..."

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
- All necessary patterns are included" \
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
- Connected to GitHub" \
  --label "setup,epic-1,sprint-1,P0"

# Epic 2: Data Management
echo "Creating Epic 2 issues..."

gh issue create --title "TASK-016: Create file upload endpoint (Backend)" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P0 - Critical

### Description
Implement POST /api/upload endpoint for file uploads.

### Tasks
- [ ] Implement POST /api/upload endpoint in api/upload.py
- [ ] Handle multipart/form-data
- [ ] Save uploaded file to data/uploads directory
- [ ] Return upload confirmation with file ID

### Acceptance Criteria
- Endpoint accepts file uploads
- Files are saved correctly
- Returns proper response" \
  --label "backend,api,epic-2,sprint-2,P0"

gh issue create --title "TASK-017: Implement CSV parsing" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P0 - Critical

### Description
Implement CSV file parsing functionality.

### Tasks
- [ ] Create data_processor.py in services/
- [ ] Implement CSV file reading with pandas
- [ ] Extract required columns (date, sku, quantity)
- [ ] Handle optional columns (product_name, category)

### Acceptance Criteria
- CSV files are parsed correctly
- Required columns are extracted
- Optional columns are handled" \
  --label "backend,data-processing,epic-2,sprint-2,P0"

gh issue create --title "TASK-018: Implement Excel parsing" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P0 - Critical

### Description
Add Excel file parsing support.

### Tasks
- [ ] Install openpyxl
- [ ] Add Excel file reading support
- [ ] Handle multiple sheets (use first sheet by default)
- [ ] Convert to standard format

### Acceptance Criteria
- Excel files are parsed correctly
- Works with .xlsx and .xls formats
- Data format matches CSV output" \
  --label "backend,data-processing,epic-2,sprint-2,P0"

gh issue create --title "TASK-019: Create data validation logic" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P0 - Critical

### Description
Implement comprehensive data validation.

### Tasks
- [ ] Validate required columns exist
- [ ] Check date format (YYYY-MM-DD)
- [ ] Validate numeric values for quantity
- [ ] Check for empty/null values
- [ ] Return validation errors with details

### Acceptance Criteria
- All validation rules are implemented
- Clear error messages are returned
- Invalid data is rejected" \
  --label "backend,data-processing,epic-2,sprint-2,P0"

gh issue create --title "TASK-020: Build data preprocessing pipeline" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P0 - Critical

### Description
Create data preprocessing pipeline.

### Tasks
- [ ] Clean data (remove duplicates, handle nulls)
- [ ] Parse and normalize dates
- [ ] Standardize SKU format
- [ ] Aggregate data if needed
- [ ] Create preprocessing functions in data_processor.py

### Acceptance Criteria
- Data is cleaned properly
- Preprocessing pipeline is complete
- Functions are reusable" \
  --label "backend,data-processing,epic-2,sprint-2,P0"

gh issue create --title "TASK-021: Store processed data in database" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P0 - Critical

### Description
Save processed data to SQLite database.

### Tasks
- [ ] Insert/update products table
- [ ] Insert sales_data records
- [ ] Handle bulk inserts efficiently
- [ ] Implement transaction management

### Acceptance Criteria
- Data is stored correctly
- Bulk operations are efficient
- Transactions are handled properly" \
  --label "backend,database,epic-2,sprint-2,P0"

gh issue create --title "TASK-022: Create data preview endpoint" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P1 - High

### Description
Implement endpoint to preview uploaded data.

### Tasks
- [ ] Implement GET /api/upload/preview/{file_id}
- [ ] Return first 10-20 rows of processed data
- [ ] Include summary statistics

### Acceptance Criteria
- Preview endpoint works
- Returns formatted data
- Includes statistics" \
  --label "backend,api,epic-2,sprint-2,P1"

gh issue create --title "TASK-023: Create FileUpload component" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P0 - Critical

### Description
Build file upload component for frontend.

### Tasks
- [ ] Build drag-and-drop upload interface
- [ ] Add file selection button
- [ ] Show file name and size
- [ ] Implement in components/Upload/FileUpload.jsx

### Acceptance Criteria
- Component renders correctly
- Drag-and-drop works
- File selection works" \
  --label "frontend,component,epic-2,sprint-2,P0"

gh issue create --title "TASK-024: Add upload progress indicator" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P1 - High

### Description
Show upload progress to user.

### Tasks
- [ ] Show upload progress bar
- [ ] Display upload status (uploading, processing, complete)
- [ ] Handle upload errors

### Acceptance Criteria
- Progress bar shows correctly
- Status updates are clear
- Errors are displayed" \
  --label "frontend,component,epic-2,sprint-2,P1"

gh issue create --title "TASK-025: Create UploadPage" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P0 - Critical

### Description
Create main upload page.

### Tasks
- [ ] Create pages/UploadPage.jsx
- [ ] Integrate FileUpload component
- [ ] Add instructions for users
- [ ] Show upload history

### Acceptance Criteria
- Page renders correctly
- FileUpload is integrated
- User instructions are clear" \
  --label "frontend,page,epic-2,sprint-2,P0"

gh issue create --title "TASK-026: Implement data preview after upload" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P1 - High

### Description
Show preview of uploaded data.

### Tasks
- [ ] Fetch preview data from API
- [ ] Display data in table format
- [ ] Show summary statistics (row count, date range, unique SKUs)

### Acceptance Criteria
- Preview displays correctly
- Table is formatted well
- Statistics are shown" \
  --label "frontend,component,epic-2,sprint-2,P1"

gh issue create --title "TASK-027: Add validation feedback" \
  --body "**Epic:** Data Management
**Sprint:** 2 (Week 2)
**Priority:** P1 - High

### Description
Display validation errors to user.

### Tasks
- [ ] Display validation errors from backend
- [ ] Highlight problematic rows/columns
- [ ] Provide suggestions for fixes

### Acceptance Criteria
- Errors are displayed clearly
- User knows what to fix
- Helpful suggestions provided" \
  --label "frontend,component,epic-2,sprint-2,P1"

echo "✓ Created issues for Epic 1 and Epic 2"
echo ""
echo "Note: This script creates only the first 27 issues (Epic 1-2)."
echo "To create all 130+ issues, you can extend this script or create issues in batches."
echo ""
echo "Next steps:"
echo "1. Install GitHub CLI: brew install gh"
echo "2. Authenticate: gh auth login"
echo "3. Create GitHub repo: gh repo create forecast_aprovizionare --public"
echo "4. Run this script: bash create_github_issues.sh"
