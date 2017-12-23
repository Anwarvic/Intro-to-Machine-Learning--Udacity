import string

file_object = open('from_chris.txt', 'r')
words = file_object.read()
words = string.replace(words, '.', '_')

new_object = open('nw2.txt', 'w')
new_object.write(words)
