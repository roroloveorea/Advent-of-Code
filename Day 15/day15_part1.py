with open('Day 15/test.txt', 'r') as file:
    content = file.read()
    content = content.replace("\n","")
    lines = content.split(',')
def find_box(line):
    value = 0
    for char in line:
        value+=ord(char)
        value*=17
        value%=256
    return value
def convert_num(string):
    new_string =''
    sign=''
    num=''
    for i in string:
        print(i)
        if i !="=" and i!="-" and (ord(i)<48 or ord(i)>57):
            new_string+=i
        if i =="=" or i=="-":
            sign=i
            print("oh")
        if ord(i)>=48 and ord(i)<=57:
            num+=i
            print(num)
    return [new_string,sign],num
            
        
the_sum = 0
boxes = {}
rank = 0
for line in lines:
    result, num = convert_num(line)
    value1=find_box(result[0])
    value=find_box(line)
    sign = result[1]
    # print(sign)
    if sign == "=":
        print("yes")
        if value1 not in boxes:
            boxes[value1]={result[0]:num}
        else:
            boxes[value1].update({result[0]:num})
    if sign == "-":
        boxes[value1].update({result[0]:0})
        
    the_sum+=value
    rank+=1
    

print(f"part1: {the_sum}")
print(boxes)
        
