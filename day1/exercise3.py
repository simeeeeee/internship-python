def gugudan(x):
    for i in range(1,10):
        print(f"{x} * {i} = {x*i}")

for i in range(2,10):
    print(gugudan(i))

def vending_machine(x, y):
    change = x - y
    answer = { 'pass' : f"커피나왔습니다. 거스름돈은 {change}",
              'fail':"돈이 부족합니다."}
    
    if change>=0:
        print(answer['pass'])
    else:
        print(answer['fail'])

vending_machine(5000,2500)
vending_machine(1000,2500)

def bmi(w,h):
    bmi = w/h
    if(bmi>=30.0):
        print("비만")
    elif(bmi>=25):
        print("과체중")
    elif(bmi>=18.5):
        print("정상")
    else:
        print("저체중")

bmi(100,170)
