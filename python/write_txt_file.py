'''
In this program we will learn how to write in a text file.
'''
file_path = "flowers.txt"
flower_file = open(file_path, "a")
flower_file.write("lotus\n")

flower_file.close()