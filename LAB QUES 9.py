import numpy as np

student_scores = np.array([
    [80, 85, 78, 92],  
    [88, 79, 84, 90],  
    [90, 92, 88, 85],  
    [85, 87, 90, 80]   
])

average_scores = student_scores.mean(axis=0)
print("Average scores for each subject:", average_scores)

subjects = ['Math', 'Science', 'English', 'History']
highest_avg_score_index = average_scores.argmax()
subject_with_highest_avg_score = subjects[highest_avg_score_index]

print(f"The subject with the highest average score is {subject_with_highest_avg_score} with an average score of {average_scores[highest_avg_score_index]:.2f}.")
