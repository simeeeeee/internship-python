a = [1,2,3]
a[2] = 4 #재할당
print(a)

#삭제
del a[2]
print(a)

a = [0,1,2,3,4,5,6,7,8]
del a[1:6] # 1~5번째 idx값 삭제
print(a)

#추가
a = [0, 1, 2, 3]
a.append(4) #원소(요소) 하나
a.append(5)
a.append(["a","b","c","d"]) #[0, 1, 2, 3, 4, 5, ['a', 'b', 'c', 'd']]
a.extend(["a","b","c","d"]) #리스트에 리스트를 더함 #[0, 1, 2, 3, 4, 5, ['a', 'b', 'c', 'd'], 'a', 'b', 'c', 'd']
print(a)

#정렬
a = [9, 8, 2, 6, 3, 66, 33]
a.sort() #바뀐 값으로 재할당
print(a)
a = [9, 8, 2, 6, 3, 66, 33]
print(sorted(a)) #재할당 아님
print(a)
a = ['a','c','d','b','A','B']
a.reverse() #재할당
print(a)
a.append(10)
print(a)

#삽입   idx,value
a.insert(2,"33")
a.insert(5, "33")
print(a)

#삭제 첫번째로 나오는 값 삭제
a.remove('33')

#꺼내기 마지막 요소를 꺼내고 리스트에서 해당 요소 삭제
a.pop()
print(a)

