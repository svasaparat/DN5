#ČE ŽELITE PREIZKUSITI DRUG NAČIN DELOVANJA, PRESTAVITE "#" IZ 10 V 9 VRSTICO




import requests


page = requests.get("https://example.com/")
#page = requests.get("http://example.com/neobstaja")


if page.status_code == 200:
    print(page.text)
else:
    print("False")




