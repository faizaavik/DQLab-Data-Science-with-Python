sepatu ={'nama':'sepatu niko','harga': 150000,'diskon':30000}
baju ={'nama':'baju unikloh','harga': 80000,'diskon':8000}
celana={'nama':'celana lepis','harga':200000,'diskon':60000}
harga_sepatu = sepatu['harga'] - sepatu['diskon']
harga_baju = baju['harga'] - baju['diskon']
harga_celana = celana['harga'] - celana['diskon']
total_harga = (harga_sepatu + harga_baju + harga_celana ) * 1.1 
print(total_harga)