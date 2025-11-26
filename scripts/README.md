# Scripts Directory

This directory contains utility scripts for creating and managing GitHub issues for the Supply Chain Forecasting System project.

## Scripts Overview

### Issue Creation Scripts

#### `fix_epic3_issues.py` ✅ (USED - Successfully updated 30 issues)
**Purpose:** Updates all Epic 3 issues (TASK-028 through TASK-057) with proper titles, descriptions, tasks, and acceptance criteria.

**Status:** Successfully executed - all 30 Epic 3 issues have been updated.

**Usage:**
```bash
python3 scripts/fix_epic3_issues.py
```

#### `create_all_72_issues.py` ✅ (USED - Successfully created 72 issues)
**Purpose:** Creates all 72 remaining Epic 4-7 issues (TASK-058 through TASK-130) with full descriptions and acceptance criteria.

**Status:** Successfully executed - all 72 issues created (with 5 deployment issues manually fixed).

**Usage:**
```bash
python3 scripts/create_all_72_issues.py
```

### Legacy/Archived Scripts

The following scripts were used during the initial issue creation process but are now superseded:

#### `create_all_github_issues.py`
Early script showing the pattern for Epic 1 issue creation (15 issues with full details).

#### `create_issues.py`
Template script demonstrating issue creation structure.

#### `create_all_issues.sh`
Bash script that creates Epic 1 issues only.

#### `create_github_issues.sh`
Alternative bash implementation for issue creation.

#### `create_remaining_issues.sh`
Script designed to create Epic 2-7 issues (condensed format).

#### `create_all_detailed_issues.sh`
Partial implementation for creating Epic 4-5 issues with detailed descriptions.

#### `create_epic4_7_detailed.sh`
Alternative approach to creating Epic 4-7 issues.

## Current Project Status

### GitHub Issues Summary
- **Total Issues:** 130 issues created
- **Epic 1:** 15 issues ✅ (Full descriptions, Sprint 1)
- **Epic 2:** 12 issues ✅ (Full descriptions, Sprint 2)
- **Epic 3:** 30 issues ✅ (Full descriptions, Sprint 3-4) - Fixed by `fix_epic3_issues.py`
- **Epic 4:** 14 issues ✅ (Full descriptions, Sprint 5)
- **Epic 5:** 21 issues ✅ (Full descriptions, Sprint 6)
- **Epic 6:** 21 issues ✅ (Full descriptions, Sprint 7)
- **Epic 7:** 17 issues ✅ (Full descriptions, Sprint 8)

### Repository
- **GitHub Repo:** https://github.com/tomike/forecast_aprovizionare
- **All Issues:** https://github.com/tomike/forecast_aprovizionare/issues

## How the Scripts Work

### Python Scripts

Both main Python scripts (`fix_epic3_issues.py` and `create_all_72_issues.py`) use the GitHub CLI (`gh`) to interact with the repository:

```python
gh issue create --title "..." --body "..." --label "..."
gh issue edit ISSUE_NUMBER --title "..." --body "..."
```

**Features:**
- Rate limiting (0.5-0.7 second delays between API calls)
- Error handling and retry logic
- Progress tracking
- Detailed issue bodies with:
  - Epic and Sprint information
  - Descriptions
  - Task lists (checkboxes)
  - Acceptance criteria
  - Proper labels

### Shell Scripts

Bash scripts provide an alternative approach using direct `gh` commands:

```bash
gh issue create \
  --title "TASK-XXX: Task Title" \
  --body "Description with tasks and criteria" \
  --label "label1,label2,label3"
```

## Labels Used

All issues are tagged with appropriate labels:

- **Epic labels:** `epic-1`, `epic-2`, ..., `epic-7`
- **Sprint labels:** `sprint-1`, `sprint-2`, ..., `sprint-8`
- **Priority:** `P0` (Critical), `P1` (High), `P2` (Medium)
- **Type:** `backend`, `frontend`, `database`, `ml`, `api`, `component`, `page`, `testing`, `documentation`, `deployment`

## Future Usage

These scripts can serve as templates for:
1. Creating similar issue structures for other projects
2. Bulk updating existing issues
3. Automating GitHub project management tasks

## References

- **BACKLOG.md:** Complete task list with all 130+ tasks
- **README.md:** Full project documentation
- **FINAL_STATUS.md:** Final status of issue creation process
