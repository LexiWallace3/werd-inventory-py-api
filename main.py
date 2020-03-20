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
                  colorsused='white/pink/black/blue', type='hoodie', quantity=1)
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
                         colorsused='blue/black/yellow/green/', type='hoodie', quantity=1)
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

print('#######################################')
print('           Werd inventory')
print('#######################################')
