##구구단
def gugudan(x):
    for i in range(1,10):
        print(f"{x} * {i} = {x*i}")

for i in range(2,10):
    print(gugudan(i))

##
def multiply_box():
    for i in range(2,10):
        for j in range(1,10):
            print(f"{i} * {j} = {i*j}")

multiply_box()


##자판기
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

##
coffee_dictionary = {
    "americano":{
        'price': 2500,
        'type': 'ice'
    },
    "latte":{
        'price': 3500,
        'type':'ice'
    }
}
def vending_machine():
    amount = int(input("돈을 입력"))
    coffee = input("커피")
    if coffee_dictionary.get(coffee):
        coffee_info = coffee_dictionary[coffee]
        price = coffee_info["price"]
        if(amount-price>=0):
            print(f"{coffee}나왔습니다. 거스름돈 {amount-price}입니다.")
        else:
            print("돈이 모자랍니다.")
    else:
        print("그런 메뉴가 없습니다.")

vending_machine()



def bmi(weight,height):
    bmi = round(weight / (height * 0.01)**2 , 2)
    if(bmi>=30.0):
        print("비만")
    elif(bmi>=25):
        print("과체중")
    elif(bmi>=18.5):
        print("정상")
    else:
        print("저체중")

bmi(100,170)
