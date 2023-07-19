a = {'A':90,'B':80,'C':70,'D':60}
print(a['B'])
print(a.get('B')) ###중괄호
if('B' in a):
    print(a["B"])

#교집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
s3 = s1.intersection(s2)
print(s3)

print(s1 - s2)
s4 = s1.difference(s2)
print(s4)

#중복없는 리스트로 출력하기
s3 = [1,2,3,4,4,4,9,11,11,11,14]
s3 = list(set(s3))
print(s3)

