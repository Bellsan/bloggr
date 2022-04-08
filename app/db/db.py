import uuid
from argon2 import PasswordHasher
from os import path
import json

ph = PasswordHasher()
filename = 'C:\\Users\\Elliot\\Documents\\programming\\python\\bloggr\\app\\db\\db.json'
db = {}
temp = {
    'users': [
        {
            'uuid': '<uuid>',
            'email': '<email>',
            'password': '<password>',
            'username': '<username>',
            'firstname': '<firstname>',
            'lastname': '<lastname>'
        },
        {
            'uuid': '9ec59590-3a8e-422d-b6cc-56a7a5de4dfa',
            'email': 'elliot@steffensens.se',
            'password': 'Test12345678!',
            'username': 'ElliotS',
            'firstname': 'Elliot',
            'lastname': 'Steffensen'
        },
    ]
}
def createUser(email, password, username, firstname, lastname):
    id = uuid.uuid4()
    tmp = {
        'uuid': str(id),
        'email': email,
        'password': password,
        'username': username,
        'firstname': firstname,
        'lastname': lastname
    }
    x = loadDB()
    x['users'].append(tmp)
    writeDB(x)

  
def getHash(email):
    jsonDB = loadDB()
    for i in jsonDB['users']:
        if i['email'] == email:
            return i['password']
        else:
            raise Exception("User not found")
        
    
def writeDB(data):
    if path.isfile(filename) is True:
        with open(filename, 'w') as json_db:
            json.dump(data, json_db)
    elif path.isfile(filename) is False:
        raise Exception("File not found")

def loadDB():
    if path.isfile(filename) is True:
        with open(filename) as fp:
            db = json.load(fp)
            return db
    elif path.isfile(filename) is False:
        raise Exception("File not found")
    
def verifyEmail(email):
    json_db = loadDB()
    for i in json_db['users']:
        if i['email'] == email:
            return False
    return True

if __name__ == '__main__':
    createUser('elliot@steffensens.io', 'Hejsan1234', 'Elliot2J', 'Rickard', 'Astley')
    #writeDB(temp)