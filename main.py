import requests
req = input('Введите ваш запрос ')
req = req.replace(' ', '%20')
url = 'https://www.lamoda.ru/catalogsearch/result/?q='+req+'&submit=y&gender_section=women'
r = requests.get(url)
text = r.text
print(text)
'''
text = text.split('brand')
for i in range(len(text)):
    print(text[i],i)
print(text)
'''