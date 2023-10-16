import requests
import pandas as pd
import RU_LOCAL as RU

req = input(RU.REQUEST)
url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + req
r = requests.get(url)
text = r.text

codes = []
prices = []
names = []
brands = []
discounts = []
countries = []

ind_1 = text.find(RU.FOUND) + 8
ind_2 = text.find(RU.RESULTS)
res = int(text[ind_1:ind_2])
if res % 60 == 0:
    pages = res // 60
else:
    pages = res // 60 + 1


for i in range(pages):
    url = 'https://www.lamoda.ru/catalogsearch/result/?q=' + req + '&sort=price_asc&page=' + str(i + 1)
    r = requests.get(url)
    text = r.text
    # print(text)

    ind_1 = text.find('<span class="d-multifilters-skeleton__checkbox">')
    ind_2 = text.find('data-form-action-login="/customer/account/login/"')
    text = text[ind_1:ind_2]

    if res < 60:
        pag = res
    else:
        pag = 60

    res -= pag

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
        codes.append(code)

        link = 'https://www.lamoda.ru/' + link[:link_2]

        #print(link)
        #print(code)

        item = requests.get(link)
        item = item.text

        info_1 = item.find('user: {')
        info_2 = item.find('request: {')
        info = item[info_1:info_2]



        brand_1 = info.find('"seo_tail":"brand-') + 18
        brand = info[brand_1:]
        brand_2 = brand.find('"title":') - 2
        brand = brand[:brand_2]
        brands.append(brand)

        #print(brand)

        name_1 = block.find('<div class="x-product-card-description__product-name">') + 55
        name_2 = block.find('</div></div></div></a>')
        name = block[name_1:name_2]
        names.append(name)

        #print(name)

        price_1 = item.find(',"price":') + 9
        price = item[price_1:]
        price_2 = price.find(',')
        price = price[:price_2]
        prices.append(price)

        #print(price)

        if '"type":"discount"' in info:
            discount_1 = info.find(',"badges":[{"text":"') + 20
            discount = info[discount_1:]
            discount_2 = discount.find('","type":"discount"')
            discount = discount[:discount_2]
            discounts.append(discount)

        else:
            discount = '0'
            discounts.append(discount)

        #print(discount)
        country_1 = item.find(RU.COUNTRIES) + 33
        country = item[country_1:]
        country_2 = country.find('"}')
        country = country[:country_2]
        countries.append(country)

        #print(country)

        text = text[start:]
        text = text[end:]

        #table[code] = [name, brand, country, price, discount]

print(countries)
print(names)
print(codes)
print(discounts)
print(brands)
print(prices)

table = pd.DataFrame({RU.CODE:codes, RU.NAME:names, RU.PRICE:prices, RU.DISCOUNT:discounts, RU.BRAND:brands, RU.COUNTRY:countries})
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', len(codes))

final_table = table.sort_values(by=[RU.PRICE])

print(final_table)

with open('table.txt', 'w') as f:
    print(final_table, file=f)
