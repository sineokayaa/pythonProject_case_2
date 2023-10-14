import requests
url = 'https://www.lamoda.ru/catalogsearch/result/?q=%D0%BA%D1%83%D1%80%D1%82%D0%BA%D0%B0%20%D0%B7%D0%B8%D0%BC%D0%BD%D1%8F%D1%8F%20%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F&&submit=y&page=1'
r = requests.get(url)
text = r.text
print(text)
