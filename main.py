from peewee import *

db = PostgresqlDatabase('inventory', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Clothes(BaseModel):
    title = CharField()
    size = CharField()
    colorsused = CharField()
    type = CharField()
    quantity = IntegerField()


db.connect()

db.drop_tables([Clothes])
db.create_tables([Clothes])


slope = Clothes(title='Slope', size='s, m, l, xl',
                colorsused='white/red', type='hoodie', quantity=5)
slope.save()


tieDyeW = Clothes(title='Tie Dye W', size='m',
                  colorsused='white/pink/black', type='hoodie', quantity=1)
tieDyeW.save()


GoodVibesXwerd = Clothes(title='Good Vibes', size='m',
                         colorsused='tan/black/red', type='hoodie', quantity=1)
GoodVibesXwerd.save()


CherryBlossom = Clothes(title='Cherry Blossom',
                        size='l, xl', colorsused='white', type='hoodie', quantity=3)
CherryBlossom.save()

Sev = Clothes(title='7/11', size='m, l',
              colorsused='white', type='hoodie', quantity=3)
Sev.save()

Mask = Clothes(title='Mask', size='m, l',
               colorsused='black/white/red', type='hoodie', quantity=6)
Mask.save()

FlowersStillDie = Clothes(title='Flowers still die', size='m',
                          colorsused='white/yellow/green/black', type='tShirt', quantity=1)
FlowersStillDie.save()

OnMars = Clothes(title='On Mars', size='m, l',
                 colorsused='white/pink/blue', type='tShirt', quantity=2)
OnMars.save()

Falling = Clothes(title='Falling', size='m',
                  colorsused='white/black/red/yellow/blue', type='tShirt', quantity=1)
Falling.save()

PolaroidEyes = Clothes(title='Polaroid Eyes', size='m',
                       colorsused='blue/black/white', type='tShirt', quantity=1)
PolaroidEyes.save()

CamoLogo = Clothes(title='Camo Logo', size='l',
                   colorsused='camo/white', type='tShirt', quantity=1)
CamoLogo.save()

camoCollective = Clothes(title='Camo 2nd Logo', size='l',
                         colorsused='camo/white', type='tShirt', quantity=1)
camoCollective.save()

NoSleep = Clothes(title='No Sleep', size='s, m, l',
                  colorsused='white/green/blue/black', type='tShirt', quantity=3)
NoSleep.save()

WerdPant = Clothes(title='Repeating Logo Pants', size='30/32',
                   colorsused='navy blue/white/red', type='pant', quantity=1)
WerdPant.save()

EyePant = Clothes(title='Eye pants', size='32/34',
                  colorsused='black/white/red', type='pant', quantity=1)
EyePant.save()

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
