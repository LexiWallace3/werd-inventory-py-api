from peewee import *
from psycopg2 import *


db = PostgresqlDatabase('inventory', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Acessories(BaseModel):
    title = CharField()
    colorsused = CharField()
    type = CharField()
    quantity = IntegerField()


db.connect()

db.drop_tables([Accessories])
db.create_tables([Acessories])



Aviators = Accessories(title='Aviators', 
                colorsused=' black/gold-lightbrown/gunmetal-lightbrown/gunmetal-blue/bronze-copper pink/bronze-copper grey', 
                type='Sunglasses', quantity=25)
Aviators.save()

Round = Accessories(title='Round', 
                  colorsused='black/gunmetal-green/bronze copper-pink/bronze-copper blue'
                   type='Sunglasses', quantity=20)
Round.save()

Hexagonal = Accessories(title='Hexagonal', 
                        colorsused='lack/grey-gunmetal/bronze-copper/gold-blue', type='Sunglasses', quantity=20)
Hexagonal.save()

CrissCross = Accessories(title='Criss cross',
                        colorsused='silver/gold', type='Earrings', quantity=10)
CrissCross.save()

LittleStud = Accessories(title='Little Stud'
              colorsused='gold/silver', type='Earrings', quantity=10)
LittleStud.save()

SharpShooter = Accessories(title='Sharp Shooter', 
               colorsused='gold/silver', type='Earrings', quantity=10)
SharpShooter.save()

ShotintheDark = Accessories(title='Shot in the Dark',
                          colorsused='gold', type='Earrings', quantity=15)
ShotinthDark.save()

Illusion = Accessories(title='Illusion', 
                 colorsused='gold', type='Earring', quantity=15)
Illusion.save()

Stealth = Accessories(title='Stealth', 
                  colorsused='gold', type='Earrings', quantity=10)
Stealth.save()

StuddedWings = Accessories(title='Studded wings',
                       colorsused='gold', type='Earings', quantity=10)
StuddedWings.save()

ButterflyHoop = Accessories(title='Butterfly Hoop', 
                   colorsused='gold', type='Earings', quantity=10)
ButterflyHoop.save()

OpenHoop = Accessories(title='Open Hoop', 
                         colorsused='gold/silver/gunmetal', type='Earrings', quantity=12)
OpenHoop.save()

Refinery = Accessories(title='Refinery',
                  colorsused='gold/silver', type='Earrings', quantity=10)
Refinery.save()

Initial = Accessories(title='Initial', 
                   colorsused='rose/gold/silver', type='Necklace', quantity=15)
Initial.save()

Coordinates = Accessories(title='Coordinates',
                  colorsused='gold/silver', type='Necklace', quantity=10)
Coordinates.save()

Lock&Key = Accessories(title='Love Hurts',
                          colorsused='gold', type='Necklace', quantity=10)
Lock&Key.save()

SUR = Accessories(title='SUR', colorsused='gold/silver', type='Necklace', quantity=10)

SUR.save()


LoveHurtsSweats = Clothes(title='Love Hurts', size='m',
                          colorsused='black/white/yellow/green', type='sweat pant', quantity=1)
LoveHurtsSweats.save()

LoveHurtsCrewneck = Clothes(title='Love Hurts', size='m',
                            colorsused='black/white/red', type='crew neck', quantity=1)
LoveHurtsCrewneck.save()

LogoShorts = Clothes(title='Logo Shorts', size='m',
                     colorsused='white/black', type='shorts', quantity=1)
LogoShorts.save()

InfiniteThought = Clothes(title='Infinite Thought', size='m',
                          colorsused='tan/black/blue', type='hoodie', quantity=1)
InfiniteThought.save()

ReaperSweats = Clothes(title='Reaper', size='m',
                       colorsused='gray/black/red', type='sweat pant', quantity=1)
ReaperSweats.save()

CartiJeanJacket = Clothes(title='Playboi Carti Jean Jacket', size='l',
                          colorsused='black/green/red/white', type='jean jacket', quantity=1)
CartiJeanJacket.save()

werdXchampionFlowers = Clothes(title='Werd x Champion', size='m',
                               colorsused='navy blue/white/green/yellow', type='hoodie', quantity=1)
werdXchampionFlowers.save()

Sakura = Clothes(title='Sakura', size='m, l, xl',
                 colorsused='white/red/pink/blue', type='hoodie', quantity=4)
Sakura.save()


NeonLogo = Clothes(title='Neon Logo', size='xl',
                   colorsused='neon green/red', type='tShirt', quantity=1)
NeonLogo.save()

JapanesesWerdShort = Clothes(
    title="'Werd' Shorts", size='m', colorsused='white', type='shorts', quantity=1)
JapanesesWerdShort.save()

OxymoronHoodie = Clothes(title='Oxy-moron', size='l',
                         colorsused='blue/black/yellow/green', type='hoodie', quantity=1)
OxymoronHoodie.save()

WhatchuWant = Clothes(title='Whatchu want from me', size='m, l',
                      colorsused='white/black/green/blue', type='tShirt', quantity=3)
WhatchuWant.save()


WhatchuWantHoodie = Clothes(title='Whatchu want from me', size='m',
                            colorsused='white/black/green/blue', type='hoodie', quantity=2)
WhatchuWantHoodie.save()


WhyTshirt = Clothes(title='Why', size='m, l, xl',
                    colorsused='white/brown/black/green', type='tShirt', quantity=4)
WhyTshirt.save()

FlipSide = Clothes(title='Flip Side', size='m, l, xl',
                   colorsused='white/black/blue/', type='tShirt', quantity=5)
FlipSide.save()

LongSleeveLogo = Clothes(title='Long Sleeve Logo', size='m, l, xl',
                         colorsused='white/red', type='long sleeve', quantity=3)
LongSleeveLogo.save()


Spider = Clothes(title='Spider', size='m',
                 colorsused='black/white/orange', type='tShirt', quantity=1)
Spider.save()


NavyBlueLogo = Clothes(title='Navy Blue Logo', size='m',
                       colorsused='navy blue/white/red', type='tShirt', quantity=1)
NavyBlueLogo.save()

NoHardFeelings = Clothes(title='No Hard Feelings', size='m',
                         colorsused='navy blue/yellow/red', type='tShirt', quantity=1)
NoHardFeelings.save()

AllEveryEverWanted = Clothes(title='All Everybody Ever Wanted', size='m',
                             colorsused='tan/navy blue/white', type='tShirt', quantity=1)
AllEveryEverWanted.save()

SeeYouNever = Clothes(title='See You Never', size='m, l',
                      colorsused='black/red/white', type='hoodie', quantity=3)
SeeYouNever.save()


print('')
print('      #######################################')
print('                  Werd Inventory')
print('      #######################################')
print('')

print('#### TYPES OF CLOTHES: hoodie, tShirt, shorts, pant, crew neck ####')
print('')

cur = db.cursor()

inputType = input(
    '-- -- Search type or "all" to view all items: ')


if inputType == 'all':
    cur.execute(
        f"SELECT title from CLOTHES")
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
            f"SELECT title, size, colorsused, type, quantity from CLOTHES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Size: ', row[1])
        print('Colors Used: ', row[2])
        print('Type: ', row[3])
        print('Quantity: ', row[4])
        print('')


if inputType == 'hoodie' or 'tShirt' or 'pant' or 'shorts' or 'crew neck':

    cur.execute(
        f"SELECT title, type from CLOTHES WHERE type = '{inputType}'")
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
            f"SELECT title, size, colorsused, type, quantity from CLOTHES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Size: ', row[1])
        print('Colors Used: ', row[2])
        print('Type: ', row[3])
        print('Quantity: ', row[4])
        print('')

# inputType = input(
#     '-- -- Search type or "all" to view all items: ')


if inputType == 'all':
    cur.execute(
        f"SELECT title from CLOTHES")
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
            f"SELECT title, size, colorsused, type, quantity from CLOTHES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Size: ', row[1])
        print('Colors Used: ', row[2])
        print('Type: ', row[3])
        print('Quantity: ', row[4])
        print('')


if inputType == 'hoodie' or 'tShirt' or 'pant' or 'shorts' or 'crew neck':

    cur.execute(
        f"SELECT title, type from CLOTHES WHERE type = '{inputType}'")
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
            f"SELECT title, size, colorsused, type, quantity from CLOTHES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Size(s) available: ', row[1])
        print('Colors Used: ', row[2])
        print('Type: ', row[3])
        print('Quantity: ', row[4])
        print('')
