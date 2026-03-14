# Online Learning Engagement Analysis

A portfolio-ready **data analyst project** built from a student engagement dataset. The goal is to explore learner behavior, identify patterns linked to performance and dropout, and present insights in a format that is easy to review on GitHub.

## Project Objective

Online learning platforms depend on consistent learner engagement, session activity, and attendance to improve completion rates. This project analyzes student-level data to answer questions such as:

- What does engagement look like across the student base?
- Which factors appear most associated with dropout?
- How do engagement and performance move together?
- Which dimensions could be monitored in a dashboard?

## Dataset Overview

- **Rows:** 50,000
- **Columns:** 18
- **Target of interest:** `dropout`
- **Main fields:** demographics, device usage, internet quality, learning activity, quiz performance, attendance, engagement, and final grade

### Column List

`student_id`, `age`, `gender`, `country`, `device_type`, `internet_speed_mbps`, `study_hours_weekly`, `login_frequency_weekly`, `avg_session_duration_min`, `video_watch_time_min`, `assignments_submitted`, `forum_posts`, `quiz_attempts`, `avg_quiz_score`, `attendance_rate`, `engagement_score`, `final_grade`, `dropout`

## Tools Used

- Python
- pandas
- matplotlib
- Jupyter Notebook
- SQL
- Git / GitHub

## Repository Structure

```text
online-learning-engagement-analyst-project/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── online_learning_engagement_dataset.csv
├── notebooks/
│   └── online_learning_engagement_analysis.ipynb
├── scripts/
│   ├── data_prep.py
│   └── generate_visuals.py
├── sql/
│   └── analysis_queries.sql
└── visuals/
    ├── correlation_heatmap.png
    ├── dropout_by_attendance_quintile.png
    ├── dropout_rate_by_country.png
    ├── engagement_score_distribution.png
    └── engagement_vs_final_grade.png
```

## Analysis Workflow

1. Load and inspect the dataset
2. Check shape, data types, and missing values
3. Review descriptive statistics
4. Analyze dropout and performance behavior
5. Build visuals for stakeholder communication
6. Translate analysis questions into SQL-style queries

## Key Findings

- The dataset contains **no missing values**, which makes it straightforward to analyze.
- The overall dropout rate is **32.41%**.
- `attendance_rate` is the variable with the strongest relationship to dropout in this dataset, with a correlation of **-0.809**.
- `engagement_score` and `final_grade` show a **modest positive relationship** of **0.050**.
- Country-level dropout rates are fairly close together, suggesting behavior differences are more likely driven by activity variables than geography.

## Dropout Rate by Country

| Country | Dropout Rate |
|---|---|
| USA | 33.23% |
| India | 32.93% |
| Canada | 32.37% |
| UK | 32.13% |
| Germany | 31.90% |
| Australia | 31.90% |

## Recommended Business Actions

- Monitor **attendance rate** as an early warning indicator for churn risk.
- Build a weekly learner health dashboard using attendance, logins, study hours, and quiz activity.
- Segment intervention campaigns toward students showing declining attendance patterns.
- Track how engagement features align with final grade over time to improve retention programs.

## Sample Visuals

### Engagement Score Distribution
![Engagement Score Distribution](visuals/engagement_score_distribution.png)

### Dropout by Attendance Quintile
![Dropout by Attendance Quintile](visuals/dropout_by_attendance_quintile.png)

### Engagement vs Final Grade
![Engagement vs Final Grade](visuals/engagement_vs_final_grade.png)

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/online-learning-engagement-analyst-project.git
cd online-learning-engagement-analyst-project
```

### 2. Create a virtual environment
```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac / Linux**
```bash
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate visuals
```bash
python scripts/generate_visuals.py
```

### 5. Open the notebook
```bash
jupyter notebook notebooks/online_learning_engagement_analysis.ipynb
```

## Suggested GitHub Description

**Portfolio project analyzing student engagement and dropout patterns in online learning data using Python, SQL, and data visualization.**

## Suggested Topics / Tags

`data-analysis`, `python`, `pandas`, `matplotlib`, `jupyter-notebook`, `sql`, `eda`, `portfolio-project`

## Next Steps

- Turn the analysis into a Power BI or Tableau dashboard
- Add cohort-style retention tracking
- Build a simple KPI layer for weekly performance monitoring
- Add stakeholder slides summarizing findings

## License

This project is for portfolio and educational use.
