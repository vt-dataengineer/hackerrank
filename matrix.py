#
# 3 5
# 13 4 8 14 1
# 9 6 3 7 21
# 5 12 17 9 3
#
#
# 13 9 5
# 4 6 12
# 8 3 17
# 14 7 9
# 1 21 3
# A basic code for matrix input from user
import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")
ll = []
# User input of entries in a
# single line separated by space
# entries = list(map(int, input().split()))
for x in range(R):
    a = []
    for y in range(C):
        a.append(map(int,input().split()))
        print(a)
ll.append(a)
# For printing the matrix
# matrix = np.array(entries).reshape(R, C)
# print(matrix)
print(ll)
