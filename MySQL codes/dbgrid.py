import pymysql
import time


class DbGrid:
    '''Class of database for grid disturbance records.'''
    db = ''
    host = '127.0.0.1'
    user = ''
    passwd = ''
    port = 3306
    charset = "utf8"

    def __init__(self, db, host, user, passwd, port=3306, charset="utf8"):
        '''Initialization of the class'''
        self.db = db  # name of database
        self.host = host  # static IP adress of MySQL server
        self.user = user  # username
        self.passwd = passwd  # password
        self.port = port  # port of IP (optional)
        self.charset = charset  # data format (optional)
        print("Class initialized.")

    def connect(self):
        try:
            conn = pymysql.connect(
                self.host, self.user, self.passwd,
                self.db, port=self.port, charset=self.charset)
            # print("Connection established.")
            return conn
        except pymysql.err.OperationalError as e:
            if str(e)[1:5] == '1045':
                print(f'Incorrect username or password.')
            elif str(e)[1:5] == '1044':
                print(f'Database {self.db} does not exist.')
            elif str(e)[1:5] == '2003':
                print(f'Can\'t connect to MySQL server on {self.host}.')
            else:
                print(f"Error : {e}")
            return False

    def init_all(self):
        '''Create all four new tables'''
        conn = self.connect()
        if type(conn) == 'bool':
            return
        else:
            c = conn.cursor()
        try:
            c.execute('''CREATE TABLE Disturbance
            (id   CHAR(16) PRIMARY KEY  NOT NULL,
            date  DATE  NOT NULL,
            time  TIME  NOT NULL)''')
            print("Table DISTURBANCE created successfully.")
        except pymysql.err.InternalError as e:
            print(f"Error : {e}")

        try:
            c.execute('''CREATE TABLE Fault
            (serial INTEGER PRIMARY KEY NOT NULL,
            ref  CHAR(16)  NOT NULL,
            ctype TEXT,
            voltage TEXT NOT NULL,
            ground TEXT NOT NULL,
            ownarea TEXT NOT NULL,
            cfsd TEXT NOT NULL,
            ftype TEXT NOT NULL,
            primar TEXT NOT NULL,
            temporary TEXT NOT NULL,
            itmt TEXT NOT NULL,
            cause TEXT NOT NULL,
            repair TEXT);''')
            print("Table FAULT created successfully.")
        except pymysql.err.InternalError as e:
            print(f"Error : {e}")

        try:
            c.execute('''CREATE TABLE Outage
            (unit  TEXT  NOT NULL,
            fault  INT  NOT NULL,
            type TEXT NOT NULL,
            ens TEXT NOT NULL,
            interrup TEXT NOT NULL,
            discon TEXT NOT NULL,
            reclos TEXT NOT NULL,
            duration TEXT NOT NULL);''')
            print("Table OUTAGE created successfully.")
        except pymysql.err.InternalError as e:
            print(f"Error : {e}")

        try:
            c.execute('''CREATE TABLE Interruption
            (delivery TEXT NOT NULL,
            ref  CHAR(16)  NOT NULL,
            duration TEXT NOT NULL);''')
            print("Table INTERRUPTION created successfully.")
        except pymysql.err.InternalError as e:
            print(f"Error : {e}")

        conn.commit()
        c.close()
        conn.close()

    def del_all(self):
        '''Delete all four tables'''
        conn = self.connect()
        if type(conn) == 'bool':
            return
        else:
            c = conn.cursor()
        for i in ['Disturbance', 'Fault', 'Outage', 'Interruption']:
            try:
                c.execute(f'''DROP TABLE {i};''')
                print(f"Table {i} deleted successfully.")
            except pymysql.err.InternalError as e:
                print(f"Error : {e}")

        conn.commit()
        c.close()
        conn.close()

    def get_info(self, tb):
        '''Get number of rows of a table'''
        sql1 = f"ANALYZE TABLE {tb};"
        sql2 = f"select TABLE_ROWS from \
              information_schema.TABLES WHERE\
              table_schema = 'piche' and table_name like '{tb}';"
        conn = self.connect()
        if type(conn) == 'bool':
            return
        c = conn.cursor(pymysql.cursors.DictCursor)
        # c = conn.cursor()
        c.execute(sql1)
        c.execute(sql2)
        result = c.fetchall()
        conn.commit()
        c.close()
        conn.close()
        return result[0]['TABLE_ROWS']

    def insert_disturbance(self, disturb):
        '''
        Insert a disturbance into the database.
        disturb is a list : [date("%Y-%m-%d"), time("%H:%M:%S")]
        Disturbance index will be automatically generated
        As 'YYYY-current number of rows'
        '''
        # get new id
        dist_nr = self.get_info('disturbance') + 1
        year = time.strftime("%Y", time.localtime())
        dist_id = year + '-' + str(dist_nr)
        disturb.insert(0, dist_id)
        # Conection
        conn = self.connect()
        if type(conn) == 'bool':
            return
        # Insertion
        c = conn.cursor()
        try:
            c.execute(f"INSERT INTO DISTURBANCE(id,date,time) \
                      VALUES {tuple(disturb)}")
            print(f"Disturbance {disturb} added.")
        except pymysql.err.IntegrityError as e:
            print(f"Error : {e}")
        # Update
        conn.commit()
        c.close()
        conn.close()

    def insert_fault(self, disturb, fault):
        '''
        Insert a fault into the database.
        fault is a list : [ctype, voltage, ground, ownarea, cfsd,
                           ftype, primar, temporary, cause, repair]
        Fault index will be automatically generated.
        '''
        # get new id
        fault_nr = self.get_info('fault') + 1
        # Conection
        conn = self.connect()
        if type(conn) == 'bool':
            return
        # Insertion
        c = conn.cursor()
        sql_command = (fault_nr, disturb) + fault[:]
        try:
            c.execute(f"INSERT INTO FAULT(serial, \
                ref, ctype, voltage, ground, ownarea, cfsd, ftype,\
                primar, temporary, itmt, cause, repair) VALUES {sql_command}")
            print(f"Fault {[fault_nr, disturb]} added successfully.")
        except (pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
            print(f"Error : {e}")
        # Update
        conn.commit()
        c.close()
        conn.close()

    def insert_outage(self, outage):
        '''
        Insert an outage into the database.
        'outage' is a list : [unit, fault, type, ens,
                              interrup, discon, reclos, duration]
        Fault index in the list should be already added to the database.
        '''
        # Verification
        fault_nr = self.get_info('fault')
        if outage[1] not in range(fault_nr):
            print(f"{outage[1]} is not a valid fault serial number.")
            return
        # Conection
        conn = self.connect()
        if type(conn) == 'bool':
            return
        # Insertion
        c = conn.cursor()
        try:
            c.execute(f"INSERT INTO outage(unit, fault, type, ens, \
                interrup, discon, reclos, duration) VALUES {tuple(outage)}")
            print(f"Outage {outage[:2]} added successfully.")
        except (pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
            print(f"Error : {e}")
        # Update
        conn.commit()
        c.close()
        conn.close()


piche = DbGrid('Piche', '127.0.0.1', 'thomas', 'Dubard.113')
# piche.init_all()  # OK
# piche.del_all()  # OK

# dtbt = [time.strftime("%Y-%m-%d", time.localtime()),
#         time.strftime("%H:%M:%S", time.localtime())]
# piche.insert_disturbance(dtbt)  # OK

'''  # OK
ft = [('Line', '400 kV', 'Own', 'Component', 'Direct earthed',
       'Single-phase earth fault', 'Primary', 'Temporary',
       'Non-intermittent', 'Lightning', '0 min'),
      ('Circuit breakers', '400 kV', 'Own', 'Component',
       'Direct earthed', 'Function failing to occur',
       'Secondary/latent fault', 'Permanent',
       'Non-intermittent', 'Technical equipment', '48 h 0 min')
      ]

for fault in ft:
    piche.insert_fault('2020-2', fault)
'''

ot = [('Line X-Y', 1, 'Line', '0 MWh', '0 min', 'Automatically',
       'Manually after repair', '48 h 0 min'),
      ('Line Y-Z', 2, 'Line', '0 MWh', '0 min', 'Automatically',
       'Manually after inspection', '0 h 45 min'),
      ('Busbar Y', 2, 'Busbar', '0 MWh', '0 min', 'Automatically',
       'Manually after inspection', '0 h 45 min'),
      ('Power transformer Y', 2, 'Power transformer', '7 MWh', '0 min',
       'Automatically', 'Manually after inspection', '0 h 45 min')
      ]

for outage in ot:
    piche.insert_outage(outage)
