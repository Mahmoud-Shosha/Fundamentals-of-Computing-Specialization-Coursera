"""
Learning file handling with python
"""


with open('example.txt', mode='w', encoding='utf-8') as file:
    file.write('This is the first line \n')
    file.write('You must use newline character to make new lines \n\n')


print('__________Using read method__________')
with open('example.txt', mode='r', encoding='utf-8') as file:
    print(file.read(5))
    print(file.read(3))
    print(file.read())
    print(file.read()) # further reading returns empty sting
    print(file.tell())
    file.seek(5)
    print(file.read())


print('__________Using loops__________') # efficient and fast
with open('example.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        print(line) # new lines in 'print' function and in line itself
    file.seek(0)
    for line in file:
        print(line, end='')


print('__________Using readline method__________')
with open('example.txt', mode='r', encoding='utf-8') as file:
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')


print('__________Using readline method__________')
with open('example.txt', mode='r', encoding='utf-8') as file:
    print(file.readlines())
    print(file.readlines())
    file.seek(10)
    print(file.readlines())
