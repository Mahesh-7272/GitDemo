#read the file and store all the line in list

with open('Test.txt','r') as reader:
    content=reader.readlines()
    reversed(content)
    with open('Test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)
