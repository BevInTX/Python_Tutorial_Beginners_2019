try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age must not be zero')
except ValueError:
    print("Invalid value")


import sys    
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError as err:
        print('cannot open', arg, err)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
        
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)