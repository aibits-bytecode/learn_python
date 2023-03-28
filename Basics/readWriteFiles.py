# write something to file this will override previous content
file = open("/Users/chandimajayamina/EagleAI/Core Python/collections/data/readwrite.txt", "w")
file.write("I love python")
file.close()

# w mode is override
# a means append to the file
# r+ for read and write files
# w+ this is for read and write if file does not exit it will create new one, if exist it will overide

### in here we dont want to close the file explicitly it will close automatically
with open("/Users/chandimajayamina/EagleAI/Core Python/collections/data/readwrite.txt", "w") as f:
    print(f)

