import numpy as np

# Example student_scores array (replace with your actual data)
student_scores = np.array([
    [80, 75, 90, 85],  # Student 1: Math, Science, English, History
    [90, 82, 78, 85],  # Student 2
    [70, 75, 80, 92],  # Student 3
    [88, 85, 75, 80]   # Student 4
])

# Calculate average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Identify the subject with the highest average score
highest_average_subject_index = np.argmax(average_scores)

# Print the results
subjects = ['Math', 'Science', 'English', 'History']

print("Average scores:")
for i, subject in enumerate(subjects):
    print(f"{subject}: {average_scores[i]}")

highest_subject = subjects[highest_average_subject_index]
print(f"\nThe subject with the highest average score is: {highest_subject}")
