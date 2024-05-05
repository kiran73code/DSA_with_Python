from array import array


def main():
    """
     main function
    """
    # Creating Array with lenth of 10 and initializing values of 0's
    arr1 = array('i', [0]*8)
    print(arr1)
    
    # Inserting values to Array
    arr1.insert(0, 9)
    print(arr1)
    
    arr1.insert(10, 56)
    print(arr1)
    
    
if __name__ == "__main__":
    main()