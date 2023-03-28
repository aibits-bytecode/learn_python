books = {}

books["tom"] = {
    "name": "tom",
    "address": "2 red street ny",
    "phone": 9834323
}

books["kamal"] = {
    "name": "kamal",
    "address": "1 red street ny",
    "phone": 9832323
}

# write to json file
import json
# this dump the dictionary into string
s = json.dumps(books)
# in here the data will write as a json object so we can interact with other languages
with open("/Users/chandimajayamina/EagleAI/Core Python/collections/data/address.txt", "w") as f:
    f.write(s)
    f.close()
# read through json file
file = open("/Users/chandimajayamina/EagleAI/Core Python/collections/data/address.txt", "r")
s = file.read()
print(s)
#import  json
phoneBook = json.loads(s)
print(type(phoneBook))