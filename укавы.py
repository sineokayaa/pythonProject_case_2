table = pd.DataFrame(
    {'Code': codes, 'Name': names, 'Price': prices, 'Discount': discounts, 'Brand': brands, 'Country': countries})
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', len(codes))
final_table = table.sort_values(by=['Price'])
print(final_table)