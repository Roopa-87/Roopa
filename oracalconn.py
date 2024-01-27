import cx_Oracle
import csv
conn=cx_Oracle.Connection('system/manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table mcakoushick(
    id number (2) primary key,
    name varchar(45)
    )
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cur.execute("insert into mcakoushick(id,name) values(:id,:name)",record)
    conn.commit()
#insertrecord(2,'vidhya')   
#insertrecord(3,'pandu')
#insertrecord(4,'sudhamani')
#insertrecord() 
def read_records():
    query ='select * from mcakoushick'
    cur.execute(query)
    records=cur.fetchall()
    #with open('records.csv','w',newlibne='') as csvfile:
        #data=csv.writer(csvfile)
        #data=writerow(['id','name'])
        #for row in records:
        # data.writerow(row)
#read_records()
def fetch_record(sid):
    record ={'id':str(sid)}
    query='select * from mcakoushick where id=:id'
    cur.execute(query,record)
    record=cur.fetchall()
    for row in record:
        print(row)

def update_name(sid):
    fetch_record(sid)
    name=input('enter  new name to update:-')
    record={'id':str(sid),'name':name}
    query='update mcakoushick set name=:name where  id= :id'
    cur.execute(query,record)
    conn.commit()
    #fetch_record(sid)
def delete_record(sid):
    fetch_record(sid)
    name=input('enter  new name to update:-')
    record={'id':str(sid),'name':name}
    query='delete from mcakoushick  where  id= :id'
    cur.execute(query,record)
    conn.commit()
    #fetch_record(sid)
def truncate():
        query='truncate table mcakoushick'
        cur.execute(query)
def insert_from_csv():
    with open('records.csv','r')as csvfile:
        data=csv.reader(csvfile)
        daat=list(data)   
        for row in range(1,len(data)):
            insertrecord(*data[row])









   