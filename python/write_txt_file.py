'''
In this program we will learn how to write in a text file.
'''

flower_file = open("flowers.txt", "a")
flower_file.write("lotus\n")

flower_file.close()