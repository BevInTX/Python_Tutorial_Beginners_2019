# Variety of utilities

def find_max(a_list):

    max = a_list[0]
    for item in a_list:
        if item > max:
            max = item
    
    return max

def main():
    
    print(find_max((100, 1, 2, 3, 11, 14)))

if __name__ == "__main__":
    main()




    