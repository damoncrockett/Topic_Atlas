import pandas as pd 
import glob,os

PRE = "/data/damoncrockett/"
DIR = PRE + "twitter-atlas/"
TABLEDIR = DIR + "500-city-tables-10km/" 
RICHDIR = DIR + "tweets/"
ACTORDIR = DIR + "actor-tables/"
TARGET = DIR + "500-city-tables-10km-wide/"

# First we produce actor tables by year
richtables = glob.glob(os.path.join(RICHDIR,"*.csv"))

counter13 = -1
counter14 = -1

for richtable in richtables:
    basename = os.path.basename(richtable)
    year = basename.split("_")[2]
    
    df = pd.read_csv(richtable)
    df = df[['mongo_id','actor_id']]

    single = ["2011","2012"]
    if year in single:
        df.to_csv(ACTORDIR+year+".csv",index=False)
    
    elif year=="2013":
        counter13+=1
        if counter13==0:
            tmp = df
        else:
            tmp = tmp.append(df)

    elif year=="2014":
        counter14+=1
        if counter14==0:
            temp = df
        else:
            temp = temp.append(df)

    print(richtable)

tmp.to_csv(ACTORDIR +"2013.csv",index=False)
temp.to_csv(ACTORDIR +"2014.csv",index=False)