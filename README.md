# pythonAPI
Multiple API projects using Python, Flask, MongoDB, Docker

## Nice to have links
During the tutorial multiple techniques are being used. The links below give more information, how-to's about these techniques.
- [Virtualbox](https://www.virtualbox.org/)
- [Make Virtual Box show Ubuntu full screen](https://www.tecmint.com/install-virtualbox-guest-additions-in-ubuntu/)
- [Ubuntu](https://ubuntu.com/download/desktop)
- [Flask](https://www.fullstackpython.com/flask.html)
- [Install MongoDB on ubuntu in virtualbox](https://websiteforstudents.com/install-mongodb-on-ubuntu-18-04-lts-beta-server/)
- [Install docker engine](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Install docker compose](https://docs.docker.com/compose/install/)
- [Mongo Cheat sheet](https://github.com/pdkorf/pythonAPI/blob/master/ReferenceCards15-PDF.pdf)
- [Docker Cheat sheet](https://github.com/pdkorf/pythonAPI/blob/master/docker-cheat-sheet.pdf)
- [Hashing for Python](https://www.mindrot.org/projects/py-bcrypt/)

## Handy commands
### Start Mongo in virtualBox
```bash
sudo systemctl stop mongod.service
sudo systemctl start mongod.service
sudo systemctl enable mongod.service
sudo systemctl status mongod
```

### Mongo tips
Pretty way of showing a mongo find query
```js
db.mycol.find({}).pretty()
```

Return just one resutl, even when there are multiple 'Jack's' 
```js
db.mycol.findOne({"name":"Jack"}).pretty()
```

Operation | Syntax
------------ | -------------
Equality | ```{<key>:<value>}```
Less than | ```{<key>:{$lt:<value>}}```
Less Than Equals | ```{<keu>:{$lte:<value>}}```
------------ | -------------
Greater Than | ```{<key>:{$tg:<value>}}```
Greater than Equals | ```{<key>:{$gte:<value>}}```
Not Equals | ```{<key>:{$ne:<values>}}```

### AND in MongoDB
```js
db.mycol.find(
  {
    $and: [
      {key1: value1},{key2: value2}
    ]
  }
).pretty()

db.mycol.find({$and:[{"likes:{$gte:50}},{"title": "MongoDB overiew"}]}).pretty()
```

### OR in MongoDB
```js
db.mycol.find(
  {
    $or: [
      {key1: value1},{key2: value2}
    ]
  }
).pretty()

db.mycol.find({$or:[{"likes:{$gte:50}},{"title": "MongoDB overiew"}]}).pretty()
```

### Updating documents in MongoDB
Update single document
```js
db.COLLECTION_NAME.update(SELECTION_CRITERIA, UPDATED_DATE)

d.mycolupdate({'title':'MongoDB Overview'},{$set:{'title':'New MongoDB Tutorial'}})
```

Update multiple documents
```js
db.mycol.update({'title':'MongoDB Overview'},{$set:{'title':'New MongoDB Tutorial'}},{multi:true})
```

### Deleting documents
```js
db.COLLECTION_NAME.remove(DELTION_CRITERIA)

// Optional, if true remove only 1 document
justOne = True 

db.mycol.remove({'title': 'MongoDB Overview'})
```

### Projection
Selecting only the necessary data,
After find finds data, only return the data i really need. Instead of returning all the data.
Like only 'name' and 'age', not 'adress'

```js
db.COLLECTION_NAME.find({},{KEY:1})

// show title, don't return the ID
db.mycol.find({},{'title:1,_id:0})  
```

### Limiting records
Just 100 records instead of all

```js
db.COLLECTION_NAME.find().limit(NUMBER)

db.mycol.find({}.{'title':1,id:0}).limit(1)
```

### Sorting Documents
```js
db.COLLECTION_NAME.find().sort(KEY:1)
// 1 = ascending
//0 = descending

db.mycol.find().sort({'likes':1})
```

## Docker

### Build and run the compose file
- docker-compose build
- docker-compose run

## API protocol example
Resource | Address | Protocol | Param | Response + status codes
------------ | ------------- | ------------- | ------------- | -------------
Register User | /register | POST | Username: string<br> password : string | 200 OK
Store Sentence | /store | POST | Username: string<br> password: string<br> sentence: string | 200 ok<br> 301 out of tokens<br> 302 invalid Username or Password
Retrieve Sentence | /get | GET | Username: string<br> password: string | 200 ok<br> 301 out of tokens<br> 302 invalid Username or Password

## Hashing for python
```python
import bcrypt

# Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# gensalt's log_rounds parameter determines the complexity.
# The work factor is 2**log_rounds, and the default is 12
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))

# Check that an unencrypted password matches one that has
# previously been hashed
if bcrypt.hashpw(password, hashed) == hashed:
        print "It matches"
else:
        print "It does not match"
```
