'''
    This is something like key value pairs
'''

scores = {"amal": 60, "bimal": 75}

# retrieve the value from key
print(scores["amal"])
# add elements to dictionary

scores["kamal"] = 44
print(scores)

# in here we can use for loops in dictionaries
for k,v in scores.items():
    print(k,v)

# clear out the dictionary
scores.clear()
print(scores)