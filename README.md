# Designing-A-Synthetic-Data-Generation-For-Cognitive-Performance-Analysis
Synthetic Cognitive Performance Dataset Generation, Statistical Analysis, and Interactive Streamlit Dashboard

This project provides a synthetic dataset and simulation framework for modeling cognitive performance under varying study conditions. The dataset is generated using principles from cognitive psychology and includes factors such as session length, break duration, task difficulty, and time of day.

The dataset contains 21,600 observations across 108 simulated scenarios (3 session lengths × 3 break durations × 3 difficulty levels × 4 time-of-day conditions, with 200 sessions per scenario). Each record includes computed measures of fatigue, recovery index, performance score, and error count.

The simulation models fatigue as a function of session length and task difficulty, while recovery is modeled logarithmically based on break duration. Performance is derived from the combined effects of fatigue, recovery, and circadian influences. Error counts are generated using a Poisson distribution.

The project includes: • A fully generated synthetic dataset (CSV) • A complete Jupyter Notebook for data generation and analysis • Statistical validation (KS test, ANOVA, Tukey HSD, Cohen’s d) • Predictive modeling using Linear Regression and Random Forest • An interactive Streamlit dashboard for visualization and exploration.

All components are included to ensure full reproducibility. The dataset is entirely synthetic and does not contain any real human data. This work is suitable for research, teaching, and experimentation in cognitive modeling, data science, and machine learning.
