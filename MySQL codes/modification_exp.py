from dbgrid import *

piche = DbGrid('Piche', '127.0.0.1', 'thomas', 'Dubard.113')

# piche.init_all()  # OK
# piche.del_all()  # OK

'''  # test code for insert_disturbance / OK
dtbt = [time.strftime("%Y-%m-%d", time.localtime()),
        time.strftime("%H:%M:%S", time.localtime())]
piche.insert_disturbance(dtbt)
'''

'''  # test code for insert_fault / OK
ft = [('Line', '400 kV', 'Own', 'Component', 'Direct earthed',
       'Single-phase earth fault', 'Primary', 'Temporary',
       'Non-intermittent', 'Lightning', '00:00:00'),
      ('Circuit breakers', '400 kV', 'Own', 'Component',
       'Direct earthed', 'Function failing to occur',
       'Secondary/latent fault', 'Permanent',
       'Non-intermittent', 'Technical equipment', '48:00:00')
      ]
for fault in ft:
    piche.insert_fault('2020-2', fault)
'''

'''  # test code for insert_outage / OK
ot = [('Line X-Y', 1, 'Line', '0 MWh', '00:00:00', 'Automatically',
       'Manually after repair', '48:00:00'),
      ('Line Y-Z', 2, 'Line', '0 MWh', '00:00:00', 'Automatically',
       'Manually after inspection', '00:45:00'),
      ('Busbar Y', 3, 'Busbar', '0 MWh', '00:00:00', 'Automatically',
       'Manually after inspection', '00:45:00'),
      ('Power transformer Y', 4, 'Power transformer', '7 MWh', '00:00:00',
       'Automatically', 'Manually after inspection', '00:45:00')
      ]
for outage in ot:
    piche.insert_outage(outage)
'''

'''  # test code for insert_interruption / OK
ip = [('Power transformer', '00:15:00')]
for interrupt in ip:
    piche.insert_interruption('2020-2', interrupt)
'''
