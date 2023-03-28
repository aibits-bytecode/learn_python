cities = ["colombo", "toronto", "newyork"]
countries = ["SL", "Canada", "USA"]

z = zip(cities,countries)
for s in z:
    print(s)

dict1 = {city:country for city, country in zip(cities,countries)}

print(dict1)
