import numpy as np
a = np.array([[1, 2, 3, 4, 4], [3, 3, 4, 5, 6]])

# Displaying the array
print('Array:\n', a)
file = open("file1.txt", "w+")

# Saving the array in a text file
content = str(a)
file.write(content)
file.close()

# Displaying the contents of the text file
file = open("file1.txt", "r")
content = file.read()

print("\nContent in file1.txt:\n", content)
file.close()
