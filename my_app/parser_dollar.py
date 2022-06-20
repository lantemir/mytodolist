
import requests
from bs4 import BeautifulSoup


url = "https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}

response = requests.get(url=url, headers=headers)

# print("decode: ")
# print(response.content.decode())  #decode это Из байт в строку – decode
print("\n\n\n\n")


soup = BeautifulSoup(response.content, 'html.parser')
allTr = soup.findAll("tr")
print("allTr: ")
print(allTr)
print("\n\n\n\n")

arrfirst= []

for tr in allTr:
    # print(i)
    # print("\n\n")

    firsttr = tr
    print("firsttr: ")
    print(firsttr)
    print("\n\n\n\n")

    print("newtest: ")
    newtest = firsttr.text.split('class="text-left"')
    print(newtest)
    print("\n\n\n\n")

    print("newtest3: ")
    newtest3 = newtest[0].strip()
    print("\n\n\n\n")

    print("newtest4: ")
    newtest4 = newtest3.split('\n')
    print(newtest4)
    print("\n\n\n\n")

    arrfirst.append(newtest4)




print("arrfirst: ")
print(arrfirst)
print("\n\n\n\n")

dollar = 0
for j in arrfirst:
    if j[1] == 'USD / KZT':
        dollar=float(j[2])


print("rezult: ")
print (502000 / dollar)
print("\n\n\n\n")


