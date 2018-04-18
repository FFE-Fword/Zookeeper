# Zookeeper
First project! Employee qualification tracker. Takes user input and searches a Data Frame built with Python 3x. 

########################
	ZooKeeper
########################

INTRO:
#########

This program is to find out who's who in The Zoo that is A BTY. Pretty 
much the Personel Tracker to beat all Personel Trackers from work. Built 
using python3 code and data from the BSM tracker (SharePoint) and Monitor 
Mass. Mixed in with some insider information of course. ;)



VERSION HISTORY:
##################

-ver_0.25 16/04/2018


Fist save where program basically works with barely any features. Asks 
for a Category to search in, then a Value to look for. Returns all rows 
that match, with all their Category data. Program closes.


-ver_0.5 17/04/2018


Changed df=pd.read_csv("TheZoo_v_0.55.csv",sep=",") to 
df=pd.read_csv("TheZoo.csv",sep=","). Must manually save new .csv file and 
update as THEZoo.csv to work. Added primitive code so entering "no" at 
beginning will exit program. Added OR_search and AND_search function. With 
those added ability to chose QUICK, OR, AND search modes. OR_search() prints 
rows that have either/or values. Its a pain because all course values are 
either Yes or No. AND_search() :

When only entering 2 entries---- takes them 
as "column", "value", in that order and searches. In that respect it works 
fine but not intended result. Crashes if first entry is also a "value".

When 2x sets of "column","value" entries------ only searches the last set 
entered and ignores the first. Prints correct rows in that respect but not 
intended result. Crashes if first entry of a set is also a "value"

-ver_0.5.01 18/04/2018

Created Git repo and uploaded ZooKeeper Project!!
