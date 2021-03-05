from app import db
from app.models import *
from datetime import datetime
from datetime import timedelta, date
'''
u1 = User(username='Анастасия')
u1.set_password('1user1')

u2 = User(username='Екатерина')
u2.set_password('user22')

u3 = User(username='Алексей')
u3.set_password('33user')

u4 = User(username='Юлия')
u4.set_password('4user44')

s1 = Service(name='Комсомольская')
s2 = Service(name='Будёновский')

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)

db.session.add(s1)
db.session.add(s2)

db.session.commit()
'''
# client = Client.query.get(3)
# print(client.service_to_client)

# d = Delivery.query.get(1)
# print(d)
# print(d.author, d.courier, d.client, d.delivery_time)

# ds = Delivery.query.all()
# ds = Delivery.query.filter_by(courier_id=Courier.query.filter_by(name='Виталий').first().id)

# dat = date(2020, 11, 2)

# for d in ds:
#     if d.delivery_time.date() == date(2020, 11, 2):
#         print(d)
#     db.session.delete(d)
# db.session.commit()
# print(Courier.query.filter_by(name='Иван ').first())

clients = Client.query.all()
couriers = Courier.query.all()
delivery = Delivery.query.all()

for c in clients:
    db.session.delete(c)
for c in couriers:
    db.session.delete(c)
for c in delivery:
    db.session.delete(c)
db.session.commit()
