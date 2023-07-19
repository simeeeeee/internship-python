a = {'A':90,'B':80,'C':70,'D':60}
print(a['B'])
print(a.get('B')) ###중괄호
if('B' in a):
    print(a["B"])

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
print(s1 - s2)

s3 = set([1,2,3,4,4,4,9,11,11,11,14])
print(s3)