n1 = [2,4,5,6,7,8,9,12]
n2 = [12,14,6,16,18,24,46,2,4]
n3 = []
n4 = []
for i in n1:
    for j in n2:
        if i == j:
            print(i)
            # print(i)
            if i % j == 0:
            n3.append(i)
print(n3)
print(n4)
