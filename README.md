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
