import requests

req = 'трус'
url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + req
r = requests.get(url)
text = r.text

table = {}

ind_1 = text.find('найдено') + 8
ind_2 = text.find('результатов')
res = int(text[ind_1:ind_2])
if res % 60 == 0:
    pages = res // 60
else:
    pages = res // 60 + 1
if res < 60:
    pag = res
else:
    pag = 60

for i in range(pages):
    url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + req + '&pages=' + str(i + 1)
    r = requests.get(url)
    text = r.text
    # print(text)

    ind_1 = text.find('<span class="d-multifilters-skeleton__checkbox">')
    ind_2 = text.find('data-form-action-login="/customer/account/login/"')
    text = text[ind_1:ind_2]

    for j in range(pag):
        start = text.find('<div class="x-product-card__card">')
        block = text[start + 34:]
        end = block.find('<div class="x-product-card__card">')
        block = block[:end]
        link_1 = block.find('<a href=') + 9
        link = block[link_1:]
        link_2 = link.find('class="x-product-card__link') - 2
        code = link[3:link_2]
        end_code = code.find('/')
        code = code[:end_code].upper()
        link = 'https://www.lamoda.ru/' + link[:link_2]

        item = requests.get(link)
        item = item.text
        info_1 = item.find('user: {')
        info_2 = item.find('request: {')
        info = item[info_1:info_2]
        brand_1 = info.find('"seo_tail":"brand-') + 18
        brand = info[brand_1:]
        brand_2 = brand.find('"title":') - 2
        brand = brand[:brand_2]

        name_1 = block.find('<div class="x-product-card-description__product-name">') + 55
        name_2 = block.find('</div></div></div></a>')
        name = block[name_1:name_2]

        price_1 = item.find(',"price":') + 9
        price = item[price_1:]
        price_2 = price.find(',')
        price = price[:price_2]


        if '"type":"discount"' in info:
            discount_1 = info.find(',"badges":[{"text":"') + 20
            discount = info[discount_1:]
            discount_2 = discount.find('","type":"discount"')
            discount = discount[:discount_2]

        else:
            discount = '0'

        country_1 = item.find('":"Страна производства","value":"') + 33
        country = item[country_1:]
        country_2 = country.find('"}]')
        country = country[:country_2]


        text = text[start:]
        text = text[end:]
        table[price] = [code,name,brand,country,discount]

table = dict(sorted(table.items(), reverse=True))
print(table)
mlmlb d