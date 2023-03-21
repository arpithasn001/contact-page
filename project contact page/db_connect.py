# def create_db(cursor,dataBaseName):
#     db=f"create database {dataBaseName}"
#     cursor.execute(db)

# def create_table(cursor,customer_comments):
#     tb=f"CREATE TABLE IF NOT EXISTS {customer_comments} (First_Name varchar(1000),Last_Name varchar(100),Contact_Number varchar(30),E_mail varchar(400),Place varchar(200));"
#     cursor.execute(tb)

def insert_table(cursor,customer_comments,lst):
    insert_query=f"INSERT INTO {customer_comments}(First_Name,Last_Name,Contact_Number,E_mail,Place) VALUES (%(First_Name)s, %(Last_Name)s, %(Contact_Number)s, %(E_mail)s, %(Place)s);"  
    cursor.executemany(insert_query,lst)     