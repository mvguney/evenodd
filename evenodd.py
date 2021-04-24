list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=[["A","B","C"],["D","E","F"],["G","H","I"]]
list3=[]
for i in range(3):
  list3.append(list(zip(list1[i],list2[i])))
list4=[]
teklist=[]
ciftlist=[]
for element in list3:
  for i in range(3):
    list4.append(element[i])
print(list4)
for element in list4:
  if element[0]%2==0:
    ciftlist.append(element)
  else:
    teklist.append(element)
print(teklist)
print(ciftlist)
def yazici(li):
  for j in range(len(li),0,-1):
    print(li[0:j])
yazici(teklist)
yazici(ciftlist)
