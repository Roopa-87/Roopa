import cx_Oracle
import csv
demo=cx_Oracle.Connection('system/manager@mother')
cursor=demo.cursor()


def table():
    query='create table aravind08(id number(4) primary key,name varchar(10))'
    cursor.execute(query)
    print('Table created')
#table()
# def insert():
#     query='''insert into aravind08 values(04,'Aravind')'''
#     query='''insert into aravind08 values(02,'Madhu')'''
#     query='''insert into aravind08 values(03,'Dhamu')'''
#     cursor.execute(query)
   
#     demo.commit()
#     print("Values Inserted")
# insert()
def insert_record(sid,name):
    record={'id':str(sid),'name':name}
    query='insert into aravind08 values(:id,:name)'
    cursor.execute(query,record)
    demo.commit()
    print("Values inserted")
# insert_record(4,'Madhu')
# insert_record(5,'Dhamu')
# insert_record(6,'Ganesh')
def read_record():
    query='Select * from aravind08'
    cursor.execute(query)
    record=cursor.fetchall()
    with open('records.csv','w',newline='')as csvfile:
        pointer=csv.writer(csvfile)
        pointer.writerow(['id','name'])
        for row in record:
            pointer.writerow(row)

   
read_record()
def get_record(sid):
    record={'id':str(sid)}
    query='Select * from aravind08 where id =:id'
    cursor.execute(query,record)
    records=cursor.fetchall()
    for row in records:
        print (row)
#get_record(1)
def update_record():
    query='''Update aravind08 set name='Rajesh' where id=1'''
    cursor.execute(query)
    demo.commit()
    print('update')
#update_record()
def delect_record():
    query='Delete aravind08 where id=1'
    cursor.execute(query)
    demo.commit()
    print("Delected")
#delect_record()
def trucate_record():
    query='truncate table aravind08'
    cursor.execute(query)
    demo.commit()
    print("Truncated")
#trucate_record()
def drop():
    query='drop table aravind08'
    cursor.execute(query)
    print("Droped")
#drop()
def get_table():
    query='Select * from tab'
    cursor.execute(query)
    table=cursor.fetchall()
    for tables in table:
        print(tables)
#get_table()