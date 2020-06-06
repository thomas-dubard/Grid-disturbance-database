from robo_head import *

db_name = "PICHE"
db_init(db_name)

dtbt = ('2020-1', '2020-04-09', '14:46:31')

ft = [(1, 'Line', '400 kV', 'Own', 'Component', 'Direct earthed',
       'Single-phase earth fault', 'Primary', 'Temporary',
       'Non-intermittent', 'Lightning', '0 min'),
      (2, 'Circuit breakers', '400 kV', 'Own', 'Component',
       'Direct earthed', 'Function failing to occur',
       'Secondary/latent fault', 'Permanent',
       'Non-intermittent', 'Technical equipment', '48 h 0 min')
      ]
ot = [('Line X-Y', 1, 'Line', '0 MWh', '0 min', 'Automatically',
       'Manually after repair', '48 h 0 min'),
      ('Line Y-Z', 2, 'Line', '0 MWh', '0 min', 'Automatically',
       'Manually after inspection', '0 h 45 min'),
      ('Busbar Y', 2, 'Busbar', '0 MWh', '0 min', 'Automatically',
       'Manually after inspection', '0 h 45 min'),
      ('Power transformer Y', 2, 'Power transformer', '7 MWh', '0 min',
       'Automatically', 'Manually after inspection', '0 h 45 min')
      ]
ip = [('Power transformer', '0 h 45 min')]

try:
    db_insert_disturbance(db_name, dtbt)
    for fault in ft:
        db_insert_fault(db_name, dtbt[0], fault)
    for outage in ot:
        db_insert_outage(db_name, outage)
    for interrupt in ip:
        db_insert_interruption(db_name, dtbt[0], interrupt)
except pymysql.err.IntegrityError as err:
    print(f"Error : {err}")
