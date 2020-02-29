from selenium import webdriver
import requests
driver = webdriver.Chrome()
url = 'https://www.zhihu.com'
driver.get(url)

backpic = requests.get('https://static.zhihu.com/heifetz/sign_bg.db29b0fbd2f78dd8c1b7.png')
print(backpic.content)
fo = open('results.png','wb')  #todo 别忘了文件名后的格式（png）
fo.write(backpic.content)
fo.close()

# responsekr = requests.get('https://36kr.com/?name=hijewish&class=rainbow6')
# print(responsekr.text)