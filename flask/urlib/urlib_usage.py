from urllib import parse

url = "https://myapp.com/login/"
queryString = {'name': 'Jhon',
               'age': '18'}

query = parse.urlencode(queryString)

print(url + query)

queryString = {"jeans": "Bell Botton",
               "colors": ['blue', 'white']}

query = parse.urlencode(queryString, doseq=True)
print(url+query)

