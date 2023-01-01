import psycopg2
import random
import string
import datetime


columns = ['val0', 'val1', 'val2', 'val3', 'val4', 'val5', 'val6', 'val7', 'val8', 'val9', 'val10', 'val11', 'val12', 'val13', 'val14', 'val15', 'val16', 'val17', 'val18', 'val19', 'val20', 'val21', 'val22', 'val23', 'val24', 'val25', 'val26', 'val27', 'val28', 'val29', 'val30', 'val31', 'val32', 'val33', 'val34', 'val35', 'val36', 'val37', 'val38', 'val39', 'val40', 'val41', 'val42', 'val43', 'val44', 'val45', 'val46', 'val47', 'val48', 'val49', 'val50', 'val51', 'val52', 'val53', 'val54', 'val55', 'val56', 'val57', 'val58', 'val59', 'val60', 'val61', 'val62', 'val63', 'val64', 'val65', 'val66', 'val67', 'val68', 'val69', 'val70', 'val71', 'val72', 'val73', 'val74', 'val75', 'val76', 'val77', 'val78', 'val79', 'val80', 'val81', 'val82', 'val83', 'val84', 'val85', 'val86', 'val87', 'val88', 'val89', 'val90', 'val91', 'val92', 'val93', 'val94', 'val95', 'val96', 'val97', 'val98', 'val99', 'val100', 'val101', 'val102', 'val103', 'val104', 'val105', 'val106', 'val107', 'val108', 'val109', 'val110', 'val111', 'val112', 'val113', 'val114', 'val115', 'val116', 'val117', 'val118', 'val119', 'val120', 'val121', 'val122', 'val123', 'val124', 'val125', 'val126', 'val127', 'val128', 'val129', 'val130', 'val131', 'val132', 'val133', 'val134', 'val135', 'val136', 'val137', 'val138', 'val139', 'val140', 'val141', 'val142', 'val143', 'val144', 'val145', 'val146', 'val147', 'val148', 'val149', 'val150', 'val151', 'val152', 'val153', 'val154', 'val155', 'val156', 'val157', 'val158', 'val159', 'val160', 'val161', 'val162', 'val163', 'val164', 'val165', 'val166', 'val167', 'val168', 'val169', 'val170', 'val171', 'val172', 'val173', 'val174', 'val175', 'val176', 'val177', 'val178', 'val179', 'val180', 'val181', 'val182', 'val183', 'val184', 'val185', 'val186', 'val187', 'val188', 'val189', 'val190', 'val191', 'val192', 'val193', 'val194', 'val195', 'val196', 'val197', 'val198', 'val199', 'val200', 'val201', 'val202', 'val203', 'val204', 'val205', 'val206', 'val207', 'val208', 'val209', 'val210', 'val211', 'val212', 'val213', 'val214', 'val215', 'val216', 'val217', 'val218', 'val219', 'val220', 'val221', 'val222', 'val223', 'val224', 'val225', 'val226', 'val227', 'val228', 'val229', 'val230', 'val231', 'val232', 'val233', 'val234', 'val235', 'val236', 'val237', 'val238', 'val239', 'val240', 'val241', 'val242', 'val243', 'val244', 'val245', 'val246', 'val247', 'val248', 'val249', 'val250', 'val251', 'val252', 'val253', 'val254', 'val255', 'val256', 'val257', 'val258', 'val259', 'val260', 'val261', 'val262', 'val263', 'val264', 'val265', 'val266', 'val267', 'val268', 'val269', 'val270', 'val271', 'val272', 'val273', 'val274', 'val275', 'val276', 'val277', 'val278', 'val279', 'val280', 'val281', 'val282', 'val283', 'val284', 'val285', 'val286', 'val287', 'val288', 'val289', 'val290', 'val291', 'val292', 'val293', 'val294', 'val295', 'val296', 'val297', 'val298', 'val299', 'val300']


def createTable():
    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a table
    sql = '''CREATE table data(
            timestamp timestamp,
            ID serial primary key,
            ''';

    for i in range(300):
        sql += "val"+str(i) + " varchar(10),\n" 

    sql += "val300 varchar(10)\n)"

    #print([i[0] for i in [a.split() for a in sql.splitlines()]])
    #Creating a database
    cursor.execute(sql)
    #print("Database created successfully........")

    #Closing the connection
    conn.close()

def populate_table():
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    dt = datetime.datetime(2010, 12, 1)
    end = datetime.datetime(2010, 12, 2, 23, 59, 59)
    step = datetime.timedelta(seconds=2)

    result = []

    while dt < end:
        a = ""
        b = ""
        a = ""
        mySet = set()
        mySet.add(random.choice(columns))
        vals = []
        c = random.randint(0, 15)
        for i in range(c):
            mySet.add(random.choice(columns))
        
        for x in mySet:
            vals.append(random.randint(0, 999999))
            a += "" + str(x) + ", "
        a = a[:len(a)-2]
        for x in vals:
            b += "'" + str(x) + "', "
        b = b[:len(b)-2]

        sql = "INSERT INTO data(timestamp, "+ a + ") VALUES ('"+ str(dt) + "', "+ b + ")"
        #print(sql)
        cursor.execute(sql)
        dt += step

    #Closing the connection
    conn.close()

    return

def createTable_2():
    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a table
    sql = '''CREATE table data2(
            timestamp timestamp,
            ID serial primary key,
            sensor_name varchar(10),
            value varchar(10))
            ''';

    #Creating a database
    cursor.execute(sql)
    #print("Database created successfully........")

    #Closing the connection
    conn.close()

def populate_table2():
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Retrieving data
    cursor.execute('''SELECT * from data''')

    #Fetching 1st row from the table
    result = cursor.fetchall();

    for i in result:
        dt = result[0]
        i = i[2:]
        vals = []
        sensor_names = []
        for index, j in enumerate(i):
            if j != "None":
                vals.append(j)
                sensor_names.append("val"+str(index))

        for v, n in zip(vals, sensor_names):
            sql = "INSERT INTO data2(timestamp, sensor_name, value) VALUES ('"+str(dt) + "', '" + n + "', '"+ v + "')"
            cursor.execute(sql)
    print(result)

    #Closing the connection
    conn.close()

    return

populate_table2()
# createTable_2()