'''
9
10 20 20 10 10 30 50 10 20

OP: 3 '''

n = int(input())
# ll = []
#
# for x in range(n):
#     ll.append(input())
ll = list(map(int, input().split()))
dd = {}
c = 0
if len(ll)!=n:
    print('failed')
else:
    c = 0
    for x in ll:
        dd[x] = ll.count(x)

for x in dd.values():
    if x//2 >=1:
        c+=x//2
print(c)

