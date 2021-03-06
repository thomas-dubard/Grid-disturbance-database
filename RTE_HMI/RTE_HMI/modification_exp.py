from dbgrid import *

piche = DbGrid('Piche', '127.0.0.1', 'Aline', '123456789')

# The codes belows as remark are code examples for test/debug
# of the attributes in the classe DbGrid

# ============ DANGER ZONE =============
# piche.init_all()  # OK
# piche.del_all()  # OK
# ============ DANGER ZONE =============

'''  # test code for insert_disturbance / OK
dtbt = [time.strftime("%Y-%m-%d", time.localtime()),
        time.strftime("%H:%M:%S", time.localtime())]
piche.insert_disturbance(dtbt)
'''

'''  # test code for insert_fault / OK
ft = [('Power transformers', '400 kV', 'Own', 'Component', 'Direct earthed',
       'Single-phase earth fault', 'Primary', 'Temporary',
       'Non-intermittent', 'Lightning', '00:00:00'),
      ('Circuit breakers', '400 kV', 'Own', 'Component',
       'Direct earthed', 'Function failing to occur',
       'Secondary/latent fault', 'Permanent',
       'Non-intermittent', 'Technical equipment', '48:00:00')
      ]
for fault in ft:
    piche.insert_fault('2020-3', fault)
'''

'''  # test code for insert_outage / OK
ot = [('Line X-Y', 4, 'Overhead line', '0 MWh', '00:00:00', 'Automatically',
       'Manually after repair', '48:00:00'),
      ('Line Y-Z', 3, 'Overhead line', '0 MWh', '00:00:00', 'Automatically',
       'Manually after inspection', '00:45:00'),
      ('Busbar Y', 2, 'Bushbar', '0 MWh', '00:00:00', 'Automatically',
       'Manually after inspection', '00:45:00'),
      ('Power transformer Y', 1, 'Power transformer', '7 MWh', '00:00:00',
       'Automatically', 'Manually after inspection', '00:45:00')
      ]
for outage in ot:
    piche.insert_outage(outage)
'''

'''  # test code for insert_interruption / OK
ip = [('Power transformer', '00:45:00')]
for interrupt in ip:
    piche.insert_interruption('2020-3', interrupt)
'''

'''  # test code for select_interruption / OK
res = piche.select_interruption('2020-1')
print(res)
print(str(res['interruption'][0][-1]))
'''

'''  # test code for select_outage / OK
res = piche.select_outage(8)
print(res)
'''

'''  # test code for select_fault / OK
res = piche.select_fault('2020-2')
print(res['fault'])
print(res['outage'])
'''

'''  # test code for select_disturbance / OK
res = piche.select_disturbance('2020-1')
print(res['disturbance'])
print(res['fault'])
print(res['outage'])
print(res['interruption'])
'''

'''  # test code for fetch_table / OK
print(piche.fetch_table('interruption'))
'''

'''  # test code for create_user / OK
print(mysql.root_connection())
mysql.create_user('Piche', 'Aline', '123456789')
mdm = DbGrid('Piche', '127.0.0.1', 'Aline', '123456789')
print(mdm.connect())
'''

'''  # test code for remove_user / OK
print(mysql.root_connection())
mysql.remove_user('Aline', '%')
'''
