import pymysql
import time
import hashlib


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
            repair TIME);''')
            print("Table FAULT created successfully.")
        except pymysql.err.InternalError as e:
            print(f"Error : {e}")

        try:
            c.execute('''CREATE TABLE Outage
            (unit  TEXT  NOT NULL,
            fault  INT  NOT NULL,
            type TEXT NOT NULL,
            ens TEXT NOT NULL,
            interrup TIME NOT NULL,
            discon TEXT NOT NULL,
            reclos TEXT NOT NULL,
            duration TIME NOT NULL);''')
            print("Table OUTAGE created successfully.")
        except pymysql.err.InternalError as e:
            print(f"Error : {e}")

        try:
            c.execute('''CREATE TABLE Interruption
            (delivery TEXT NOT NULL,
            ref  CHAR(16)  NOT NULL,
            duration TIME NOT NULL);''')
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
        if outage[1] not in range(fault_nr+1):
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
                interrup, discon, reclos, duration)\
                VALUES {tuple(outage)}")
            print(f"Outage {outage[:2]} added successfully.")
        except (pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
            print(f"Error : {e}")
        # Update
        conn.commit()
        c.close()
        conn.close()

    def insert_interruption(self, disturb, itrpt):
        '''
        Insert an outage into the database.
        'disturb' is the index of the disturbance associated.
        'itrpt' is a list : [unit, fault, type, ens,
                              interrup, discon, reclos, duration]
        Disturbance index in the list should be already added to the database.
        '''
        # Conection
        conn = self.connect()
        if type(conn) == 'bool':
            return
        c = conn.cursor()
        # Verification
        try:
            sql_command = f"SELECT * FROM disturbance WHERE id = '{disturb}'"
            c.execute(sql_command)
            # for dist in c.fetchall():
            if len(c.fetchall()) > 0:
                pass
            else:
                print(f"No such disturbance {disturb} found.")
                return
        except (pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
            print(f"Error : {e}")
            return
        # Insertion
        try:
            sql_command = (interrupt[0], disturb, interrupt[1])
            c.execute(f"INSERT INTO interruption(delivery, \
                      ref, duration) VALUES {sql_command}")
            print(f"Interruption {itrpt} added successfully.")
        except (pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
            print(f"Error : {e}")
        # Update
        conn.commit()
        c.close()
        conn.close()
