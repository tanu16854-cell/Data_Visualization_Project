# -------------------------------
# Student Data Visualization Project
# -------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# Create folders if not exist
# -------------------------------
if not os.path.exists("images"):
    os.makedirs("images")

# -------------------------------
# Load Dataset (CSV or Default Data)
# -------------------------------
try:
    df = pd.read_csv("data/students.csv")
except:
    data = {
        "Name": ["Aman", "Riya", "Rahul", "Simran", "Vikas", "Neha", "Arjun", "Pooja"],
        "Math": [78, 85, 62, 90, 70, 88, 95, 60],
        "Science": [82, 79, 65, 88, 72, 91, 89, 58],
        "English": [75, 88, 70, 92, 68, 85, 90, 65],
        "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"]
    }
    df = pd.DataFrame(data)

# -------------------------------
# Data Processing
# -------------------------------
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\n===== STUDENT DATA =====")
print(df)

# -------------------------------
# 1. Average Marks Visualization
# -------------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/avg_marks.png")
plt.show()

# -------------------------------
# 2. Subject-wise Comparison
# -------------------------------
df.set_index("Name")[["Math", "Science", "English"]].plot(
    kind="bar", figsize=(10,6)
)
plt.title("Subject-wise Marks Comparison")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/subject_comparison.png")
plt.show()

# -------------------------------
# 3. Gender-wise Performance
# -------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(x="Gender", y="Average", data=df)
plt.title("Gender-wise Performance")
plt.savefig("images/gender_boxplot.png")
plt.show()

# -------------------------------
# 4. Score Distribution
# -------------------------------
plt.figure(figsize=(7,5))
sns.histplot(df["Average"], bins=5, kde=True, color="green")
plt.title("Score Distribution")
plt.savefig("images/distribution.png")
plt.show()

print("\n✔ All graphs saved in 'images' folder")