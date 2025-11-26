# Supply Chain Forecasting System

## Project Overview
This document contains the planning and requirements for the Supply Chain Forecasting System.

---

## Requirements Gathering

### 1. Supply Chain Type
**Question:** What type of supply chain are you forecasting for?

**Options:**
- A) Retail/E-commerce inventory (forecasting product demand for stores or online sales)
- B) Manufacturing raw materials (forecasting material needs for production)
- C) Distribution/logistics (forecasting transportation and warehousing needs)
- D) Multi-tier supply chain (end-to-end forecasting across suppliers, manufacturers, distributors, and retailers)
- E) Other (custom description)

**Answer:** A) Retail/E-commerce inventory (forecasting product demand for stores or online sales)

---

### 2. Forecasting Methods
**Question:** What forecasting methods do you want to implement?

**Options:**
- A) Time Series Statistical Methods (ARIMA, Exponential Smoothing, Seasonal decomposition)
- B) Machine Learning Models (Prophet, LSTM, XGBoost/Random Forest, Linear Regression)
- C) Hybrid Approach (Combination of statistical and ML methods, Ensemble models)
- D) All of the above (Multiple methods with performance comparison)
- E) Start simple, expand later (Basic statistical methods first, add ML later)

**Answer:** B) Machine Learning Models (Prophet, LSTM, XGBoost/Random Forest, Linear Regression)

---

### 3. Key Features/Inputs
**Question:** What are the key features/inputs for forecasting?

**Options:**
- A) Basic historical data only (Historical sales/demand, Product SKUs, Timestamps)
- B) Enhanced with temporal features (+ Seasonality, Trends, Holiday flags)
- C) External factors included (+ Weather, Promotions, Marketing campaigns, Competitor pricing)
- D) Comprehensive supply chain data (+ Lead times, Supplier reliability, Stock levels, Reorder points)
- E) Custom selection

**Answer:** A) Basic historical data only (Historical sales/demand, Product SKUs, Timestamps)
**Note:** Start with basic features, add additional requirements in future iterations

---

### 4. Technology Stack
**Question:** What's your preferred technology stack?

**Options:**
- A) Python-based (FastAPI/Flask, scikit-learn/TensorFlow/PyTorch/Prophet, PostgreSQL, React/Vue optional)
- B) Full JavaScript/TypeScript (Node.js, TensorFlow.js, PostgreSQL/MongoDB, React/Vue)
- C) Python Backend + JavaScript Frontend (Python FastAPI/Django, React/Vue/Angular, Python ML libraries, PostgreSQL)
- D) Microservices Architecture (Python ML service, Node.js API gateway, React, PostgreSQL + Redis)
- E) Custom stack

**Answer:** C) Python Backend + JavaScript Frontend
**Details:**
- Backend: Python (FastAPI or Flask)
- Frontend: React
- ML Framework: Python ML libraries (scikit-learn, TensorFlow, Prophet, etc.)
- Database: SQLite (for development/small scale)

---

### 5. Core Functionalities
**Question:** What are the core functionalities you need?

**Options:**
- A) Minimal MVP (Data upload CSV/Excel, Train ML model, Generate forecasts, View results)
- B) Standard Features (+ Multiple model comparison, Performance metrics, Visualization dashboard, Export results)
- C) Advanced Features (+ Real-time ingestion, Automated retraining, Alerts, Confidence intervals, What-if analysis)
- D) Enterprise Features (+ Multi-user auth, API endpoints, Scheduled processing, Model versioning, Audit logs)
- E) Custom selection

**Answer:** A) Minimal MVP (Data upload CSV/Excel, Train ML model, Generate forecasts, View results)
**Note:** Start with MVP, expand with additional features in future iterations

---

### 6. Scale and Deployment
**Question:** What are your scale and deployment requirements?

**Options:**
- A) Local Development Only (Small dataset < 10K records, Few SKUs < 100, Local machine)
- B) Small Production (10K-100K records, 100-1,000 SKUs, VPS/small cloud instance)
- C) Medium Scale (100K-1M records, 1,000-10,000 SKUs, Cloud deployment with optimization)
- D) Enterprise Scale (> 1M records, > 10,000 SKUs, High availability, Scalable infrastructure)
- E) Not sure yet / Flexible

**Answer:** A) Local Development Only (Small dataset < 10K records, Few SKUs < 100, Local machine)
**Note:** Starting with local development, can scale up later as needed

---

## System Architecture

### High-Level Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (React)                        │
│  - File Upload Component                                     │
│  - Forecast Dashboard                                        │
│  - Results Visualization (Charts/Tables)                     │
└───────────────────────┬─────────────────────────────────────┘
                        │ REST API
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                Backend (Python FastAPI)                      │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  API Layer                                          │    │
│  │  - /upload (CSV/Excel file handling)                │    │
│  │  - /train (Model training endpoint)                 │    │
│  │  - /forecast (Generate predictions)                 │    │
│  │  - /results (Retrieve forecast data)                │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  ML Service Layer                                   │    │
│  │  - Data preprocessing                               │    │
│  │  - Feature engineering                              │    │
│  │  - Model training (Prophet, LSTM, XGBoost)          │    │
│  │  - Prediction generation                            │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Data Layer                                         │    │
│  │  - SQLite database operations                       │    │
│  │  - File storage management                          │    │
│  └─────────────────────────────────────────────────────┘    │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                  Database (SQLite)                           │
│  - Sales/Demand history                                      │
│  - Product/SKU information                                   │
│  - Trained models metadata                                   │
│  - Forecast results                                          │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack Details

**Backend:**
- Framework: FastAPI (async, fast, auto API docs)
- Python Version: 3.10+
- ML Libraries:
  - Prophet (Facebook's time series forecasting)
  - TensorFlow/Keras (for LSTM models)
  - XGBoost (gradient boosting)
  - scikit-learn (preprocessing, metrics)
  - pandas (data manipulation)
  - numpy (numerical operations)

**Frontend:**
- React 18+
- Axios (API calls)
- Recharts or Chart.js (visualization)
- Material-UI or Tailwind CSS (styling)
- React Query (data fetching/caching)

**Database:**
- SQLite (lightweight, file-based, no server needed)
- SQLAlchemy (ORM for Python)

**Development Tools:**
- Poetry or pip for Python dependencies
- npm/yarn for JavaScript dependencies
- pytest for Python testing
- Jest/React Testing Library for frontend testing

---

## Data Model

### Database Schema

**products table:**
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(255),
    category VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**sales_data table:**
```sql
CREATE TABLE sales_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    date DATE NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

**forecasts table:**
```sql
CREATE TABLE forecasts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    model_type VARCHAR(50),
    forecast_date DATE NOT NULL,
    predicted_quantity DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

**model_metadata table:**
```sql
CREATE TABLE model_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_type VARCHAR(50),
    model_path VARCHAR(255),
    training_date TIMESTAMP,
    accuracy_metrics JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Implementation Plan

### Phase 1: Project Setup & Infrastructure
1. **Backend Setup**
   - Initialize Python project with FastAPI
   - Set up project structure
   - Configure SQLite database
   - Create database models with SQLAlchemy
   - Set up CORS for frontend communication

2. **Frontend Setup**
   - Initialize React project (Vite or Create React App)
   - Set up project structure
   - Configure API client (Axios)
   - Set up routing (React Router)
   - Configure styling framework

3. **Development Environment**
   - Create requirements.txt / pyproject.toml
   - Create package.json
   - Set up .gitignore
   - Create environment configuration files

### Phase 2: Data Management
1. **File Upload Feature**
   - Backend endpoint to receive CSV/Excel files
   - File validation and parsing
   - Data cleaning and preprocessing
   - Store data in SQLite database
   - Frontend upload component with drag-drop

2. **Data Validation**
   - Validate required columns (SKU, date, quantity)
   - Check data types and formats
   - Handle missing values
   - Detect and report anomalies

### Phase 3: ML Model Development
1. **Data Preprocessing Pipeline**
   - Time series data preparation
   - Feature extraction from dates
   - Data normalization/scaling
   - Train-test split

2. **Model Implementation**
   - **Prophet Model:**
     - Basic time series forecasting
     - Handle seasonality automatically
   - **LSTM Model:**
     - Sequence preparation
     - Neural network architecture
     - Training pipeline
   - **XGBoost Model:**
     - Feature engineering
     - Tree-based forecasting
     - Hyperparameter tuning

3. **Model Training Service**
   - API endpoint for training
   - Background task processing
   - Model serialization and storage
   - Training metrics calculation

### Phase 4: Forecasting Engine
1. **Prediction Service**
   - Load trained models
   - Generate forecasts for selected products
   - Forecast horizon configuration (7, 30, 90 days)
   - Store predictions in database

2. **Results API**
   - Retrieve forecast results
   - Filter by product, date range
   - Format data for visualization

### Phase 5: Frontend Development
1. **Upload Page**
   - File upload interface
   - Upload progress indicator
   - Data preview after upload
   - Validation feedback

2. **Training Page**
   - Select products for training
   - Choose model type
   - Start training process
   - Display training status/progress

3. **Dashboard Page**
   - Visualize historical data
   - Display forecast results
   - Interactive charts (line charts, bar charts)
   - Compare actual vs predicted
   - Basic filtering options

4. **Results Table**
   - Tabular view of forecasts
   - Export to CSV
   - Sorting and filtering

### Phase 6: Testing & Refinement
1. **Backend Testing**
   - Unit tests for API endpoints
   - Test ML pipelines
   - Database operations testing

2. **Frontend Testing**
   - Component testing
   - Integration testing
   - E2E testing (optional for MVP)

3. **Performance Optimization**
   - Optimize model training time
   - Add loading states
   - Error handling improvements

---

## Development Roadmap

### Sprint 1 (Week 1): Project Setup
- [ ] Set up Python FastAPI backend project
- [ ] Set up React frontend project
- [ ] Configure SQLite database
- [ ] Create database schema and models
- [ ] Set up basic API structure
- [ ] Configure CORS and environment variables

### Sprint 2 (Week 2): Data Upload & Storage
- [ ] Implement file upload endpoint (CSV/Excel)
- [ ] Create data validation logic
- [ ] Build data preprocessing pipeline
- [ ] Store processed data in database
- [ ] Create frontend upload component
- [ ] Add file preview functionality

### Sprint 3 (Week 3): ML Models - Part 1
- [ ] Implement data preprocessing for time series
- [ ] Build Prophet model implementation
- [ ] Create model training endpoint
- [ ] Add model serialization
- [ ] Test Prophet forecasting

### Sprint 4 (Week 4): ML Models - Part 2
- [ ] Implement LSTM model
- [ ] Implement XGBoost model
- [ ] Add model selection logic
- [ ] Create model performance metrics
- [ ] Store model metadata

### Sprint 5 (Week 5): Forecasting Service
- [ ] Build prediction generation service
- [ ] Create forecast API endpoint
- [ ] Store forecasts in database
- [ ] Add forecast retrieval endpoints
- [ ] Test forecasting pipeline end-to-end

### Sprint 6 (Week 6): Frontend Dashboard
- [ ] Build training page UI
- [ ] Implement forecast dashboard
- [ ] Add data visualization (charts)
- [ ] Create results table view
- [ ] Connect all components to backend APIs

### Sprint 7 (Week 7): Testing & Polish
- [ ] Write backend unit tests
- [ ] Write frontend component tests
- [ ] Fix bugs and issues
- [ ] Improve error handling
- [ ] Add loading states and feedback
- [ ] Optimize performance

### Sprint 8 (Week 8): Documentation & Deployment
- [ ] Write API documentation
- [ ] Create user guide
- [ ] Add code comments
- [ ] Set up local deployment instructions
- [ ] Final testing and validation
- [ ] MVP Release

---

## Technical Specifications

### API Endpoints

**POST /api/upload**
- Upload CSV/Excel file with sales data
- Request: multipart/form-data
- Response: Upload status, data preview

**POST /api/train**
- Train ML model for specified products
- Request: `{ "product_ids": [1,2,3], "model_type": "prophet" }`
- Response: Training job ID, status

**GET /api/train/status/{job_id}**
- Check training status
- Response: Status, metrics, completion percentage

**POST /api/forecast**
- Generate forecasts
- Request: `{ "product_ids": [1,2,3], "model_type": "prophet", "horizon_days": 30 }`
- Response: Forecast data

**GET /api/forecasts**
- Retrieve forecast results
- Query params: product_id, start_date, end_date
- Response: List of forecasts

**GET /api/products**
- List all products
- Response: Product list with metadata

**GET /api/models**
- List trained models
- Response: Model metadata and performance metrics

### Input Data Format (CSV/Excel)

Required columns:
- `date`: Date in YYYY-MM-DD format
- `sku`: Product SKU identifier
- `quantity`: Sales/demand quantity (numeric)

Optional columns:
- `product_name`: Product name
- `category`: Product category

Example:
```csv
date,sku,quantity,product_name,category
2024-01-01,PROD001,150,Widget A,Electronics
2024-01-02,PROD001,145,Widget A,Electronics
2024-01-01,PROD002,200,Widget B,Home
```

### Model Output Format

Forecast results include:
```json
{
  "product_id": 1,
  "sku": "PROD001",
  "model_type": "prophet",
  "forecasts": [
    {
      "date": "2024-02-01",
      "predicted_quantity": 155.5
    },
    {
      "date": "2024-02-02",
      "predicted_quantity": 158.2
    }
  ],
  "metrics": {
    "mae": 12.5,
    "rmse": 15.8,
    "mape": 8.5
  }
}
```

---

## Project Structure

```
forecast_aprovizionare/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app entry point
│   │   ├── config.py               # Configuration settings
│   │   ├── database.py             # Database connection
│   │   ├── models/                 # SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   ├── product.py
│   │   │   ├── sales.py
│   │   │   └── forecast.py
│   │   ├── schemas/                # Pydantic schemas
│   │   │   ├── __init__.py
│   │   │   ├── product.py
│   │   │   └── forecast.py
│   │   ├── api/                    # API routes
│   │   │   ├── __init__.py
│   │   │   ├── upload.py
│   │   │   ├── train.py
│   │   │   └── forecast.py
│   │   ├── services/               # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── data_processor.py
│   │   │   ├── ml_trainer.py
│   │   │   └── forecaster.py
│   │   └── ml_models/              # ML implementations
│   │       ├── __init__.py
│   │       ├── prophet_model.py
│   │       ├── lstm_model.py
│   │       └── xgboost_model.py
│   ├── tests/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Upload/
│   │   │   │   └── FileUpload.jsx
│   │   │   ├── Training/
│   │   │   │   └── ModelTraining.jsx
│   │   │   ├── Dashboard/
│   │   │   │   ├── ForecastChart.jsx
│   │   │   │   └── ResultsTable.jsx
│   │   │   └── common/
│   │   │       └── Navbar.jsx
│   │   ├── services/
│   │   │   └── api.js              # API client
│   │   ├── pages/
│   │   │   ├── UploadPage.jsx
│   │   │   ├── TrainingPage.jsx
│   │   │   └── DashboardPage.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── .env
│
├── data/                           # SQLite database & uploads
│   ├── database.db
│   └── uploads/
├── models/                         # Saved ML models
├── README.md
└── .gitignore
```

---

## Getting Started (To be implemented)

### Prerequisites
- Python 3.10+
- Node.js 16+
- npm or yarn

### Installation Steps

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### Access
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## Future Enhancements

### Phase 2 Features (Post-MVP)
- Model comparison dashboard
- Performance metrics visualization
- Confidence intervals for predictions
- Multiple model ensemble
- Automated model selection

### Phase 3 Features
- Additional input features (seasonality, holidays)
- Real-time data ingestion
- Automated retraining schedules
- Alert system for anomalies
- What-if scenario analysis

### Phase 4 Features
- User authentication
- Multi-tenancy support
- API for external integrations
- Advanced visualization options
- Export to multiple formats (PDF, Excel)

---

## Notes
- This is an MVP focused on core functionality
- Designed for local development and small-scale use
- Architecture supports future scalability
- All components are modular for easy expansion
