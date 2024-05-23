
def isSubset( a1, a2, n, m):
    count_dict = dict()
    count_dict2 = dict()
    for index,val in enumerate(a1):
        if val in count_dict:
            count_dict[val] = count_dict[val] + 1
        else:
            count_dict[val] = 1
            
    for val in a2:
        if val in count_dict2:
            count_dict2[val] = count_dict2[val] + 1
        else:
            count_dict2[val] = 1
    for key in count_dict2:
        if key not in count_dict:
            return "No"
        if count_dict.get(key) < count_dict2.get(key):
            return "No"
    return "Yes"

if __name__ == "__main__":
    a1 = [1,2,3,4,5]
    a2 = [1,2,3,4,5]
    print(isSubset(a1, a2, 5, 5))
            