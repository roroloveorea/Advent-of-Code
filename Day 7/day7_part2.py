with open('Day 7/input.txt', 'r') as file:    
    # print(file)
    myList = []
    for line in file:
        print(line)
        data = line.split()

        myList.append(data)
    print(myList)

rank = {}
def find_hand(hands):
    print(hands)
    item_dict = {}
    for items in hands:
        item_dict[items] = item_dict.get(items, 0) + 1
    # item_dict = sorted(item_dict.items(), key=lambda x:x[1], reverse=True)  
    item_dict={k: v for k, v in sorted(item_dict.items(), key=lambda item: item[1],reverse=True)}
    print(item_dict)
    # if first in list is more than 2, add j to that
    if "J" in item_dict:
        
        value = item_dict["J"]
        item_dict.pop("J", None)
        if item_dict:
            first_key = next(iter(item_dict))
            item_dict[first_key] = item_dict[first_key] + value
            
        else:
            first_key = "2"
            item_dict[first_key] = value
        
        
    # if first in list is 2 then compare if second in list is also two
    
    if len(item_dict) == 1:
        return 7
    if len(item_dict) == 2:
        if list(item_dict.values())[0] == 4:
            return 6
        else:
            return 5
    if len(item_dict) == 3:
        if list(item_dict.values())[0] == 3:
            return 4
        else:
            return 3
    if len(item_dict) == 4:
        return 2
    if len(item_dict) == 5:
        return 1
    
def find_order(hands):
    hands_dict = {
    "A":13, 
    "K":12, 
    "Q":11, 
    # "J":10, 
    "T":9, 
    "9":8, 
    "8":7, 
    "7":6, 
    "6":5, 
    "5":4, 
    "4":3, 
    "3":2,
    "2":1,
    "J":0
}
    list = []
    for i in hands:
        list.append(hands_dict[i])
    return list
        
for items in myList:
    the_list = []
    the_list.append(find_hand(items[0]))
    the_list.extend(find_order(items[0]))
    rank[items[1]] = the_list


def find_none_values(dictionary):
    none_values = {}
    for key, value in dictionary.items():
        if None in value:
            none_values[key] = value
    return none_values 
# print(find_none_values(rank))          
# print(find_type("A7Q7Q"))
# item_dict = {
#     1:1
# }
# print(list(item_dict.values())[0])


sorted_dict = dict(sorted(rank.items(), key=lambda item: item[1]))
print(sorted_dict)
i =1
thesum = 0
for key, value in sorted_dict.items():
    
    
    
    thesum+=(i*int(key))
    i+=1
print(thesum)
        
