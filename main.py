import requests
req = input('Введите ваш запрос ')
url = 'https://www.lamoda.ru/catalogsearch/result/?q='+req
r = requests.get(url)
text = r.text
#print(text)


#ind = text.find('<span class="d-multifilters-skeleton__checkbox">')
#text = text[ind:]
print(text)