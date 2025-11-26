#!/bin/bash

# Create ALL remaining GitHub issues with FULL descriptions
# Epic 4-7 with complete task details

echo "Creating remaining GitHub issues with full descriptions..."
echo "Epic 4: Forecasting Engine (14 tasks)"
echo "Epic 5: Frontend Development (21 tasks)"
echo "Epic 6: Testing & Quality (21 tasks)"
echo "Epic 7: Documentation & Deployment (17 tasks)"
echo ""

CREATED=0
FAILED=0

create_issue() {
    if gh issue create "$@" 2>/dev/null; then
        ((CREATED++))
        echo "  ✓ Created (total: $CREATED)"
    else
        ((FAILED++))
        echo "  ✗ Failed"
    fi
    sleep 0.5
}

# EPIC 4: Forecasting Engine (Sprint 5)
echo "Creating Epic 4: Forecasting Engine..."

create_issue --title "TASK-058: Create forecaster service" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Supports Prophet, LSTM, and XGBoost" \
--label "backend,api,epic-4,sprint-5,P0"

create_issue --title "TASK-059: Implement model loading" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Error handling is robust" \
--label "backend,ml,epic-4,sprint-5,P0"

create_issue --title "TASK-060: Implement forecast generation" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Handles edge cases properly" \
--label "backend,ml,epic-4,sprint-5,P0"

create_issue --title "TASK-061: Configure forecast horizon" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Validation prevents invalid inputs" \
--label "backend,ml,epic-4,sprint-5,P0"

create_issue --title "TASK-062: Store predictions in database" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Relationships are maintained" \
--label "backend,database,epic-4,sprint-5,P0"

create_issue --title "TASK-063: Create forecast endpoint" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Returns proper response format" \
--label "backend,api,epic-4,sprint-5,P0"

create_issue --title "TASK-064: Implement forecast retrieval endpoint" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Response format is consistent" \
--label "backend,api,epic-4,sprint-5,P0"

create_issue --title "TASK-065: Add product listing endpoint" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Response is performant" \
--label "backend,api,epic-4,sprint-5,P0"

create_issue --title "TASK-066: Add models listing endpoint" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P1

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
- Filtering works if implemented" \
--label "backend,api,epic-4,sprint-5,P1"

create_issue --title "TASK-067: Format data for visualization" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P1

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
- Documentation is clear" \
--label "backend,api,epic-4,sprint-5,P1"

create_issue --title "TASK-068: Test Prophet forecasting end-to-end" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- No errors occur" \
--label "backend,ml,testing,epic-4,sprint-5,P0"

create_issue --title "TASK-069: Test LSTM forecasting end-to-end" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- No errors occur" \
--label "backend,ml,testing,epic-4,sprint-5,P0"

create_issue --title "TASK-070: Test XGBoost forecasting end-to-end" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- No errors occur" \
--label "backend,ml,testing,epic-4,sprint-5,P0"

create_issue --title "TASK-071: Test multi-product forecasting" \
--body "**Epic:** Forecasting Engine | **Sprint:** 5 (Week 5) | **Priority:** P0

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
- Results are correctly linked" \
--label "backend,ml,testing,epic-4,sprint-5,P0"

echo "Epic 4 complete. Created: $CREATED"
echo ""

# EPIC 5: Frontend Development (Sprint 6)
echo "Creating Epic 5: Frontend Development..."

create_issue --title "TASK-072: Create ModelTraining component" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Styling is consistent" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-073: Implement product selection" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Multi-select is intuitive" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-074: Add training trigger" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Status polling begins" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-075: Display training status/progress" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Completion is indicated" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-076: Create TrainingPage" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Navigation works" \
--label "frontend,page,epic-5,sprint-6,P0"

create_issue --title "TASK-077: Create ForecastChart component" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Data displays accurately" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-078: Implement chart visualization" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Legend is helpful" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-079: Add interactivity to charts" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

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
- Mobile-friendly" \
--label "frontend,component,epic-5,sprint-6,P1"

create_issue --title "TASK-080: Create ResultsTable component" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Data is formatted properly" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-081: Add table sorting" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

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
- Performance is good" \
--label "frontend,component,epic-5,sprint-6,P1"

create_issue --title "TASK-082: Add table filtering" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

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
- Can combine filters" \
--label "frontend,component,epic-5,sprint-6,P1"

create_issue --title "TASK-083: Implement export to CSV" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

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
- All data is included" \
--label "frontend,component,epic-5,sprint-6,P1"

create_issue --title "TASK-084: Create DashboardPage" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Page is functional" \
--label "frontend,page,epic-5,sprint-6,P0"

create_issue --title "TASK-085: Add forecast generation controls" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- UI is user-friendly" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-086: Fetch and display forecast data" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Loading states shown" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-087: Compare actual vs predicted" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

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
- Toggle works" \
--label "frontend,component,epic-5,sprint-6,P1"

create_issue --title "TASK-088: Create Navbar component" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Styling is consistent" \
--label "frontend,component,epic-5,sprint-6,P0"

create_issue --title "TASK-089: Create loading spinner component" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

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
- Styling is consistent" \
--label "frontend,component,epic-5,sprint-6,P1"

create_issue --title "TASK-090: Create error message component" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

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
- Component is reusable" \
--label "frontend,component,epic-5,sprint-6,P1"

create_issue --title "TASK-091: Update App.jsx with routes" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P0

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
- Default route loads" \
--label "frontend,setup,epic-5,sprint-6,P0"

create_issue --title "TASK-092: Add responsive design" \
--body "**Epic:** Frontend Development | **Sprint:** 6 (Week 6) | **Priority:** P1

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
- Desktop layout optimal" \
--label "frontend,component,epic-5,sprint-6,P1"

echo "Epic 5 complete. Created: $CREATED"
echo ""

# Continue with Epic 6 and 7 in next message due to length...
echo "Continuing with Epic 6 and 7..."

