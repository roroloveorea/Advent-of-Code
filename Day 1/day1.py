num_dict = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
  }
with open('input.txt', 'r') as f:
    myList = [line.strip() for line in f]
    

def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]   
listB = []
for the_items in myList:
    for word, digit in num_dict.items():
        try:
            index = the_items.find(word,0)
            print(index)
            while(index != -1):
                the_items = insert(the_items,str(digit), index+2)
                print(the_items)
                index = the_items.find(word,index)
        except:
            pass
    listB.append(the_items)
    

    
print(listB)
# print(myList)
listA = []
for item in listB:
    listnumber = ''
    for i in range(len(item)):
        # print(item[i])
        if item[i].isdigit():
            listnumber+=item[i]
            break
    for j in range(len(item)):
        # print(item[len(item)-j-1])
        if item[len(item)-j-1].isdigit():
            listnumber+=item[len(item)-j-1]
            break
            
    
    listA.append(int(listnumber))

print(listA)   
    

print(sum(listA))