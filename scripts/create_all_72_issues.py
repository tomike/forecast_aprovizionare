#!/usr/bin/env python3
"""
Create all 72 remaining GitHub issues (TASK-058 through TASK-130)
with full descriptions and acceptance criteria from BACKLOG.md
"""

import subprocess
import time

def create_issue(title, body, labels):
    """Create a GitHub issue using gh CLI"""
    try:
        cmd = [
            'gh', 'issue', 'create',
            '--title', title,
            '--body', body,
            '--label', ','.join(labels)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"✓ {title}")
            return True
        else:
            print(f"✗ {title} - Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ {title} - Exception: {e}")
        return False

def main():
    print("=" * 80)
    print("Creating 72 Remaining GitHub Issues (TASK-058 through TASK-130)")
    print("=" * 80)
    print()

    created = 0
    failed = 0

    # Epic 4: Forecasting Engine (Sprint 5) - 14 tasks
    print("\n### EPIC 4: Forecasting Engine (14 tasks) ###\n")

    epic4_issues = [
        ("TASK-058: Create forecaster service", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
Create the main forecaster service that handles prediction generation.

### Tasks
- [ ] Create services/forecaster.py
- [ ] Implement Forecaster class
- [ ] Add model loading logic
- [ ] Handle multiple model types

### Acceptance Criteria
- Forecaster service is created
- Can load and use trained models
- Supports Prophet, LSTM, and XGBoost""", ["backend", "api", "epic-4", "sprint-5", "P0"]),

        ("TASK-059: Implement model loading", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
Implement functionality to load trained models from file system.

### Tasks
- [ ] Load model from file system
- [ ] Load associated metadata
- [ ] Cache loaded models for performance
- [ ] Handle model not found errors

### Acceptance Criteria
- Models load correctly from disk
- Metadata is associated properly
- Caching improves performance
- Error handling is robust""", ["backend", "ml", "epic-4", "sprint-5", "P0"]),

        ("TASK-060: Implement forecast generation", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
Core forecast generation functionality.

### Tasks
- [ ] Accept product_id, model_type, horizon_days
- [ ] Load historical data for product
- [ ] Generate predictions using selected model
- [ ] Create forecast objects

### Acceptance Criteria
- Forecasts are generated accurately
- Works with all three model types
- Handles edge cases properly""", ["backend", "ml", "epic-4", "sprint-5", "P0"]),

        ("TASK-061: Configure forecast horizon", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
Add configurable forecast horizons.

### Tasks
- [ ] Support 7-day forecast
- [ ] Support 30-day forecast
- [ ] Support 90-day forecast
- [ ] Support custom horizon input

### Acceptance Criteria
- All preset horizons work
- Custom horizons are supported
- Validation prevents invalid inputs""", ["backend", "ml", "epic-4", "sprint-5", "P0"]),

        ("TASK-062: Store predictions in database", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
Save generated forecasts to database.

### Tasks
- [ ] Insert forecast records into forecasts table
- [ ] Link to product_id and model_type
- [ ] Store forecast_date and predicted_quantity
- [ ] Handle bulk inserts

### Acceptance Criteria
- Forecasts are stored correctly
- Bulk inserts are efficient
- Relationships are maintained""", ["backend", "database", "epic-4", "sprint-5", "P0"]),

        ("TASK-063: Create forecast endpoint", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
API endpoint to generate forecasts.

### Tasks
- [ ] Implement POST /api/forecast in api/forecast.py
- [ ] Accept request with product_ids, model_type, horizon_days
- [ ] Call forecaster service
- [ ] Return forecast data

### Acceptance Criteria
- Endpoint is documented
- Handles requests correctly
- Returns proper response format""", ["backend", "api", "epic-4", "sprint-5", "P0"]),

        ("TASK-064: Implement forecast retrieval endpoint", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
API endpoint to retrieve saved forecasts.

### Tasks
- [ ] Implement GET /api/forecasts
- [ ] Filter by product_id (query param)
- [ ] Filter by date range (start_date, end_date)
- [ ] Return list of forecasts

### Acceptance Criteria
- Filtering works correctly
- Pagination considered
- Response format is consistent""", ["backend", "api", "epic-4", "sprint-5", "P0"]),

        ("TASK-065: Add product listing endpoint", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
API endpoint to list all products.

### Tasks
- [ ] Implement GET /api/products
- [ ] Return all products with metadata
- [ ] Include SKU, name, category
- [ ] Support pagination (optional for MVP)

### Acceptance Criteria
- All products are listed
- Metadata is complete
- Response is performant""", ["backend", "api", "epic-4", "sprint-5", "P0"]),

        ("TASK-066: Add models listing endpoint", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P1

### Description
API endpoint to list trained models.

### Tasks
- [ ] Implement GET /api/models
- [ ] Return all trained models
- [ ] Include model_type, training_date, metrics
- [ ] Filter by product_id (optional)

### Acceptance Criteria
- Model list is complete
- Metrics are displayed
- Filtering works if implemented""", ["backend", "api", "epic-4", "sprint-5", "P1"]),

        ("TASK-067: Format data for visualization", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P1

### Description
Structure API responses for chart rendering.

### Tasks
- [ ] Structure response for charts
- [ ] Include historical data + forecast
- [ ] Add metadata (model type, accuracy)
- [ ] Return in JSON format

### Acceptance Criteria
- Data format is chart-friendly
- All necessary fields included
- Documentation is clear""", ["backend", "api", "epic-4", "sprint-5", "P1"]),

        ("TASK-068: Test Prophet forecasting end-to-end", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
End-to-end testing of Prophet forecasting.

### Tasks
- [ ] Upload sample data
- [ ] Train Prophet model
- [ ] Generate forecasts
- [ ] Verify results

### Acceptance Criteria
- Complete workflow works
- Results are accurate
- No errors occur""", ["backend", "ml", "testing", "epic-4", "sprint-5", "P0"]),

        ("TASK-069: Test LSTM forecasting end-to-end", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
End-to-end testing of LSTM forecasting.

### Tasks
- [ ] Upload sample data
- [ ] Train LSTM model
- [ ] Generate forecasts
- [ ] Verify results

### Acceptance Criteria
- Complete workflow works
- Results are accurate
- No errors occur""", ["backend", "ml", "testing", "epic-4", "sprint-5", "P0"]),

        ("TASK-070: Test XGBoost forecasting end-to-end", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
End-to-end testing of XGBoost forecasting.

### Tasks
- [ ] Upload sample data
- [ ] Train XGBoost model
- [ ] Generate forecasts
- [ ] Verify results

### Acceptance Criteria
- Complete workflow works
- Results are accurate
- No errors occur""", ["backend", "ml", "testing", "epic-4", "sprint-5", "P0"]),

        ("TASK-071: Test multi-product forecasting", """**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

### Description
Test forecasting for multiple products simultaneously.

### Tasks
- [ ] Upload data for multiple SKUs
- [ ] Train models for all products
- [ ] Generate forecasts for all products
- [ ] Verify correct product association

### Acceptance Criteria
- Multi-product handling works
- Products don't interfere
- Results are correctly linked""", ["backend", "ml", "testing", "epic-4", "sprint-5", "P0"]),
    ]

    for title, body, labels in epic4_issues:
        if create_issue(title, body, labels):
            created += 1
        else:
            failed += 1
        time.sleep(0.7)  # Rate limiting

    print(f"\nEpic 4 complete: {created} issues created\n")

    # Epic 5: Frontend Development (Sprint 6) - 21 tasks
    print("\n### EPIC 5: Frontend Development (21 tasks) ###\n")

    epic5_issues = [
        ("TASK-072: Create ModelTraining component", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Build component for model training interface.

### Tasks
- [ ] Build in components/Training/ModelTraining.jsx
- [ ] Add product selection dropdown/list
- [ ] Add model type selector (Prophet, LSTM, XGBoost)
- [ ] Add 'Start Training' button

### Acceptance Criteria
- Component renders correctly
- All UI elements are functional
- Styling is consistent""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-073: Implement product selection", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Add product selection functionality.

### Tasks
- [ ] Fetch products from GET /api/products
- [ ] Display in selectable list
- [ ] Support multi-select
- [ ] Show product details (SKU, name)

### Acceptance Criteria
- Products load from API
- Selection works smoothly
- Multi-select is intuitive""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-074: Add training trigger", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Implement training initiation logic.

### Tasks
- [ ] Call POST /api/train on button click
- [ ] Pass selected products and model type
- [ ] Receive job ID
- [ ] Start polling for status

### Acceptance Criteria
- Training starts correctly
- Job ID is tracked
- Status polling begins""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-075: Display training status/progress", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Show training progress to user.

### Tasks
- [ ] Poll GET /api/train/status/{job_id}
- [ ] Show progress bar
- [ ] Display current status message
- [ ] Show completion percentage

### Acceptance Criteria
- Progress updates in real-time
- Status messages are clear
- Completion is indicated""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-076: Create TrainingPage", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Create main training page.

### Tasks
- [ ] Create pages/TrainingPage.jsx
- [ ] Integrate ModelTraining component
- [ ] Add training history section
- [ ] Show trained models list

### Acceptance Criteria
- Page layout is complete
- Components are integrated
- Navigation works""", ["frontend", "page", "epic-5", "sprint-6", "P0"]),

        ("TASK-077: Create ForecastChart component", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Build chart component for visualizations.

### Tasks
- [ ] Build in components/Dashboard/ForecastChart.jsx
- [ ] Install Recharts or Chart.js
- [ ] Create line chart for time series
- [ ] Plot historical data + forecast

### Acceptance Criteria
- Charts render correctly
- Library is properly configured
- Data displays accurately""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-078: Implement chart visualization", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Add visualization features to charts.

### Tasks
- [ ] Display date on X-axis
- [ ] Display quantity on Y-axis
- [ ] Differentiate historical vs forecast (colors/line styles)
- [ ] Add legend

### Acceptance Criteria
- Axes are labeled correctly
- Visual distinction is clear
- Legend is helpful""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-079: Add interactivity to charts", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

### Description
Make charts interactive.

### Tasks
- [ ] Add tooltips on hover
- [ ] Support zoom/pan (optional)
- [ ] Click to view details
- [ ] Responsive design

### Acceptance Criteria
- Tooltips show data points
- Interactions are smooth
- Mobile-friendly""", ["frontend", "component", "epic-5", "sprint-6", "P1"]),

        ("TASK-080: Create ResultsTable component", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Build table component for forecast data.

### Tasks
- [ ] Build in components/Dashboard/ResultsTable.jsx
- [ ] Display forecast data in table format
- [ ] Columns: Date, SKU, Predicted Quantity, Model Type
- [ ] Basic styling

### Acceptance Criteria
- Table renders correctly
- All columns are present
- Data is formatted properly""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-081: Add table sorting", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

### Description
Add sorting functionality to table.

### Tasks
- [ ] Sort by date
- [ ] Sort by SKU
- [ ] Sort by quantity
- [ ] Toggle ascending/descending

### Acceptance Criteria
- All columns are sortable
- Sort order toggles
- Performance is good""", ["frontend", "component", "epic-5", "sprint-6", "P1"]),

        ("TASK-082: Add table filtering", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

### Description
Add filtering capabilities to table.

### Tasks
- [ ] Filter by product/SKU
- [ ] Filter by date range
- [ ] Filter by model type
- [ ] Show filter controls

### Acceptance Criteria
- Filters work correctly
- UI is intuitive
- Can combine filters""", ["frontend", "component", "epic-5", "sprint-6", "P1"]),

        ("TASK-083: Implement export to CSV", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

### Description
Add CSV export functionality.

### Tasks
- [ ] Add 'Export' button
- [ ] Convert table data to CSV format
- [ ] Trigger download
- [ ] Include headers

### Acceptance Criteria
- Export works correctly
- CSV format is valid
- All data is included""", ["frontend", "component", "epic-5", "sprint-6", "P1"]),

        ("TASK-084: Create DashboardPage", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Create main dashboard page.

### Tasks
- [ ] Create pages/DashboardPage.jsx
- [ ] Add forecast generation section
- [ ] Integrate ForecastChart component
- [ ] Integrate ResultsTable component

### Acceptance Criteria
- Layout is complete
- Components are integrated
- Page is functional""", ["frontend", "page", "epic-5", "sprint-6", "P0"]),

        ("TASK-085: Add forecast generation controls", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Add controls for generating forecasts.

### Tasks
- [ ] Product selector
- [ ] Model type selector
- [ ] Horizon input (7, 30, 90 days)
- [ ] 'Generate Forecast' button

### Acceptance Criteria
- All controls work
- Validation is present
- UI is user-friendly""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-086: Fetch and display forecast data", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Connect forecast generation to display.

### Tasks
- [ ] Call POST /api/forecast
- [ ] Receive forecast results
- [ ] Update chart with new data
- [ ] Update table with new data

### Acceptance Criteria
- API integration works
- Data updates correctly
- Loading states shown""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-087: Compare actual vs predicted", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

### Description
Add comparison visualization.

### Tasks
- [ ] Overlay historical data on chart
- [ ] Show comparison metrics
- [ ] Highlight differences
- [ ] Add comparison view toggle

### Acceptance Criteria
- Comparison is clear
- Metrics are helpful
- Toggle works""", ["frontend", "component", "epic-5", "sprint-6", "P1"]),

        ("TASK-088: Create Navbar component", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Build navigation bar component.

### Tasks
- [ ] Build in components/common/Navbar.jsx
- [ ] Add navigation links (Upload, Training, Dashboard)
- [ ] Add app title/logo
- [ ] Style with chosen CSS framework

### Acceptance Criteria
- Navbar renders on all pages
- Links work correctly
- Styling is consistent""", ["frontend", "component", "epic-5", "sprint-6", "P0"]),

        ("TASK-089: Create loading spinner component", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

### Description
Create reusable loading indicator.

### Tasks
- [ ] Reusable loading indicator
- [ ] Use during API calls
- [ ] Consistent styling
- [ ] Configurable size/color

### Acceptance Criteria
- Spinner is reusable
- Animations are smooth
- Styling is consistent""", ["frontend", "component", "epic-5", "sprint-6", "P1"]),

        ("TASK-090: Create error message component", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

### Description
Create error display component.

### Tasks
- [ ] Display API errors
- [ ] User-friendly error messages
- [ ] Dismissible alerts
- [ ] Different error levels (warning, error, info)

### Acceptance Criteria
- Errors display clearly
- Messages are helpful
- Component is reusable""", ["frontend", "component", "epic-5", "sprint-6", "P1"]),

        ("TASK-091: Update App.jsx with routes", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

### Description
Configure main app routing.

### Tasks
- [ ] Configure React Router
- [ ] Add routes for all pages
- [ ] Include Navbar on all pages
- [ ] Set default route

### Acceptance Criteria
- All routes work
- Navbar shows on all pages
- Default route loads""", ["frontend", "setup", "epic-5", "sprint-6", "P0"]),

        ("TASK-092: Add responsive design", """**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

### Description
Make application responsive.

### Tasks
- [ ] Make components mobile-friendly
- [ ] Test on different screen sizes
- [ ] Adjust layouts for tablets/phones
- [ ] Use responsive CSS utilities

### Acceptance Criteria
- Works on mobile
- Works on tablet
- Desktop layout optimal""", ["frontend", "component", "epic-5", "sprint-6", "P1"]),
    ]

    for title, body, labels in epic5_issues:
        if create_issue(title, body, labels):
            created += 1
        else:
            failed += 1
        time.sleep(0.7)

    print(f"\nEpic 5 complete: {created} issues created so far\n")

    # Epic 6: Testing & Quality (Sprint 7) - 21 tasks
    print("\n### EPIC 6: Testing & Quality (21 tasks) ###\n")

    epic6_issues = [
        ("TASK-093: Set up pytest", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Set up Python testing infrastructure.

### Tasks
- [ ] Install pytest
- [ ] Create tests/ directory structure
- [ ] Configure pytest.ini
- [ ] Set up test database

### Acceptance Criteria
- pytest is configured
- Test structure is ready
- Test database works""", ["backend", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-094: Write tests for upload endpoint", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Test file upload functionality.

### Tasks
- [ ] Test valid CSV upload
- [ ] Test valid Excel upload
- [ ] Test invalid file format
- [ ] Test missing columns
- [ ] Test validation errors

### Acceptance Criteria
- All upload scenarios tested
- Tests pass
- Edge cases covered""", ["backend", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-095: Write tests for data processing", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Test data processing pipeline.

### Tasks
- [ ] Test CSV parsing
- [ ] Test Excel parsing
- [ ] Test data validation
- [ ] Test preprocessing pipeline
- [ ] Test database insertion

### Acceptance Criteria
- All processing steps tested
- Tests are comprehensive
- Coverage is high""", ["backend", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-096: Write tests for Prophet model", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Test Prophet model implementation.

### Tasks
- [ ] Test model training
- [ ] Test prediction generation
- [ ] Test model serialization
- [ ] Test metrics calculation

### Acceptance Criteria
- Prophet model fully tested
- All functions work correctly
- Edge cases handled""", ["backend", "ml", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-097: Write tests for LSTM model", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Test LSTM model implementation.

### Tasks
- [ ] Test sequence preparation
- [ ] Test model training
- [ ] Test prediction generation
- [ ] Test model serialization

### Acceptance Criteria
- LSTM model fully tested
- All functions work correctly
- Edge cases handled""", ["backend", "ml", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-098: Write tests for XGBoost model", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Test XGBoost model implementation.

### Tasks
- [ ] Test feature engineering
- [ ] Test model training
- [ ] Test prediction generation
- [ ] Test model serialization

### Acceptance Criteria
- XGBoost model fully tested
- All functions work correctly
- Edge cases handled""", ["backend", "ml", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-099: Write tests for forecast endpoint", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Test forecasting API endpoints.

### Tasks
- [ ] Test forecast generation
- [ ] Test forecast retrieval
- [ ] Test filtering
- [ ] Test error handling

### Acceptance Criteria
- All endpoints tested
- Response formats verified
- Error cases covered""", ["backend", "api", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-100: Write database operation tests", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Test database CRUD operations.

### Tasks
- [ ] Test CRUD operations for products
- [ ] Test CRUD operations for sales_data
- [ ] Test CRUD operations for forecasts
- [ ] Test relationships and joins

### Acceptance Criteria
- All database operations tested
- Relationships verified
- Data integrity maintained""", ["backend", "database", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-101: Set up Jest and React Testing Library", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Set up frontend testing infrastructure.

### Tasks
- [ ] Install dependencies
- [ ] Configure Jest
- [ ] Set up test utilities

### Acceptance Criteria
- Jest is configured
- Testing library is ready
- Test utilities work""", ["frontend", "testing", "epic-6", "sprint-7", "P0"]),

        ("TASK-102: Write tests for FileUpload component", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P1

### Description
Test file upload component.

### Tasks
- [ ] Test file selection
- [ ] Test drag-and-drop
- [ ] Test upload trigger
- [ ] Test error display

### Acceptance Criteria
- Component is fully tested
- User interactions work
- Error handling verified""", ["frontend", "testing", "epic-6", "sprint-7", "P1"]),

        ("TASK-103: Write tests for ModelTraining component", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P1

### Description
Test model training component.

### Tasks
- [ ] Test product selection
- [ ] Test model selection
- [ ] Test training trigger
- [ ] Test status updates

### Acceptance Criteria
- Component is fully tested
- All interactions work
- State management verified""", ["frontend", "testing", "epic-6", "sprint-7", "P1"]),

        ("TASK-104: Write tests for ForecastChart component", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P1

### Description
Test forecast chart component.

### Tasks
- [ ] Test chart rendering
- [ ] Test data display
- [ ] Test interactivity

### Acceptance Criteria
- Chart rendering tested
- Data visualization works
- Interactions verified""", ["frontend", "testing", "epic-6", "sprint-7", "P1"]),

        ("TASK-105: Write tests for ResultsTable component", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P1

### Description
Test results table component.

### Tasks
- [ ] Test table rendering
- [ ] Test sorting
- [ ] Test filtering
- [ ] Test export functionality

### Acceptance Criteria
- Table is fully tested
- All features work
- Data handling verified""", ["frontend", "testing", "epic-6", "sprint-7", "P1"]),

        ("TASK-106: Write integration tests", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P2

### Description
Write integration tests (optional for MVP).

### Tasks
- [ ] Test full upload-to-forecast flow
- [ ] Test multi-page navigation
- [ ] Test API integration

### Acceptance Criteria
- Integration tests pass
- Full workflow works
- End-to-end verified""", ["testing", "epic-6", "sprint-7", "P2"]),

        ("TASK-107: Fix bugs discovered during testing", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P0

### Description
Address bugs found during testing.

### Tasks
- [ ] Document bugs
- [ ] Prioritize fixes
- [ ] Implement solutions
- [ ] Verify fixes

### Acceptance Criteria
- All critical bugs fixed
- Tests pass
- No regressions""", ["backend", "frontend", "epic-6", "sprint-7", "P0"]),

        ("TASK-108: Improve error handling (Backend)", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P1

### Description
Enhance backend error handling.

### Tasks
- [ ] Add try-catch blocks
- [ ] Return meaningful error messages
- [ ] Log errors appropriately
- [ ] Handle edge cases

### Acceptance Criteria
- Error handling is robust
- Messages are helpful
- Logging is comprehensive""", ["backend", "epic-6", "sprint-7", "P1"]),

        ("TASK-109: Improve error handling (Frontend)", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P1

### Description
Enhance frontend error handling.

### Tasks
- [ ] Catch API errors
- [ ] Display user-friendly messages
- [ ] Provide recovery options
- [ ] Add retry mechanisms

### Acceptance Criteria
- Errors are caught gracefully
- Users get helpful feedback
- Recovery is possible""", ["frontend", "epic-6", "sprint-7", "P1"]),

        ("TASK-110: Add loading states", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P1

### Description
Add loading indicators throughout app.

### Tasks
- [ ] Show spinners during API calls
- [ ] Disable buttons during processing
- [ ] Indicate background tasks
- [ ] Provide feedback

### Acceptance Criteria
- Loading states are clear
- UX is improved
- Users know when to wait""", ["frontend", "epic-6", "sprint-7", "P1"]),

        ("TASK-111: Optimize model training time", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P2

### Description
Improve model training performance.

### Tasks
- [ ] Profile training performance
- [ ] Optimize data preprocessing
- [ ] Adjust model parameters
- [ ] Use efficient algorithms

### Acceptance Criteria
- Training time reduced
- Performance is acceptable
- Accuracy maintained""", ["backend", "ml", "epic-6", "sprint-7", "P2"]),

        ("TASK-112: Optimize database queries", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P2

### Description
Improve database query performance.

### Tasks
- [ ] Add indexes
- [ ] Optimize joins
- [ ] Use bulk operations
- [ ] Profile query performance

### Acceptance Criteria
- Queries are faster
- Database is efficient
- Performance is monitored""", ["backend", "database", "epic-6", "sprint-7", "P2"]),

        ("TASK-113: Code review and refactoring", """**Epic:** Testing & Quality | **Sprint:** 7 (Week 7) | **Priority:** P1

### Description
Review and refactor codebase.

### Tasks
- [ ] Review all code
- [ ] Refactor duplicated code
- [ ] Improve naming conventions
- [ ] Add code comments

### Acceptance Criteria
- Code is clean
- Duplication removed
- Comments are helpful""", ["backend", "frontend", "epic-6", "sprint-7", "P1"]),
    ]

    for title, body, labels in epic6_issues:
        if create_issue(title, body, labels):
            created += 1
        else:
            failed += 1
        time.sleep(0.7)

    print(f"\nEpic 6 complete: {created} issues created so far\n")

    # Epic 7: Documentation & Deployment (Sprint 8) - 17 tasks
    print("\n### EPIC 7: Documentation & Deployment (17 tasks) ###\n")

    epic7_issues = [
        ("TASK-114: Write API documentation", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Document all API endpoints.

### Tasks
- [ ] Document all endpoints
- [ ] Add request/response examples
- [ ] Include authentication details
- [ ] Describe error codes

### Acceptance Criteria
- All endpoints documented
- Examples are clear
- Documentation is complete""", ["documentation", "epic-7", "sprint-8", "P0"]),

        ("TASK-115: Create user guide", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Write end-user documentation.

### Tasks
- [ ] Write step-by-step instructions
- [ ] Add screenshots
- [ ] Explain each feature
- [ ] Include troubleshooting

### Acceptance Criteria
- User guide is complete
- Instructions are clear
- Screenshots are helpful""", ["documentation", "epic-7", "sprint-8", "P0"]),

        ("TASK-116: Write developer documentation", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P1

### Description
Document codebase for developers.

### Tasks
- [ ] Explain architecture
- [ ] Document data models
- [ ] Add inline code comments
- [ ] Create setup guide

### Acceptance Criteria
- Architecture is documented
- Code is well-commented
- Setup guide works""", ["documentation", "epic-7", "sprint-8", "P1"]),

        ("TASK-117: Create README.md", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Write comprehensive README.

### Tasks
- [ ] Project overview
- [ ] Installation instructions
- [ ] Usage examples
- [ ] Contributing guidelines

### Acceptance Criteria
- README is complete
- Installation works
- Examples are helpful""", ["documentation", "epic-7", "sprint-8", "P0"]),

        ("TASK-118: Add inline code documentation", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P1

### Description
Add docstrings and comments.

### Tasks
- [ ] Add Python docstrings
- [ ] Add JSDoc comments
- [ ] Document complex logic
- [ ] Explain algorithms

### Acceptance Criteria
- All functions documented
- Comments are helpful
- Code is self-explanatory""", ["documentation", "epic-7", "sprint-8", "P1"]),

        ("TASK-119: Create deployment scripts", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Prepare deployment automation.

### Tasks
- [ ] Create deployment scripts
- [ ] Test deployment process
- [ ] Document deployment steps
- [ ] Add rollback procedure

### Acceptance Criteria
- Scripts work correctly
- Deployment is automated
- Rollback is possible""", ["deployment", "epic-7", "sprint-8", "P0"]),

        ("TASK-120: Configure production environment", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Set up production configuration.

### Tasks
- [ ] Set environment variables
- [ ] Configure database
- [ ] Set up logging
- [ ] Configure security settings

### Acceptance Criteria
- Environment is configured
- Security is enabled
- Logging works""", ["deployment", "epic-7", "sprint-8", "P0"]),

        ("TASK-121: Set up monitoring and logging", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P1

### Description
Implement monitoring and logging.

### Tasks
- [ ] Set up application logging
- [ ] Configure error tracking
- [ ] Add performance monitoring
- [ ] Create dashboards

### Acceptance Criteria
- Logging is comprehensive
- Errors are tracked
- Performance is monitored""", ["deployment", "epic-7", "sprint-8", "P1"]),

        ("TASK-122: Deploy to production", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Deploy application to production.

### Tasks
- [ ] Deploy backend
- [ ] Deploy frontend
- [ ] Configure reverse proxy
- [ ] Test production deployment

### Acceptance Criteria
- Application is deployed
- Both services work
- Production is stable""", ["deployment", "epic-7", "sprint-8", "P0"]),

        ("TASK-123: Perform security audit", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Conduct security review.

### Tasks
- [ ] Review authentication
- [ ] Check for vulnerabilities
- [ ] Test input validation
- [ ] Review permissions

### Acceptance Criteria
- Security is reviewed
- Vulnerabilities fixed
- App is secure""", ["testing", "epic-7", "sprint-8", "P0"]),

        ("TASK-124: Perform load testing", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P1

### Description
Test application under load.

### Tasks
- [ ] Create load test scenarios
- [ ] Run load tests
- [ ] Identify bottlenecks
- [ ] Optimize performance

### Acceptance Criteria
- Load tests complete
- Performance is acceptable
- Bottlenecks addressed""", ["testing", "epic-7", "sprint-8", "P1"]),

        ("TASK-125: Create backup strategy", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Implement data backup system.

### Tasks
- [ ] Set up database backups
- [ ] Test restore procedure
- [ ] Document backup process
- [ ] Schedule automated backups

### Acceptance Criteria
- Backups work
- Restore is tested
- Process is automated""", ["deployment", "epic-7", "sprint-8", "P0"]),

        ("TASK-126: Final QA testing", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Conduct final quality assurance.

### Tasks
- [ ] Test all features
- [ ] Verify requirements met
- [ ] Test edge cases
- [ ] Check browser compatibility

### Acceptance Criteria
- All features work
- Requirements satisfied
- No critical bugs""", ["testing", "epic-7", "sprint-8", "P0"]),

        ("TASK-127: User acceptance testing", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Conduct UAT with stakeholders.

### Tasks
- [ ] Prepare test scenarios
- [ ] Conduct UAT sessions
- [ ] Collect feedback
- [ ] Address issues

### Acceptance Criteria
- UAT is complete
- Feedback addressed
- Users are satisfied""", ["testing", "epic-7", "sprint-8", "P0"]),

        ("TASK-128: Create project handover documentation", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P0

### Description
Prepare handover materials.

### Tasks
- [ ] Document system architecture
- [ ] List all credentials
- [ ] Explain maintenance procedures
- [ ] Create support guide

### Acceptance Criteria
- Handover docs complete
- All info included
- Team can maintain system""", ["documentation", "epic-7", "sprint-8", "P0"]),

        ("TASK-129: Prepare demo presentation", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P1

### Description
Create demo for stakeholders.

### Tasks
- [ ] Prepare demo script
- [ ] Create presentation slides
- [ ] Prepare sample data
- [ ] Practice demo

### Acceptance Criteria
- Demo is ready
- Presentation is clear
- Features showcased""", ["documentation", "epic-7", "sprint-8", "P1"]),

        ("TASK-130: Project completion and retrospective", """**Epic:** Documentation & Deployment | **Sprint:** 8 (Week 8) | **Priority:** P1

### Description
Complete project and conduct retrospective.

### Tasks
- [ ] Finalize all deliverables
- [ ] Conduct team retrospective
- [ ] Document lessons learned
- [ ] Archive project materials

### Acceptance Criteria
- Project is complete
- Retrospective done
- Lessons documented""", ["documentation", "epic-7", "sprint-8", "P1"]),
    ]

    for title, body, labels in epic7_issues:
        if create_issue(title, body, labels):
            created += 1
        else:
            failed += 1
        time.sleep(0.7)

    print(f"\nEpic 7 complete!\n")
    print("=" * 80)
    print(f"FINAL SUMMARY: Created {created} issues, {failed} failed")
    print("=" * 80)
    print(f"\nView all issues at: https://github.com/tomike/forecast_aprovizionare/issues")

if __name__ == "__main__":
    main()
