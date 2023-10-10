import requests

def insPlanet():
    url = 'http://localhost:5000/planets'
    myobj = {'id': None, 'name': 'somevalue'}
    x = requests.post(url, json = myobj)
    print(x.text)

def err1():
    url = 'http://localhost:5000/planets'
    myobj = {'id': None, 'name': ''}
    x = requests.post(url, json = myobj)
    print(x.text)
def err2():
    url = 'http://localhost:5000/planets'
    myobj = {'id': None}
    x = requests.post(url, json = myobj)
    print(x.text)


def insConn():
    url = 'http://localhost:5000/connections'
    myobj = {'id': None, 'from_planet_id': 1, 'to_planet_id': 1, 'price': 42}
    x = requests.post(url, json = myobj)
    print(x.text)

def errNotFound():
    url = 'http://localhost:5000/connections'
    myobj = {'id': None, 'from_planet_id': 1, 'to_planet_id': 111111, 'price': 42}
    x = requests.post(url, json = myobj)
    print(x.text)

#insPlanet()
err1()
err2()

insConn()
errNotFound()

