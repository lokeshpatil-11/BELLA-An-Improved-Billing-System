import requests
url='https://api.apilayer.com/image_to_text/url?url=https://tse4.mm.bing.net/th?id=OIP.XKoQcxhip3MF9TwVAS_ScAHaHa&pid=Api&P=0'
headers= {'apikey' : '41fNR8h5VwFOyum0CFhiXZc364ywHZnO'}
r=requests.get(url,headers)
r=r.content.decode()
print("API o/p: ",r)

r=r.split()

strt=r.index('"all_text":')+1
end=r.index('"annotations":')

print("string: ",r[strt:end])