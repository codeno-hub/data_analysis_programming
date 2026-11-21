
# NUMPY FOR DATA SCIENCE
import numpy as np
import time
import matplotlib.pyplot as plt

#Dunder Method- Special Methods python has made for you
#*init*,*str*, *len*,*name*
print("NumPy Version:", np.__version__)

# PART 1: WHY NUMPY?
# Python vs NumPy Speed Comparison
print("\nPART 1: SPEED COMPARISON")
# Create two Python lists
a = list(range(1000000))
b = list(range(1000000))

# Python multiplication
start = time.time()
result = []
for i in range(len(a)):
  result.append(a[i] * b[i])
python_time = time.time() - start

# NumPy multiplication
x = np.arange(1000000)
y = np.arange(1000000)
start = time.time()
numpy_result = x * y
numpy_time = time.time() - start
numpy_time

print("Python Time:", round(python_time, 4), "seconds")
print("NumPy Time:", round(numpy_time, 4), "seconds")

if numpy_time > 0:
    print("Speed Ratio:", round(python_time / numpy_time, 2), "times")

# PART 2: ARRAY CREATION
print("\nPART 2: ARRAY CREATION")
# Simple array
a = np.array([10, 20, 30, 40, 50])
print("Simple Array:", a)

# Two-dimensional array
b = np.array([[10, 20, 30],
              [40, 50, 60]])
print("2D Array:\n", b)

# Array of zeros
print("Zeros:\n", np.zeros((3, 3)))

# Array of Ones
print("Zeros:\n", np.ones((3, 3)))

# Array of ones
print("Ones:\n", np.ones((2, 4)))

# Array with a fixed value
print("Full Array:\n", np.full((2, 2), 8))

# Range of numbers
print("Arange:", np.arange(1, 10, 1))

print("Arange:", np.arange(1, 10, 2))

print("Arange:", np.arange(1, 10, 3))

# Check shape, size and data type
print("Shape:", b.shape)

print("Total Elements:", b.size)

print("Data Type:", b.dtype)

#Quiz
# Question 1
print("Q1:", np.zeros((3, 3)).dtype)

# Question 2
print("Q2:", np.arange(1, 10, 2))

# Question 3
print("Q3:", np.ones((5, 2)).shape)

# Question 4
print("Q4:\n", np.full((2, 2), 7))

# Question 5
a = np.array([[1, 2],
              [3, 4]])

print("Q5:", a[0, 1])

# PART 4: IPL CRICKET DATA ANALYSIS
# 4 Matches x 5 Batting Positions
print("\nPART 4: IPL CRICKET ANALYSIS")
# IPL match scores
scores = np.array([
    [45, 33, 67, 12,  8],
    [82, 10, 54, 30,  5],
    [23, 71, 45, 60, 14],
    [95, 40, 28, 17, 50]
])
print("Complete Scorecard:\n", scores)

# Shape and data type
print("Shape:", scores.shape)

print("Data Type:", scores.dtype)

# Task 1: Extract first two matches
match_12 = scores[:2, :]
print("\nFirst Two Matches:\n", match_12)

# Task 2: Extract top three batting positions
top_order = scores[:, :3]
print("\nTop Order Scores:\n", top_order)

# Task 3: Extract second match
print("\nSecond Match:", scores[1, :])

# Task 4: Extract third batting position
print("\nThird Batting Position:", scores[:, 2])

# Task 5: Extract one particular score
print("\nMatch 1, Player 3:", scores[0, 2])

# Task 6: Fancy indexing-Lets you pick specific(rows and column) pair instead of picking a full row
#or column
row_idx = np.array([0, 1, 2, 3])
col_idx = np.array([2, 0, 1, 4])

star_scores = scores[row_idx, col_idx]
star_scores

print("\nStar Player Scores:", star_scores)

# Task 7: Add 10 bonus runs
scores[row_idx, col_idx] += 10
print("\nUpdated Scorecard:\n", scores)

# Task 8: Total runs in each match
print("\nTotal Runs Per Match:", np.sum(scores, axis=1))

#library .py file with functions in it
#step1: create a folder
#step2:



# Commented out IPython magic to ensure Python compatibility.
# %%writefile mytools.py
# 
# #mytools.py- this is my library
# def add(a,b):
#   return a+b
# 
# def greet(name):
#   return f"Hello {name}, welcome!"

import mytools
print(mytools.add(5,3))
print(mytools.greet("Mithun"))