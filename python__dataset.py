# ------------------------------
# 🎓 Student Performance Analysis Project
# Using Pandas
# ------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

# ------------------------------
# 1. How many rows and columns are there in the dataset?
# ------------------------------
print("1️⃣ Dataset Shape:", df.shape)

# ------------------------------
# 2. What are the column names and their data types?
# ------------------------------
print("\n2️⃣ Column Names and Data Types:")
print(df.dtypes)

# ------------------------------
# 3. Are there any missing values in the dataset?
# ------------------------------
print("\n3️⃣ Missing Values:")
print(df.isnull().sum())

# ------------------------------
# 4. What is the average score in each subject?
# ------------------------------
print("\n4️⃣ Average Scores in Each Subject:")
print(df[['math score', 'reading score', 'writing score']].mean())

# ------------------------------
# 5. Which subject has the highest average score overall?
# ------------------------------
avg_scores = df[['math score', 'reading score', 'writing score']].mean()
print("\n5️⃣ Subject with Highest Average Score:")
print(f"{avg_scores.idxmax()} - {avg_scores.max()}")

# ------------------------------
# 6. Find the student with the highest and lowest total score.
# ------------------------------
df['total_score'] = df['math score'] + df['reading score'] + df['writing score']
print("\n6️⃣ Student with Highest Total Score:")
print(df.loc[df['total_score'].idxmax()])
print("\nStudent with Lowest Total Score:")
print(df.loc[df['total_score'].idxmin()])

# ------------------------------
# 7. Compare average scores between male and female students.
# ------------------------------
print("\n7️⃣ Average Scores by Gender:")
print(df.groupby('gender')[['math score', 'reading score', 'writing score']].mean())

# ------------------------------
# 8. Compare average scores based on parental level of education.
# ------------------------------
print("\n8️⃣ Average Scores by Parental Education:")
print(df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean())

# ------------------------------
# 9. How does lunch type affect performance?
# ------------------------------
print("\n9️⃣ Average Scores by Lunch Type:")
print(df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean())

# ------------------------------
# 10. Does completing a test preparation course improve scores?
# ------------------------------
print("\n🔟 Test Preparation Course Effect:")
print(df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean())

# ------------------------------
# 11. Add a new column for average score
# ------------------------------
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
print("\n11️⃣ Added new column 'average_score'")

# ------------------------------
# 12. Correlation between the three subjects
# ------------------------------
print("\n12️⃣ Correlation Between Subjects:")
print(df[['math score', 'reading score', 'writing score']].corr())

# ------------------------------
# 13. Which race/ethnicity group performs best on average?
# ------------------------------
print("\n13️⃣ Average Scores by Race/Ethnicity:")
print(df.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean())

# ------------------------------
# 14. Display the top 10 students based on total score.
# ------------------------------
print("\n14️⃣ Top 10 Students by Total Score:")
print(df.nlargest(10, 'total_score')[['gender', 'race/ethnicity', 'total_score']])

# ------------------------------
# 15. Count how many students scored above 80 in all three subjects.
# ------------------------------
above80 = df[(df['math score'] > 80) & (df['reading score'] > 80) & (df['writing score'] > 80)]
print("\n15️⃣ Students scoring above 80 in all subjects:", len(above80))

# ------------------------------
# OPTIONAL VISUALIZATIONS (BONUS)
# ------------------------------

# Bar chart of average scores
avg_scores.plot(kind='bar', title='Average Scores per Subject', color=['#6A5ACD','#20B2AA','#FFA07A'])
plt.ylabel('Average Score')
plt.show()

# Boxplot of math scores by gender
df.boxplot(column='math score', by='gender', grid=False)
plt.title('Math Scores by Gender')
plt.suptitle('')
plt.show()

# Histogram of total scores
df['total_score'].plot(kind='hist', bins=15, title='Distribution of Total Scores', color='lightblue', edgecolor='black')
plt.xlabel('Total Score')
plt.show()

# Scatter plot between math and reading scores
df.plot.scatter(x='math score', y='reading score', title='Math vs Reading Score', color='purple')
plt.show()

# Pie chart for parental education levels
df['parental level of education'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Parental Education Distribution')
plt.ylabel('')
plt.show()

print("\n✅ Project Completed Successfully!")
