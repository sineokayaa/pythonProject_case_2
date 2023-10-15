import requests

req = 'куртка женская'
url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + req
r = requests.get(url)
text = r.text

names = []
codes = []

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
    ind_1 = text.find('<span class="d-multifilters-skeleton__checkbox">')
    ind_2 = text.find('data-form-action-login="/customer/account/login/"')
    text = text[ind_1:ind_2]
    for j in range(60):
        start = text.find('<div class="x-product-card-description__microdata-wrap">')
        text=text[start + 56:]
        end = text.find('<img')
        text=text[:end]
        link_1 = text.find('<a href=') + 9
        link_2 = text.find('class="x-product-card__link') - 2
        link = 'https://www.lamoda.ru' + text[link_1:link_2]
        code = text[link_1+3:link_1+15].upper()
        codes.append(code)
        name_1 = text.find('<div class="x-product-card-description__product-name">') + 55
        name_2 = text.find('</div></div></div></a>')
        name = text[name_1:name_2]
        names.append(name)
        item = requests.get(link)
        item = item.text()
'''
ind_1 = text.find('<span class="d-multifilters-skeleton__checkbox">')
ind_2 = text.find('data-form-action-login="/customer/account/login/"')
text = text[ind_1:ind_2]
start = text.find('<div class="x-product-card-description__microdata-wrap">')
text=text[start + 56:]
end = text.find('<img')
text=text[:end]
link_1 = text.find('<a href=') + 9
link_2 = text.find('class="x-product-card__link') - 2
link = 'https://www.lamoda.ru' + text[link_1:link_2]
item = requests.get(link)
item = item.text
#print(item)
item_ind = item.find('<div class="popup auth-popup hidden"')
item = item[item_ind:]
print(item.find('Страна производства'))

'''
name_1 = text.find('<div class="x-product-card-description__product-name">') + 54
name_2 = text.find('</div></div></div></a>')
name = text[name_1 + 1:name_2]
print(name)'''
