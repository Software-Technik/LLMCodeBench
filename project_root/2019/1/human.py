# Program to multiply two matrices using Python taking User Input
A = []
B = []

# Open the input file
with open('input', 'r') as f:
    lines = f.readlines()

# Read matrix A
index = 0
n = int(lines[index].strip())
index += 1
for i in range(n):
    row = list(map(int, lines[index].strip().split()))
    A.append(row)
    index += 1

# Read matrix B
m = int(lines[index].strip())
index += 1
for i in range(m):
    row = list(map(int, lines[index].strip().split()))
    B.append(row)
    index += 1

# Display A
print("Matrix A:")
for row in A:
    print(" ".join(map(str, row)))

# Display B
print("\nMatrix B:")
for row in B:
    print(" ".join(map(str, row)))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Display the 2D array
print("Display Array In Matrix Form:")
for i in range(n):
   for j in range(n):
      print(B[i][j], end=" ")
   print()                                           
result = [[0,0,0], [0,0,0], [0,0,0]] 
for i in range(len(A)): 
   for j in range(len(B[0])): 
      for k in range(len(B)): 
         result[i][j] += A[i][k] * B[k][j] 
print("The Resultant Sum Matrix Is ::>")
with open('solution', 'w') as f:
    for r in result:
        line = " ".join(map(str, r))
        print(line)          # print to screen
        f.write(line + '\n')  # write to file