# ---------------------------------------
# Student Data Visualization Project
# ---------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------------
# Create folder to save graphs
# ---------------------------------------
os.makedirs("images", exist_ok=True)

# ---------------------------------------
# Load Dataset
# ---------------------------------------
try:
    df = pd.read_csv("data/students.csv")
except FileNotFoundError:
    # Default dataset
    data = {
        "Name": ["Aman", "Riya", "Rahul", "Simran", "Vikas", "Neha", "Arjun", "Pooja"],
        "Math": [78, 85, 62, 90, 70, 88, 95, 60],
        "Science": [82, 79, 65, 88, 72, 91, 89, 58],
        "English": [75, 88, 70, 92, 68, 85, 90, 65],
        "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"]
    }
    df = pd.DataFrame(data)

# ---------------------------------------
# Data Processing
# ---------------------------------------
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\n===== STUDENT DATA =====")
print(df)

# ---------------------------------------
# 1. Average Marks Visualization
# ---------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/average_marks.png")
plt.show()

# ---------------------------------------
# 2. Subject-wise Comparison
# ---------------------------------------
plt.figure(figsize=(10, 6))
df.set_index("Name")[["Math", "Science", "English"]].plot(kind="bar")
plt.title("Subject-wise Marks Comparison")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/subject_comparison.png")
plt.show()

# ---------------------------------------
# 3. Gender-wise Performance
# ---------------------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(x="Gender", y="Average", data=df)
plt.title("Gender-wise Performance")
plt.tight_layout()
plt.savefig("images/gender_performance.png")
plt.show()

# ---------------------------------------
# 4. Score Distribution
# ---------------------------------------
plt.figure(figsize=(7, 5))
sns.histplot(df["Average"], bins=5, kde=True)
plt.title("Score Distribution")
plt.tight_layout()
plt.savefig("images/score_distribution.png")
plt.show()

# ---------------------------------------
# Completion Message
# ---------------------------------------
print("\n✔ All graphs generated and saved successfully in 'images' folder")