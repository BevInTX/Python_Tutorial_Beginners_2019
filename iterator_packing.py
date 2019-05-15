coordinates = (1, 2, 3)
x, y, z = coordinates
print(x, y, z)

alist = list(range(3, 6))            # normal call with separate arguments
print(alist)
args = [3, 6]
print(list(range(*args)))           # call with arguments unpacked from a list

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
d = {"state": "bleedin' demised", "action": "VOOM", "voltage": "four million"}
parrot(**d)

released = {
    "iphone" : 2007,
    "iphone 3G" : 2008,
    "iphone 3GS" : 2009,
    "iphone 4" : 2010,
    "iphone 4S" : 2011,
    "iphone 5" : 2012
}
print(released)

#the syntax is: mydict[key] = "value"
released["iphone 5S"] = 2013
print (released)

my_dict = {'a' : 'one', 'b' : 'two'}
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

for key,val in released.items():
    print (f"{key} => {val}")