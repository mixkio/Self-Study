from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusurl = input('검색어를 입력하세요.')
url = baseurl + quote_plus(plusurl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

n = 1
for i in img:
    imgurl = i['data-source']
    with urlopen(imgurl) as f:
        with open(plusurl+str(n)+'.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgurl)

print('다운로드 완료')
