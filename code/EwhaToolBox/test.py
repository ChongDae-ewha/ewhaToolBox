import requests

# POST할 URL
url = "https://forms.gle/4zUivtFwZWXkRTU57"

# POST할 데이터
data = {
    "entry.2010186661": "1969"  # 첫 번째 옵션인 "1969" 선택
}

# POST 요청 보내기
response = requests.post(url, data=data)

# 결과 출력
print("Response Status:", response.status_code)
