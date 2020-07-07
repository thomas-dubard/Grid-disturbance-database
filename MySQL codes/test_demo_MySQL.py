import pymysql
import time
from dbgrid import *


# =========================
# This script is used for demonstrating the
# code usage to manipulate the MySQL database
#
# ATTENTION
# To sucessfully launch the program, it is necessory
# that MySQL server has been installed locally or remotely,
# and the database itself has been created.
# =========================

root_user = 'Edward.Elric'  # Please fill in your root username
root_pswd = 'Elric'  # Please fill in your root password
database_host = '127.0.0.1'  # Please replace it by the adress of your database
database_name = 'Piche'  # Please replace it by the name of your database


def main():
    '''
    Here is the main function for the test.
    '''
    # Define the entrance of database
    database = DbGrid(database_name, database_host, root_user, root_pswd)

    print('Verify the connection :')
    print(type(database.connect()), '\n')

    print('Try a wrong username / password :')
    fake_db = DbGrid(database_name, database_host, root_pswd, root_user)
    print(fake_db.connect(), '\n')

    print('Try a wrong name of database :')
    fake_db = DbGrid('fakemysql', database_host, root_user, root_pswd)
    print(fake_db.connect(), '\n')

    print('Try a wrong adress of database :')
    fake_db = DbGrid(database_name, '256.256.256.256', root_user, root_pswd)
    print(fake_db.connect(), '\n')

    print('Add a new user with limited authority :')
    database.create_user('Piche', 'Alfonse.Elric', 'Elric')
    mdm = DbGrid('Piche', '127.0.0.1', 'Alfonse.Elric', 'Elric')
    print('Test the connection with the created account')
    print(type(mdm.connect()), '\n')

    print('Initialize 4 tables with limited user :')
    # if this function is not launched the first time, we expect 4 errors
    try:
        mdm.init_all()
    except RuntimeError as e:
        print(e)
    print('\n')

    print('Initialize 4 tables with root user :')
    # if this function is not launched the first time, we expect 4 errors
    try:
        database.init_all()
    except RuntimeError as e:
        print(e)
    print('\n')

    print('Insert a disturbance record :')
    # generate some random disturbance
    dtbt = [time.strftime("%Y-%m-%d", time.localtime()),
            time.strftime("%H:%M:%S", time.localtime())]
    database.insert_disturbance(dtbt)
    print('Check the table \'disturbance\' :')
    print(database.fetch_table('disturbance'))
    print('Current number of records in disturbance : ',
          database.get_info('disturbance'), '\n')

    print('Insert a wrong disturbance record :')
    dtbt2 = ['20200630', 'Disturbance']
    database.insert_disturbance(dtbt2)
    print('Current number of records in disturbance : ',
          database.get_info('disturbance'), '\n')

    print('Insert some fault records :')
    # generate some faults
    ft = [('Busbars', '400 kV', 'Own', 'Component', 'Direct earthed',
           'Single-phase earth fault', 'Primary', 'Temporary',
           'Non-intermittent', 'Lightning', '00:00:00'),
          ('Circuit breakers', '400 kV', 'Own', 'Component',
           'Direct earthed', 'Function failing to occur',
           'Secondary/latent fault', 'Permanent',
           'Non-intermittent', 'Technical equipment', '48:00:00')
          ]
    for fault in ft:
        database.insert_fault('2020-1', fault)
    print(database.fetch_table('fault'))
    print('Current number of records in fault : ',
          database.get_info('fault'), '\n')

    print('Insert a wrong fault record :')
    ft2 = ('Circuit', '400 kV', 'Own', 'Component',
           'Direct earthed', 'Function failing to occur',
           'Secondary/latent fault', 'Permanent',
           'Non-intermittent', 'Technical equipment', '48:00:00')
    database.insert_fault('2020-1', ft2)
    database.insert_fault('2019-1', ft[0])
    print('Current number of records in fault : ',
          database.get_info('fault'), '\n')

    print('Insert some outage records :')
    # generate some outages
    ot = [('Line X-Y', 1, 'Cable', '0 MWh', '00:00:00', 'Automatically',
           'Manually after repair', '48:00:00'),
          ('Line Y-Z', 2, 'Cable', '0 MWh', '00:00:00', 'Automatically',
           'Manually after inspection', '00:45:00'),
          ('Busbar Y', 1, 'Bushbar', '0 MWh', '00:00:00', 'Automatically',
           'Manually after inspection', '00:45:00'),
          ('Power transformer Y', 2, 'Power transformer', '7 MWh', '00:00:00',
           'Automatically', 'Manually after inspection', '00:45:00')
          ]
    for outage in ot:
        database.insert_outage(outage)
    print('Check the table \'outage\' :')
    print(database.fetch_table('outage'))
    print('Current number of records in outage : ',
          database.get_info('outage'), '\n')

    print('Insert some wrong outage records :')
    ot2 = ('Power transformer Y', 2, 'Lost component', '7 MWh', '00:00:00',
           'Automatically', 'Manually after inspection', '00:45:00')
    database.insert_outage(ot2)
    ot3 = ('Line Y-Z', 998, 'Cable', '0 MWh', '00:00:00', 'Automatically',
           'Manually after inspection', '00:45:00')
    database.insert_outage(ot3)
    print('Current number of records in outage : ',
          database.get_info('outage'), '\n')

    print('Insert an interruption record :')
    ip = ('Power transformer', '00:45:00')
    database.insert_interruption('2020-1', ip)
    print(database.fetch_table('interruption'))
    print('Current number of records in interruption : ',
          database.get_info('interruption'), '\n')

    print('Insert a wrong interruption record :')
    ip = ('Power transformer', '00:45:00')
    database.insert_interruption('1970-1', ip)
    print('Current number of records in interruption : ',
          database.get_info('interruption'), '\n')

    print('Select a disturbation with all its associating records : ')
    res = database.select_disturbance('2020-1')
    print('Disturbance :\n', res['disturbance'])
    print('Fault :\n', res['fault'])
    print('Outage :\n', res['outage'])
    print('Interruption :\n', res['interruption'], '\n')

    print('Fetch the table of outages : ')
    print(database.fetch_table('outage'), '\n')

    print('Delete all tables with limited account : ')
    try:
        mdm.del_all()
    except RuntimeError as e:
        print(e)
    print('\n')

    print('Delete all tables with root account : ')
    try:
        database.del_all()
    except RuntimeError as e:
        print(e)
    print('\n')

    print('Delete user with limited authority :')
    database.remove_user('Alfonse.Elric', 'localhost')
    print('Test the connection with the removed account : ')
    print(mdm.connect(), '\n')


if __name__ == "__main__":
    # execute only if run as a script
    main()
