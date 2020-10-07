import pandas as pd  

file1 = open("Holiday Schedule Ranking 2019.csv", "r")

data = pd.read_csv(file1, index_col=0).T

file1.close()

file1 = open("Holiday Schedule Ranking 2019.csv", "r")

schedule = pd.read_csv(file1, index_col=0)

for c in schedule:
    schedule[c].values[:] = 0

data["col_sum"] = data.apply(lambda x:x.sum(), axis=1)

data = data.sort_values(by="col_sum", ascending = False)

data = data.T

for date in data.columns:
    date_series = data[date].nsmallest(13,keep="all")
    for i in date_series.index.values:
        preference = data[date].loc[i]
        if ((schedule[date].sum() < 3) and (schedule.loc[i].sum() < 2)):
            schedule.loc[i][date] = preference

schedule.replace(0,"", inplace = True)

schedule.to_csv("final_schedule.csv")
print("done")











