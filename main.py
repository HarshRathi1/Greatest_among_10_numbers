list=[]
greatest=[0]
for i in range(1,11):
    num=int(input())
    list.append(num)
print(list)
for j in list:
    if j>greatest[0]:
        greatest[0]=j
print(greatest)