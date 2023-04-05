import sys

while True:
    try:
        file_name = sys.argv[1]
        file = open(file_name, "r")
        break
    except IndexError:
        print("Please enter a file name.")
        continue
    except FileNotFoundError:
        print("The file name you entered is incorrect. Please enter a valid file name.")
        continue

content = file.read()
print(content)
file.close()
