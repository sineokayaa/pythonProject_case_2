import requests
req = input('Введите ваш запрос ')
url = 'https://www.lamoda.ru/catalogsearch/result/?q='+req
r = requests.get(url)
text = r.text

ind_1 = text.find('найдено') + 8
ind_2 = text.find('результатов')
res = int(text[ind_1:ind_2])
if res % 60 == 0:
    pages = res // 60
else:
    pages = res // 60 + 1
'''
for i in range(pages):
    url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + req + '&pages=' + str(i + 1)
    r = requests.get(url)
    text = r.text
'''
ind = text.find('<span class="d-multifilters-skeleton__checkbox">')
text = text[ind:]
print(text)