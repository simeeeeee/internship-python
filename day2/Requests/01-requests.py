import requests
import secrets  #api key존재

base = 'KRW'

def main():
    
    #response = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={secrets.API_KEY}")
    
    #위 방식을 파라미터로 따로 보내는 방법
    payload = {"access_key": secrets.API_KEY}
    response = requests.get("http://api.exchangeratesapi.io/v1/latest",
                            params=payload)
    

    
    print(response.status_code)
    print(response.headers['Content-Type']) #html/css application/json
    #print(response.text)
    #print(type(response.text))  #str
    
    response_json = response.json()  #response.text를 dictionary화
    #print(response_json)
    print(response_json['success'])
    print(response_json['timestamp'])

if __name__ == "__main__":
    main()
