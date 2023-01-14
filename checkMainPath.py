# 结点数
n = 26

list = []
result = []
for i in range(26):
    list.append([i+1])
list.remove([2])
list.remove([11])
list.remove([19])
print(list)
# 子节点
dict = {
    1: [2,3],
    3: [4],
    4: [5,9],
    5: [6],
    6: [7,8],
    7: [6],
    8: [4],
    9: [10],
    10: [11,12],
    12: [13],
    13: [14,10],
    14: [15],
    15: [16,17],
    16: [13],
    17: [15,18],
    18: [19,20],
    20: [21,22],
    21: [23],
    22: [23],
    23: [15,24],
    24: [25,26],
    25: [15],
    26: [15]
}
mm = 0
while len(list) != 0:
    first = list.pop(0)

    for i in range(0,len(dict[first[-1]])):
        nome = first.copy()
        if (dict[first[-1]][i] in nome ) and (dict[first[-1]][i]  != nome[0]):
            continue
        nome.append(dict[first[-1]][i])
        print(nome)
        if nome[-1] == 2 or nome[-1] == 11 or nome[-1] == 19:
            result.append(nome)

        elif nome[0] == nome[-1]:
            result.append(nome)
        else:
            list.append(nome)
    mm+=1
    # if len()
    # if mm == 5000 :

# print(mm)
# print(result)

# print("-----")
# for item in result:
#     print(item)
# print("-----")
# print(len(result))
result2 = []
for item in result:
    flag = 0
    for item2 in result:
        if (item != item2) and( set(item) < set(item2)):
            flag = 1
            break
    if flag == 0:
        result2.append(item)

print("-----")
for item in result2:
    print(item)
print("-----")
print(len(result2))