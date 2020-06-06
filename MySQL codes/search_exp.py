from robo_head import *

db_name = "PICHE"
db_init(db_name)

dtbt = ('2020-1', '2020-04-09', '14:46:31')

piche = db_select_disturbance(db_name, dtbt[0])
for key in piche.keys():
    print(key)
    print(piche[key])
