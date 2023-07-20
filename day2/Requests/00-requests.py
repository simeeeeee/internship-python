#가상 python 환경

#python -m venv venv
#source venv/Scripts/activate.bat
#pip install requests #pip install <package명>

import requests

def main():
    response = requests.get("https://outback.60736ldvbpamu.ap-northeast-2.cs.amazonlightsail.com/participation/statistics")
    print(response)
    print(response.status_code)
    #type(response.headers) -> dict
    print(response.headers['Content-Type'])  #html/css
    #개발자도구 -> network -> headers : CORS정책도 확인...
    #request URL 엔드포인트로 바로 url입력시 json형태로 출
    print("Content: ", response.text) ##HTML나오면 CSR / 보통 SSR임
    #GET POST PATCH PUT DELETE


if __name__ == "__main__": ##js에서 init()과 동일한 기능
    main()