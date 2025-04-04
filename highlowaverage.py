#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

f = open("numbers.txt", "r")
print(f.read())

for _ in range("numbers.txt"):
    sum = 0
    count = 0
    average = 0
    highest = 0
    lowest = 0

    count = len(set("numbers.txt"))

print(f"Sum of the list:", sum)
print(f"Number of numbers in the file is: ", len("numbers.txt"))

f.close()