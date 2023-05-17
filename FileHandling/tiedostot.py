"""
file = open('myfile.txt', 'w')  # open the file named records.txt in write mode
file.write('hello')  # write the text 'hello' to the file
file.close()  # close the file
file = open(fileName, mode)  # open the file
file.read()  # read all the file
file.readline()  # read the next line
file.write(string)  # write string to the file
file.close()  # close the file
"""

file = open("FileHandling/text.txt", "w")

# write to file from a list
numberlist = [5, 12, 3, 123, 123, 1, 321, 3, 213, 12, 3412, 54]

for i in range(len(numberlist)):
    file.write(str(numberlist[i]) + "\n")
file.close()


# read contents
file = open("FileHandling/text.txt", "r")
output = file.read()
print(output)
# read each line into a list
lines = output.split("\n")
print(lines)
file.close()