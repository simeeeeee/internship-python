import requests
import secrets


def main():
    #payload = {"access_key": secrets.API_KEY, "base": 'KRW' } #400에서 유료서비스
    payload = {"access_key": secrets.API_KEY}
    response = requests.get("http://api.exchangeratesapi.io/v1/latest",
                            params=payload)
    

    if not response.status_code == 200:
        print("Error occured")
        return

    response_dict = response.json()

    success = response_dict['success']
    timestamp = response_dict['timestamp']
    date = response_dict['date']
    base = response_dict['base']
    KRW = response_dict['rates']['KRW']
    USD = response_dict['rates']['USD']

    print(f"성공코드 : {success}")
    print(f"timestamp : {timestamp}")
    print(f"USD : {USD}")


if __name__ == "__main__":
    main()


