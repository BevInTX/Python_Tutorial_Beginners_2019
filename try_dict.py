
released = {
    "iphone": 2007,
    "iphone 3G": 2008,
    "iphone 3GS": 2009,
    "iphone 4": 2010,
    "iphone 4S": 2011,
    "iphone 5": 2012
}
print(released)

# the syntax is: mydict[key] = "value"
released["iphone 5S"] = 2013
print (released)

my_dict = {'a': 'one', 'b': 'two'}
print ('a' in my_dict)
print('c' in my_dict)
print('two' in my_dict)

for item in released:
    if "iphone 5" in released:
        print ("Key found")
        break
    else:
        print ("No keys found")

print (released.get("iphone 3G", "none"))


def put_dashes(n):
    print("-" * n)


put_dashes(10)
print("iPhone releases so far:")
put_dashes(10)
for release in released:
    print(release)

for key, val in released.items():
    print (f"{key} => {val}")

customer = {
    "name": "John Smith",
    "age": 30,
    "age": 40,
    "is_verified": True
}
for key, val in customer.items():
    print(f"{key}: {val}")
