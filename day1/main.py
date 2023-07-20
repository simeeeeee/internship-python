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

#꺼내기 
a.pop() #마지막 요소를 꺼내고 리스트에서 해당 요소 삭제
print(a)

a=["A","b","c","D","e"]
print(a.pop(1))
print(a)
#pop은 pop() 하면 마지막 요소
#      pop(idx)  idx요소의 값을 pop

print(a.count("A"))
print(sorted(a))

# b ="lalalalaaa"
# print("count a is: ", b.count("a"))

my_list = [0] * 10 # 원소가 10개가 된 리스트
my_tuple = (0, 0) * 5 # 튜플은 (0)시, 튜플인지 인식못함! 그래서 (0, ) 콤마 무조건 있어야함

print(type(0)) # class 'int'
print(my_list)
print(my_tuple)

my_list = [1,2,3,["a","b","c"]]
print(my_list[3][2])
print(len(my_list))  # 4
print(len(my_list[3]))  # 3

##dictionary => javascript의 object, json과 유사
my_dictionary = dict() #선언
print(my_dictionary)
my_dictionary = {"key" : "value"} #할당
print(my_dictionary)
my_dictionary = {"name":"gildong","age":20, "location":"seoul"}
my_dictionary["favorite_numbers"] = [1,2,3] #추가

my_dictionary["office_location"] = "Dangsan"

#삭제
del my_dictionary["office_location"]

my_dictionary["favorite_color"] = "green"
my_dictionary["favorite_foods"] = [{"name":"apple",
                                    "is_healty":True},
                                    {"name":"pizza",
                                     "is_healty":False}] #딕셔너리로된 리스트

print(my_dictionary["favorite_foods"])
print(my_dictionary)

#print(my_dictionary["office_location"]) ##keyerror
print(my_dictionary.get("office_location")) # 키값이 존재하지 않아 -> none  에러안나고 none나오게
#키값이 없다면 뒤에 값을 출력
print(my_dictionary.get("office_location","없다면 이거"))

print("----------------------")
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items()) # key, value값을 튜플형식으로 (key,value)

print("----------------------")
for key, value in my_dictionary.items():
    print("key", key)
    print("value", value)


print("age" in my_dictionary) #in -> True/False(boolean)로 반환 
                            # key값이 존재 : True/ 없음 : False

if "age" in my_dictionary:
    pass
else:
    my_dictionary["age"] = 50

##Set
my_list = [1,2,3, "A"]
my_list.append("B")
my_list.append("B")
my_list.append("B")
print(my_list)

#print(set(my_list)) #리스트를 set로

my_set ={1,2,3,"A"}
my_set.add(4)
my_set.add(4)
my_set.add(4)
my_set.add(4)
print(my_set)
#set은 중복안됨

a = "Hello"
my_set = set(a)
print(my_set) #hello 중 중복되는 l은 하나만

set1 = {1, 2, 3, 4, 5}
set2 = {4,5,6,7}
set2.add(8)
set2.update([12,3,66,83,11]) #리스트로 추가

print(set1 & set2) #교집합
print(set1 | set2) #합집합
print(set1 - set2) #차집합

##연산자
print(5 == "5") #False
print(5 > 3 and 10 > 1)
print(5 < 3 or 10 > 1)
print(not 1 > 2)
print(not False)  #True

##if문
a = "student"
if a =="teacher":
    print("hello")
    print("----") #중괄호 X
else: #elif(조건):
    print("nope")
    print("!!!!!")


#score = input("점수가 몆 점인가요? ")
#score = int(score)
#score = int(input("점수가 몆 점인가요? "))
#input으로 받을때는 무조건 String으로 받아들임 그래서 형변***

# if score >= 60:
#     print("pass")
# else:
#     print("fail")

# #score = int(input("점수는? "))
# if 90 <= score < 100:  #score >=90 and score < 100
#     print('A')
# elif score >=80:
#     print('B')
# elif score>=70:
#     print('C')
# elif score>=60:
#     print('D')
# else:
#     print('F')

##while문
a = 10
while a > 0:
    print('hello')
    a -= 1

a = -5
while a < 0:
    print('while')
    a += 1

my_list =['A', 'B', 'C', 'D']
for letter in my_list:
    print(letter)

##range
print(range(5))  #range(0, 5)->0,1,2,3,4
for i in range(5):
    print(i)

for i in range(len(my_list)):
    print(my_list[i])

##function
def say_hello():
    print('hello')

def say_goodbay(name):
    print("goodbye,", name)

say_hello()
say_goodbay("Jack")

##abs
print(abs(3))
print(abs(-3.5))

##id -> 객체//메모리에 할당한 값
a = 3
print(id(a))
b = 3
print(a is b)

##sum -> 리스트,튜플,세트의 합
print(sum([1,2,4]))

##range
for i in range(0,5,2): #start,stop,step
    print(i)
for i in range(5,0,-2):
    print(i)

##filter() -> 걸러낸다
def positive(x):
    return x > 0  
    #if x>0 
    #  return True
    #return False
a = [ 1, 3, 6, 0, -2 ]
#print(positive(a)) -> error : int , List 형이 서로 달라
print(list(filter(positive,a)))
