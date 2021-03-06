# selenium으로 instagram열기

from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup
# import pyautogui


# btn = pyautogui.confirm('아영이의 편리한 생활을 실행할까요?', '아영이의 편리한 생활')
# input_id = pyautogui.prompt('Instagram ID를 입력해주세요', '아영이의 편리한 생활')
# input_pw = pyautogui.prompt('Instagram Password를 입력해주세요', '아영이의 편리한 생활')
# input_keyword = pyautogui.prompt('검색할 키워드를 입력해주세요', '아영이의 편리한 생활')
# input_like = pyautogui.prompt('작업할 내용을 번호로 입력해주세요. like = 1, commant = 2, both = 3')


# Instagrm data
insta_id = "songkg8"
insta_pw = "black7kg"
keyword = "아이린"
like = "1"
# 1 일 경우 좋아요만, 2 일 경우 댓글만 ,3 일 경우 둘 다 실행, 그 외는 작업 안함


# 작성하고 싶은 댓글 목록
messageList = ["잘 보고 갑니다.", "Like it",
               "Very good!", "정말 예쁘네요!"]


driver = webdriver.Chrome(
    executable_path="/Users/songkg7/Documents/GitHub/Python sidepoject/Instagram Marketing Tool/chrome/chromedriver84"
)

url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
driver.get(url)

time.sleep(3)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div[1]/div/label/input').send_keys(insta_id)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div[2]/div/label/input').send_keys(insta_pw)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div[3]/button/div').click()

# time.sleep(3)
# popup
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

# search
time.sleep(random.uniform(3, 5))
url = f"https://www.instagram.com/explore/tags/{keyword}/"
driver.get(url)


def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    insta_photo = bsobj.find("article")
    v1Nh3List = insta_photo.findAll("div", {"class": "v1Nh3"})

    links = []
    for v1Nh3 in v1Nh3List:
        instaLink = "https://www.instagram.com"
        # <a href="123" alt="456">hi my name is ~~</a>
        linkAddr = v1Nh3.find("a")['href']
        links.append(instaLink + linkAddr)

    return links


time.sleep(4)
pageString = driver.page_source
links = parse(pageString)


# 좋아요 누르고 댓글 달기
for url in links:
    try:
        print(url)
        driver.get(url)

        rndSec = random.uniform(4, 10)
        time.sleep(rndSec)

        message = random.choice(messageList)

        # 좋아요
        if like == 1 or like == 3:
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()

        # 댓글
        if like == 2 or like == 3:
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/textarea').click()
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/textarea').send_keys(message)
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/button').click()

    except Exception as e:
        pass


driver.close()
# link뽑기
