'''
This program teaches how to read a text file.
'''
sample_file_path = '/Users/aarush/Documents/git/training/python/sample.txt'
city_file = open(sample_file_path, 'r')
for line in city_file:
    print(line.strip())

city_file.close()