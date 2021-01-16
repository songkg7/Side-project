from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from pathlib import Path
import time

start_time = time.time()
baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
Puppy = {
    "리트리버 견종": ["골든 리트리버", "래브라도 리트리버"],
    "푸들 견종": ["스탠다드 푸들", "미니엄 푸들", "토이 푸들", "미니어처 푸들"],
    "스피츠 견종": ["시베리안 허스키", "진돗개", "시바견", "포메라니안", "사모예드", "차우차우"],
    "말티즈 견종": ["말티즈", "Maltese"],
    "다리 짧은 견종": ["웰시코기", "닥스훈트"],
    "테리어 견종": ["요크셔 테리어", "잭 러셀 테리어", "폭스 테리어", "보스턴 테리어"],
    "스패니얼 견종": ["코카 스패니얼", "아메리칸 스패니얼", "블루피카르디 스패니얼", "잉글리시 코커 스패니얼", "스패니얼"],
    "셰퍼드 견종": ["저먼 셰퍼드"],
    "치와와 견종": ["치와와", "장모 치와와"],
}

print("Downloading...")
Path("./puppy-img").mkdir(parents=True, exist_ok=True)
for k, v in Puppy.items():
    Path("./puppy-img/" + k).mkdir(parents=True, exist_ok=True)
    for breed in v:
        url = baseUrl + quote_plus(breed)
        html = urlopen(url)
        soup = bs(html, "html.parser")
        img = soup.find_all(class_="_img", limit=50)
        Path("./puppy-img/" + k + "/" + breed).mkdir(parents=True, exist_ok=True)
        n = 1
        for i in img:
            imgUrl = i["data-source"]
            with urlopen(imgUrl) as f:

                with open(
                    "./puppy-img/"
                    + k
                    + "/"
                    + breed
                    + "/"
                    + breed
                    + " "
                    + str(n)
                    + ".jpg",
                    "wb",
                ) as h:
                    # w - write b - binary

                    img = f.read()
                    h.write(img)
            n += 1


print(
    "===================================================================================================="
)
print("Download Complete!")
print("WorkingTime: {} sec".format(time.time() - start_time))
