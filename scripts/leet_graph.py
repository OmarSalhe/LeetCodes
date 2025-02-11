import os
import matplotlib.pyplot as plt

base_dir = "./"
difficulties = ["Hard", "Medium", "Easy"]
counts = []

# Counting solutions 
for difficulty in difficulties:
    dir_path = os.path.join(base_dir, difficulty)
    if os.path.exists(dir_path):
        counts.append(len([f for f in os.listdir(dir_path)])) # counts number of subdirectories in each directory 
    else:
        counts.append(0)


# Creating graph
plt.figure(figsize=(6, 4))
plt.bar(difficulties, counts, color=['red', 'orange', 'blue'])
plt.xlabel('Difficulty')
plt.ylabel('Number of Solutions')
plt.title('Leetcode Solutions')

plt.savefig("solutions.png")