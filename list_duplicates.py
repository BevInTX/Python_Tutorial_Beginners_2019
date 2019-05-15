alist = ['a', 'b', 'c', 'd', 'a', 'c']

# Don't care about order and don't want to allocate another list
for item in alist:
    
    item_count = alist.count(item)
    while item_count > 1:
        item_count -= 1
        alist.remove(item)  
print(f'in place duplicate removal: {alist}')

alist = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
# care about order and don't mind allocating another list
for item in alist:
    
    if item not in uniques:
        uniques.append(item)
        
print(f'duplicate removal via separate list (old one intact``): {uniques}')