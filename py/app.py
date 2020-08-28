from py.data_access import DataAccess

db = DataAccess()
db.insert({'marklar_field': 'marklar_value'})

for d in db.find():
    print(d)
