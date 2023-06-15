'''
This program teaches how to read a text file.
'''

city_file = open('/Users/aarush/Documents/git/training/python/sample.txt', 'r')
for line in city_file:
    print(line.strip())

city_file.close()