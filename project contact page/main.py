from flask import Flask,render_template,request 
import requests
import mysql.connector as conn
from db_connect import insert_table

mydb=conn.connect(host="localhost",user="root",password="12345678",database="Contact_Page")
print(mydb)
cursor=mydb.cursor()
# dataBaseName="Contact_Page"
customer_comments="contact"
# create_db(cursor,dataBaseName)
# create_table(cursor,customer_comments)

app = Flask(__name__)  
  
@app.route('/',methods=['POST', 'GET'])      
def index():
    return render_template('index.html')


@app.route("/review",methods=['POST', 'GET'])
def results():
    if request.method=="POST":
        reviews=[]
        first_name = request.form["first_name"]
        last_name =  request.form["last_name"]
        contact_number = request.form["contact_number"]
        e_mail = request.form["e_mail"]
        place=request.form["place"]


        mydict={'First_Name':first_name,"Last_Name":last_name,"Contact_Number":contact_number,"E_mail":e_mail,"Place":place}
        reviews.append(mydict)
        insert_query=f"INSERT INTO {customer_comments}(First_Name,Last_Name,Contact_Number,E_mail,Place) VALUES (%(First_Name)s, %(Last_Name)s, %(Contact_Number)s, %(E_mail)s, %(Place)s);"  
        cursor.executemany(insert_query,reviews)
        mydb.commit() 
    
        
        return render_template('results.html',reviews=reviews)


        

    else:
        return render_template('index.html')        

  
if __name__=='__main__':
   app.run(debug=True)
