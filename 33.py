import numpy as np
daily_sales = np.array([100, 120, 90, 110, 130, 95, 105, 115, 125, 100, 110, 120, 130, 95, 105])
mean_sales = np.mean(daily_sales)
variance_sales = np.var(daily_sales)
print("Variance of Daily Sales:", variance_sales)
import numpy as np
study_hours = np.array([2, 3, 1, 4, 5, 2, 3, 4, 5, 1])
exam_scores = np.array([65, 70, 60, 75, 80, 65, 70, 75, 80, 60])
covariance_study_exam = np.cov(study_hours, exam_scores)[0, 1]
print("Covariance between Study Hours and Exam Scores:", covariance_study_exam)

