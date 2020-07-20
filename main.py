from peewee import *
from psycopg2 import *


db = PostgresqlDatabase('inventory', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Accessories(BaseModel):
    title = CharField()
    colorsused = CharField()
    type = CharField()
    quantity = IntegerField()


db.connect()

db.drop_tables([Accessories])
db.create_tables([Accessories])

# different style and colors of sunglassess available in Inventory

Aviators = Accessories(title='Aviators', 
                colorsused=' black/gold-lightbrown/gunmetal-lightbrown/gunmetal-blue/bronze-copper pink/bronze-copper grey', 
                type='sunglasses', quantity=25)
Aviators.save()

Round = Accessories(title='Round', 
                  colorsused='black/gunmetal-green/bronze copper-pink/bronze-copper blue'
                   type='sunglasses', quantity=20)
Round.save()

Hexagonal = Accessories(title='Hexagonal', 
                        colorsused='lack/grey-gunmetal/bronze-copper/gold-blue', type='sunglasses', quantity=20)
Hexagonal.save()

# different types of earrings available

CrissCross = Accessories(title='Criss cross',
                        colorsused='silver/gold', type='earrings', quantity=10)
CrissCross.save()

LittleStud = Accessories(title='Little Stud'
              colorsused='gold/silver', type='earrings', quantity=10)
LittleStud.save()

SharpShooter = Accessories(title='Sharp Shooter', 
               colorsused='gold/silver', type='earrings', quantity=10)
SharpShooter.save()

ShotintheDark = Accessories(title='Shot in the Dark',
                          colorsused='gold', type='earrings', quantity=15)
ShotinthDark.save()

Illusion = Accessories(title='Illusion', 
                 colorsused='gold', type='earring', quantity=15)
Illusion.save()

Stealth = Accessories(title='Stealth', 
                  colorsused='gold', type='earrings', quantity=10)
Stealth.save()

StuddedWings = Accessories(title='Studded wings',
                       colorsused='gold', type='earings', quantity=10)
StuddedWings.save()

ButterflyHoop = Accessories(title='Butterfly Hoop', 
                   colorsused='gold', type='earings', quantity=10)
ButterflyHoop.save()

OpenHoop = Accessories(title='Open Hoop', 
                         colorsused='gold/silver/gunmetal', type='earrings', quantity=12)
OpenHoop.save()

Refinery = Accessories(title='Refinery',
                  colorsused='gold/silver', type='earrings', quantity=10)
Refinery.save()

# Necklaces

Initial = Accessories(title='Initial', 
                   colorsused='rose/gold/silver', type='necklace', quantity=15)
Initial.save()

Coordinates = Accessories(title='Coordinates',
                  colorsused='gold/silver', type='necklace', quantity=10)
Coordinates.save()

Lock&Key = Accessories(title='Love Hurts',
                          colorsused='gold', type='necklace', quantity=10)
Lock&Key.save()

SUR = Accessories(title='SUR', colorsused='gold/silver', type='necklace', quantity=10)

SUR.save()
 
# belts
RoriLeatherBelt = Accessories(title='Rori Leather Belt,
                     colorsused='black/brown/cream/sage', type='belt', quantity=20)
                     
RoriLeatherBelt.save()


GigLeatherChain = Accessories(title='Gigi Leather Chain',
                     colorsused='Black', type='belt', quantity=6)

GigiLeatherChain.save()


Suede= Accessories(title='Suede',
                          colorsused='tan/black/brown', type='belt', quantity=12)
Suede.save()

# hats /  hair accessories

Fedora = Acessories(title='Fedora',
                     colorsused='cream/black/olive/dusty', type='hats', quantity=20)
Fedora.save()


SuperScrunchie = Accessories(title='Super Scrunchie',
                          colorsused='tan/black/sage/orange/dusty', type='Hair', quantity=12)
SuperScrunchie.save()


DaydreamScarfPony= Accessories(title='Daydream Scarf Pony',
                          colorsused='gold/olive/blue floral/midnight garden', type='Hair', quantity=12)
DaydreamScarfPony.save()

TopKnotHeadband= Accessories(title='Top Knot Headband',
                          colorsused='gold/black', type='Hair', quantity=12)
TopKnotHeadband.save()

PrettyMessBarrette= Accessories(title='Pretty Mess Barrette',
                          colorsused='gold', type='Hair', quantity=12)
PrettyMessBarrette.save() 

BeadedClips= Accessories(title='Beaded Clips',
                          colorsused='Blush/Mint/Peach/Bronze/Ivory', type='Hair', quantity=12)
BeadedClips.save() 

# handbags 



print('')
print('      #######################################')
print('                 Accessories Inventory')
print('      #######################################')
print('')

print('#### TYPES OF ACCESSORIES: Sunglasses, Earings, Necklace, Hats, Belts, Hair ####')
print('')

cur = db.cursor()

inputType = input(
    '-- -- Search type or "all" to view all items: ')


if inputType == 'all':
    cur.execute(
        f"SELECT title from ACCESSORIES")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
    inputTitle = input('Search for individual item or type back to return: ')
    if inputTitle == 'back':
        inputType = input(
            '-- -- Search type or "all" to view all items: ')
    else:
        cur.execute(
            f"SELECT title, colorsused, type, quantity from ACCESSORIES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Colors Used: ', row[1])
        print('Type: ', row[2])
        print('Quantity: ', row[3])
        print('')


if inputType == 'sunglasses' or 'earrings' or 'necklace' or 'belts' or 'hat' or 'hair':

    cur.execute(
        f"SELECT title, type from Accessories WHERE type = '{inputType}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Type: ', row[1])
        print('')
    inputTitle = input('Search for individual item or type back to return: ')
    if inputTitle == 'back':
        inputType = input(
            '-- -- Search type or "all" to view all items: ')
    else:
        cur.execute(
            f"SELECT title, colorsused, type, quantity from ACCESSORIES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Colors Used: ', row[1])
        print('Type: ', row[2])
        print('Quantity: ', row[3])
        print('')

# inputType = input(
#     '-- -- Search type or "all" to view all items: ')


if inputType == 'all':
    cur.execute(
        f"SELECT title from ACCESSORIES")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
    inputTitle = input('Search for individual item or type back to return: ')
    if inputTitle == 'back':
        inputType = input(
            '-- -- Search type or click enter to view all items: ')
    else:
        cur.execute(
            f"SELECT title, colorsused, type, quantity from ACCESSORIES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Colors Used: ', row[1])
        print('Type: ', row[2])
        print('Quantity: ', row[3])
        print('')


if inputType == 'sunglasses' or 'earrings' or 'necklace' or 'belts' or 'hat' or 'hair':
    cur.execute(
        f"SELECT title, type from ACCESSORIES WHERE type = '{inputType}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Type: ', row[1])
        print('')
    inputTitle = input('Search for individual item or type back to return: ')
    if inputTitle == 'back':
        inputType = input(
            '-- -- Search type or click enter to view all items: ')
    else:
        cur.execute(
            f"SELECT title, colorsused, type, quantity from ACCESSORIES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Colors available: ', row[1])
        print('Type: ', row[2])
        print('Quantity: ', row[3])
        print('')
