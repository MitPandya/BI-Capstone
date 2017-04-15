import pymongo
from pymongo import MongoClient
client = MongoClient("localhost", 27017)

db = client.yelp_db
#collection = db.yelp_academic_dataset_review
collection = db.yelp_academic_dataset_business
collection2 = db.yelp_academic_dataset_review

data = collection.find({'$and':[{'categories':'Food'}]})

business_id = []
for x in data:
	business_id.append(x['business_id'])

review_data = list(collection2.find())

reviews = filter(lambda x: x in business_id, review_data)

print len(reviews)

'''print collection.count()

data = collection.find({'$and':[{'state':'AZ'}]})

names = []
c = 0
for x in data:
	names.append(x['city'])
	c += 1
print c
names = list(set(names))
print names'''