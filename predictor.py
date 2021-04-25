import csv
import zipfile
import pandas as pd

#all_matches_csv = open("all_matches.csv", "r")
#dict_reader = csv.DictReader(all_matches_csv)

#ordered_dict_from_csv = list(dict_reader)[0]
#dict_from_csv = dict(ordered_dict_from_csv)

#print(dict_from_csv)
def predictRuns(testInput):
    prediction = 0

    zf = zipfile.ZipFile('D:\dev\IPL\ipl_csv2.zip')
    df = pd.read_csv(zf.open('all_matches.csv'))
    pl = pd.read_csv('D:\dev\IPL\playersList.csv')
    ti = pd.read_csv(testInput)
    print(type(ti.batsmen))
    scores = df.groupby("striker")["runs_off_bat"].sum()
    played = df.groupby("striker")["match_id"].nunique()
    df_new = df[(df["ball"] < 7)]
    #df_new.to_csv('sixovers.csv')
    extras = df_new.extras.sum()
    #print(extras)
    #print(df_new.wicket_type.count())
    wickets = df_new.wicket_type.count()
    #print(df_new.match_id.nunique())
    matches = df_new.match_id.nunique()

    avgscores = scores/played
    print(avgscores)
    avgextras = extras/matches
    print(avgextras)
    avgwickets = wickets/matches
    print(testInput)


    return prediction
    #ti = pd.read_csv(testInput)
    #df_new["weight"].mean()
    #print(df_new)
    #print(df)
