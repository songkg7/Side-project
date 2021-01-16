import requests

json = requests.get("https://www.naver.com/srchrank?frm=main").json()
# print(json)

ranks = json.get("data")
# print(ranks)

i = 1
f = open("/Users/songkg7/Documents/GitHub/Python sidepoject/1/photo/text.txt", 'w')
for r in ranks:
    data = str(i) + "위 " + r.get("keyword") + "\n"
    i += 1
    f.write(data)
f.close()

