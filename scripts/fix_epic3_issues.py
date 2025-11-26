#!/usr/bin/env python3
"""
Script to fix all Epic 3 issues (TASK-028 through TASK-057)
Updates titles, descriptions, tasks, and acceptance criteria
"""

import subprocess
import time
import sys

def run_gh_command(args):
    """Run gh command and return result"""
    try:
        result = subprocess.run(
            ['gh'] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def update_issue(issue_number, title, body):
    """Update an existing GitHub issue"""
    print(f"Updating TASK-{issue_number:03d}: {title}")

    result = run_gh_command([
        'issue', 'edit', str(issue_number),
        '--title', f"TASK-{issue_number:03d}: {title}",
        '--body', body
    ])

    if result is not None:
        print(f"  ✓ Updated successfully")
        return True
    else:
        print(f"  ✗ Failed to update")
        return False

def main():
    print("=" * 80)
    print("Fixing Epic 3: ML Model Development Issues")
    print("Updating TASK-028 through TASK-057 (30 tasks)")
    print("=" * 80)
    print()

    updated = 0
    failed = 0

    # Epic 3 issues with proper details from BACKLOG.md
    # Note: Issue numbers start from issue #30 for TASK-028

    # Calculate actual GitHub issue number
    # TASK-001 = Issue #2, so TASK-028 = Issue #29
    base_issue = 29  # GitHub issue number for TASK-028

    epic3_tasks = [
        # Data Preprocessing (TASK-028 to TASK-031)
        {
            "task_num": 28,
            "title": "Load and explore historical sales data",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Load historical sales data from database and perform exploratory data analysis.

### Tasks
- [ ] Query sales data from database
- [ ] Load into pandas DataFrame
- [ ] Explore data shape, types, missing values
- [ ] Generate summary statistics

### Acceptance Criteria
- Data is loaded successfully
- Basic statistics are available
- Data quality is understood""",
            "labels": ["backend", "ml", "data-processing", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 29,
            "title": "Handle missing values",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Implement missing value handling strategies for sales data.

### Tasks
- [ ] Identify missing values
- [ ] Decide strategy (imputation vs removal)
- [ ] Implement forward-fill or interpolation for dates
- [ ] Document decisions

### Acceptance Criteria
- Missing values are handled appropriately
- Data completeness is improved
- Strategy is documented""",
            "labels": ["backend", "ml", "data-processing", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 30,
            "title": "Create time series features",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Engineer time-based features for model training.

### Tasks
- [ ] Extract day of week, month, year
- [ ] Create lag features (previous 7 days, 30 days)
- [ ] Calculate rolling averages
- [ ] Add seasonal indicators

### Acceptance Criteria
- Time features are created
- Lag features are calculated
- Rolling statistics are added""",
            "labels": ["backend", "ml", "feature-engineering", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 31,
            "title": "Split data into train/validation/test sets",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Split data chronologically for proper time series validation.

### Tasks
- [ ] Use chronological split (not random)
- [ ] Create train (70%), validation (15%), test (15%)
- [ ] Ensure no data leakage
- [ ] Save splits for reproducibility

### Acceptance Criteria
- Data is split chronologically
- No overlap between sets
- Splits are reproducible""",
            "labels": ["backend", "ml", "data-processing", "epic-3", "sprint-3", "P0"]
        },

        # Prophet Model Implementation (TASK-032 to TASK-036)
        {
            "task_num": 32,
            "title": "Create Prophet model class",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Create Prophet model class for time series forecasting.

### Tasks
- [ ] Create ml_models/prophet_model.py
- [ ] Implement ProphetForecaster class
- [ ] Add initialization method
- [ ] Set up basic configuration

### Acceptance Criteria
- Prophet model class is created
- Initialization works correctly
- Configuration is set up properly""",
            "labels": ["backend", "ml", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 33,
            "title": "Implement Prophet training method",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Implement training functionality for Prophet model.

### Tasks
- [ ] Accept training data (dates, values)
- [ ] Format data for Prophet (ds, y columns)
- [ ] Configure Prophet parameters (seasonality, holidays)
- [ ] Train model and return fitted instance

### Acceptance Criteria
- Training method works
- Data formatting is correct
- Model trains successfully""",
            "labels": ["backend", "ml", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 34,
            "title": "Implement Prophet prediction method",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Implement prediction functionality for Prophet model.

### Tasks
- [ ] Create future dataframe
- [ ] Generate predictions
- [ ] Extract yhat (predicted values)
- [ ] Return predictions with dates

### Acceptance Criteria
- Predictions are generated
- Future dates are created correctly
- Output format is correct""",
            "labels": ["backend", "ml", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 35,
            "title": "Add model save/load functionality for Prophet",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Implement model persistence for Prophet.

### Tasks
- [ ] Save trained model to disk (pickle or joblib)
- [ ] Load model from disk
- [ ] Store in models/ directory
- [ ] Handle file paths correctly

### Acceptance Criteria
- Models can be saved
- Models can be loaded
- File handling is robust""",
            "labels": ["backend", "ml", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 36,
            "title": "Test Prophet model on sample data",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Validate Prophet implementation with sample data.

### Tasks
- [ ] Use small sample dataset
- [ ] Train Prophet model
- [ ] Generate predictions
- [ ] Verify results look reasonable

### Acceptance Criteria
- Model trains without errors
- Predictions are generated
- Results pass sanity checks""",
            "labels": ["backend", "ml", "testing", "epic-3", "sprint-3", "P0"]
        },

        # Model Training Service (TASK-037 to TASK-041)
        {
            "task_num": 37,
            "title": "Create ML training service",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Create centralized service for model training.

### Tasks
- [ ] Create services/ml_trainer.py
- [ ] Implement ModelTrainer class
- [ ] Add methods for data loading, training, evaluation
- [ ] Handle model selection

### Acceptance Criteria
- Training service is created
- Class structure is clear
- Ready for model integration""",
            "labels": ["backend", "ml", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 38,
            "title": "Implement model evaluation metrics",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
Implement metrics for evaluating forecast quality.

### Tasks
- [ ] Calculate MAE (Mean Absolute Error)
- [ ] Calculate RMSE (Root Mean Squared Error)
- [ ] Calculate MAPE (Mean Absolute Percentage Error)
- [ ] Return metrics dictionary

### Acceptance Criteria
- All metrics are calculated correctly
- Metrics are returned in standard format
- Edge cases are handled""",
            "labels": ["backend", "ml", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 39,
            "title": "Create model training endpoint",
            "body": """**Epic:** ML Model Development | **Sprint:** 3 (Week 3) | **Priority:** P0

### Description
API endpoint to trigger model training.

### Tasks
- [ ] Implement POST /api/train in api/train.py
- [ ] Accept product_ids and model_type in request
- [ ] Call training service
- [ ] Return training status and job ID

### Acceptance Criteria
- Endpoint is functional
- Request validation works
- Training is triggered correctly""",
            "labels": ["backend", "api", "epic-3", "sprint-3", "P0"]
        },
        {
            "task_num": 40,
            "title": "Implement training status tracking",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Track and report training job status.

### Tasks
- [ ] Store training job status in memory or database
- [ ] Implement GET /api/train/status/{job_id}
- [ ] Return status (pending, running, completed, failed)
- [ ] Include progress percentage if possible

### Acceptance Criteria
- Status tracking works
- Endpoint returns current status
- Progress is reported""",
            "labels": ["backend", "api", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 41,
            "title": "Store trained models and metadata",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Persist trained models and their metadata.

### Tasks
- [ ] Save model files to models/ directory
- [ ] Store metadata in model_metadata table
- [ ] Include training_date, metrics, product_id, model_type
- [ ] Link models to products

### Acceptance Criteria
- Models are saved to disk
- Metadata is stored in database
- Relationships are maintained""",
            "labels": ["backend", "ml", "database", "epic-3", "sprint-4", "P0"]
        },

        # LSTM Model Implementation (TASK-042 to TASK-047)
        {
            "task_num": 42,
            "title": "Create LSTM model class",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Create LSTM neural network model for time series.

### Tasks
- [ ] Create ml_models/lstm_model.py
- [ ] Implement LSTMForecaster class
- [ ] Use TensorFlow/Keras
- [ ] Define LSTM architecture

### Acceptance Criteria
- LSTM class is created
- Architecture is defined
- TensorFlow integration works""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 43,
            "title": "Prepare sequences for LSTM",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Transform time series data into LSTM input sequences.

### Tasks
- [ ] Create sliding window sequences
- [ ] Define lookback period (e.g., 30 days)
- [ ] Reshape data to (samples, timesteps, features)
- [ ] Normalize/scale data

### Acceptance Criteria
- Sequences are created correctly
- Shape matches LSTM requirements
- Data is properly scaled""",
            "labels": ["backend", "ml", "data-processing", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 44,
            "title": "Implement LSTM training method",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Implement LSTM model training.

### Tasks
- [ ] Build LSTM layers
- [ ] Compile model (optimizer, loss)
- [ ] Train on sequence data
- [ ] Use validation set for early stopping

### Acceptance Criteria
- Model trains successfully
- Validation is performed
- Training converges""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 45,
            "title": "Implement LSTM prediction method",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Implement LSTM prediction functionality.

### Tasks
- [ ] Accept input sequence
- [ ] Generate predictions
- [ ] Inverse transform (denormalize)
- [ ] Return predictions with dates

### Acceptance Criteria
- Predictions are generated
- Denormalization works correctly
- Output format matches requirements""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 46,
            "title": "Add model save/load functionality for LSTM",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Implement LSTM model persistence.

### Tasks
- [ ] Save model architecture and weights (.h5 or SavedModel)
- [ ] Save scaler parameters
- [ ] Load model and scaler
- [ ] Store in models/ directory

### Acceptance Criteria
- Models can be saved
- Models can be loaded
- Scaler is persisted""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 47,
            "title": "Test LSTM model on sample data",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Validate LSTM implementation.

### Tasks
- [ ] Use sample dataset
- [ ] Train LSTM model
- [ ] Generate predictions
- [ ] Verify results

### Acceptance Criteria
- Model trains without errors
- Predictions are reasonable
- Performance is acceptable""",
            "labels": ["backend", "ml", "testing", "epic-3", "sprint-4", "P0"]
        },

        # XGBoost Model Implementation (TASK-048 to TASK-053)
        {
            "task_num": 48,
            "title": "Create XGBoost model class",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Create XGBoost model for time series forecasting.

### Tasks
- [ ] Create ml_models/xgboost_model.py
- [ ] Implement XGBoostForecaster class
- [ ] Import xgboost library
- [ ] Set up basic configuration

### Acceptance Criteria
- XGBoost class is created
- Library is imported correctly
- Configuration is set up""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 49,
            "title": "Prepare features for XGBoost",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Create features for XGBoost training.

### Tasks
- [ ] Use time series features from TASK-030
- [ ] Create lag features
- [ ] Add rolling statistics
- [ ] Format as tabular data (X, y)

### Acceptance Criteria
- Features are created
- Data format is correct for XGBoost
- No data leakage""",
            "labels": ["backend", "ml", "feature-engineering", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 50,
            "title": "Implement XGBoost training method",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Implement XGBoost model training.

### Tasks
- [ ] Configure XGBoost parameters (n_estimators, max_depth, learning_rate)
- [ ] Train on feature matrix
- [ ] Use validation set for early stopping
- [ ] Return trained model

### Acceptance Criteria
- Model trains successfully
- Parameters are tuned
- Early stopping works""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 51,
            "title": "Implement XGBoost prediction method",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Implement XGBoost prediction functionality.

### Tasks
- [ ] Accept feature matrix
- [ ] Generate predictions
- [ ] Handle multi-step forecasting
- [ ] Return predictions with dates

### Acceptance Criteria
- Predictions are generated
- Multi-step forecasting works
- Output format is correct""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 52,
            "title": "Add model save/load functionality for XGBoost",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Implement XGBoost model persistence.

### Tasks
- [ ] Save model to disk (.json or .pkl)
- [ ] Load model from disk
- [ ] Store in models/ directory
- [ ] Handle file paths

### Acceptance Criteria
- Models can be saved
- Models can be loaded
- File handling is robust""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 53,
            "title": "Test XGBoost model on sample data",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Validate XGBoost implementation.

### Tasks
- [ ] Use sample dataset
- [ ] Train XGBoost model
- [ ] Generate predictions
- [ ] Verify results

### Acceptance Criteria
- Model trains without errors
- Predictions are reasonable
- Performance is acceptable""",
            "labels": ["backend", "ml", "testing", "epic-3", "sprint-4", "P0"]
        },

        # Model Integration (TASK-054 to TASK-057)
        {
            "task_num": 54,
            "title": "Integrate LSTM into training service",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Add LSTM to the model training service.

### Tasks
- [ ] Add LSTM option to model selection
- [ ] Call LSTM training in ml_trainer.py
- [ ] Handle LSTM-specific parameters
- [ ] Test integration

### Acceptance Criteria
- LSTM can be selected
- Training works through service
- Parameters are handled correctly""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 55,
            "title": "Integrate XGBoost into training service",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Add XGBoost to the model training service.

### Tasks
- [ ] Add XGBoost option to model selection
- [ ] Call XGBoost training in ml_trainer.py
- [ ] Handle XGBoost-specific parameters
- [ ] Test integration

### Acceptance Criteria
- XGBoost can be selected
- Training works through service
- Parameters are handled correctly""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 56,
            "title": "Create unified model interface",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Define common interface for all models.

### Tasks
- [ ] Define common interface (train, predict, save, load)
- [ ] Ensure all models implement the interface
- [ ] Simplify model switching
- [ ] Document interface

### Acceptance Criteria
- Interface is defined
- All models conform
- Model switching is simplified""",
            "labels": ["backend", "ml", "epic-3", "sprint-4", "P0"]
        },
        {
            "task_num": 57,
            "title": "Store performance metrics for all models",
            "body": """**Epic:** ML Model Development | **Sprint:** 4 (Week 4) | **Priority:** P0

### Description
Calculate and store metrics for model comparison.

### Tasks
- [ ] Calculate metrics for LSTM
- [ ] Calculate metrics for XGBoost
- [ ] Store in model_metadata table
- [ ] Compare model performance

### Acceptance Criteria
- Metrics are calculated for all models
- Metrics are stored in database
- Model comparison is possible""",
            "labels": ["backend", "ml", "database", "epic-3", "sprint-4", "P0"]
        },
    ]

    # Update each issue
    for task in epic3_tasks:
        issue_number = base_issue + (task["task_num"] - 28)
        if update_issue(issue_number, task["title"], task["body"]):
            updated += 1
        else:
            failed += 1
        time.sleep(0.7)  # Rate limiting

    print()
    print("=" * 80)
    print(f"Summary: Updated {updated} issues, {failed} failed")
    print("=" * 80)

    if updated == 30:
        print()
        print("✅ SUCCESS! All Epic 3 issues have been updated with proper:")
        print("   - Descriptive titles")
        print("   - Full descriptions")
        print("   - Task lists")
        print("   - Acceptance criteria")
        print()
        print("View updated issues at:")
        print("https://github.com/tomike/forecast_aprovizionare/issues?q=is%3Aissue+label%3Aepic-3")

if __name__ == "__main__":
    main()
