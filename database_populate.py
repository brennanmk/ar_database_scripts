'''
https://docs.peewee-orm.com/en/latest/peewee/api.html
https://docs.peewee-orm.com/en/latest/peewee/quickstart.html
https://docs.python.org/3/library/csv.html
'''

from peewee import *
import datetime
import csv

db = MySQLDatabase('ar', host='71.232.14.210', port=3307, user='root', password='NveQlG8bKp89hPWMdhdC6jBnd')

class robots(Model):

    name = CharField()
    created = DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'

class database_controller():
    def create_tables(self):      
        robots.create_table()

    def drop_tables(self):      
        robots.drop_table()

    def populate_tables(self):
        data = []
        with open('data.csv') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                for row in reader:
                    print(', '.join(row))

        for vals in data:
            robots.create(text='').save()
    
if __name__ == '__main__':
    controller = database_controller
    controller.drop_tables()
    controller.create_tables()
    controller.populate_tables()