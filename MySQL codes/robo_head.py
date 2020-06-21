import pymysql
from user_info import *


def db_init(db):
    try:
        conn = pymysql.connect(host, user, passwd, db,
                               port=port, charset="utf8")
        print("Access granted.")
        return 1
    except pymysql.err.OperationalError as e:
        print(f"Error : {e}")
        return 0


def db_init_all(db):
    conn = pymysql.connect(host, user, passwd, db, port=port, charset="utf8")
    c = conn.cursor()
    c.execute('''CREATE TABLE DISTURBANCE
        (id   CHAR(16) PRIMARY KEY  NOT NULL,
        date  TEXT  NOT NULL,
        time  TEXT  NOT NULL)''')
    print("Table DISTURBANCE created successfully.")
    conn.commit()

    # serial INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
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

    c.execute('''CREATE TABLE outage
        (unit  TEXT  NOT NULL,
        fault  INT  NOT NULL,
        type TEXT NOT NULL,
        ens TEXT NOT NULL,
        interrup TEXT NOT NULL,
        discon TEXT NOT NULL,
        reclos TEXT NOT NULL,
        duration TEXT NOT NULL);''')
    print("Table OUTAGE created successfully.")

    c.execute('''CREATE TABLE interruption
        (delivery TEXT NOT NULL,
        ref  CHAR(16)  NOT NULL,
        duration TEXT NOT NULL);''')
    print("Table INTERRUPTION created successfully.")

    conn.commit()
    conn.close()
    print("Database " + name + " created successfully.")


def db_insert_disturbance(db, disturb):
    conn = pymysql.connect(host, user, passwd, db, port=port, charset="utf8")
    c = conn.cursor()

    c.execute(f"INSERT INTO DISTURBANCE(id,date,time) \
        VALUES {tuple(disturb)}")

    conn.commit()
    print("Disturbance records added successfully.")
    conn.close()


def db_insert_fault(db, disturb, fault):
    conn = pymysql.connect(host, user, passwd, db, port=port, charset="utf8")
    c = conn.cursor()
    '''
    sql_command = "INSERT INTO FAULT(serial, \
            ref, ctype, voltage, ground, ownarea, cfsd, \
            ftype, primar, temporary, cause, repair) VALUES (NULL"
    for item in fault:
        sql_command = sql_command + ", '" + item + "'"
    c.execute(sql_command + ")")
    '''
    sql_command = (fault[0], disturb) + fault[1:]
    c.execute(f"INSERT INTO FAULT(serial, \
            ref, ctype, voltage, ground, ownarea, cfsd, ftype,\
            primar, temporary, itmt, cause, repair) VALUES {sql_command}")

    conn.commit()
    print("Fault records added successfully.")
    conn.close()


def db_insert_outage(db, outage):
    conn = pymysql.connect(host, user, passwd, db, port=port, charset="utf8")
    c = conn.cursor()

    c.execute(f"INSERT INTO outage(unit, fault, type, ens, \
                interrup, discon, reclos, duration) VALUES {tuple(outage)}")

    conn.commit()
    print("Outage records added successfully.")
    conn.close()


def db_insert_interruption(db, disturb, interrupt):
    conn = pymysql.connect(host, user, passwd, db, port=port, charset="utf8")
    c = conn.cursor()

    sql_command = (interrupt[0], disturb, interrupt[1])
    c.execute(f"INSERT INTO interruption(delivery, \
                ref, duration) VALUES {sql_command}")

    conn.commit()
    print("Interruption records added successfully.")
    conn.close()


def db_select_disturbance(db, disturb):
    conn = pymysql.connect(host, user, passwd, db, port=port, charset="utf8")
    c = conn.cursor()
    res = {}

    sql_command = f"SELECT * FROM disturbance WHERE id = '{disturb}'"
    c.execute(sql_command)
    for dist in c.fetchall():
        res['disturbance'] = dist

    sql_command = f"SELECT * FROM fault WHERE ref = '{disturb}'"
    # sql_command = f"SELECT * FROM fault"
    c.execute(sql_command)
    res['fault'] = []
    for fault in c.fetchall():
        res['fault'].append(fault)
        # res.append(fault)

    res['outage'] = []
    for i in range(len(res)-1):
        sql_command = f"SELECT * FROM outage WHERE \
                     fault = {res['fault'][i][0]}"
        c.execute(sql_command)
        for outage in c.fetchall():
            res['outage'].append(outage)
            # res.append(outage)

    res['interruptions'] = []
    sql_command = f"SELECT * FROM interruption WHERE ref = '{disturb}'"
    c.execute(sql_command)
    for interruption in c.fetchall():
        res['interruptions'].append(interruption)
        # res.append(interruption)

    return res
