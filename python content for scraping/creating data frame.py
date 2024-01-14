#write thr lib mode u want to install in the terminal.
import pandas as pd
states = ["odisha","MP","West bengal"]
population=[1234,6789,5567]
dict = {"States":states,"population":population}
table=pd.DataFrame.from_dict(dict)
print(table)
#dfstates.to_csv("states.csv",index=False)
