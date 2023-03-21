from flask import Flask,render_template,request 
import requests


app = Flask(__name__)  
  
@app.route('/',methods=['POST', 'GET'])      
def index():
    return render_template('index.html')


@app.route("/review",methods=['POST', 'GET'])
def results():
    if request.method=="POST":
        reviews=[]

        
        

        
        try:

            first_name = request.form["first_name"]
                    
        except:

            print('first name not found')

        try:
            last_name =  request.form["last_name"]
        except:
            print('lastname not found')    

        try:
            contact_number = request.form["contact_number"]
        except:
            print('contact not found')    

        try:
            e_mail = request.form["e_mail"]
        except:
            print('email not found')    


        

        


        mydict={'First_Name':first_name,"Last_Name":last_name,"Contact_Number":contact_number,"E_mail":e_mail}
        reviews.append(mydict)
    
        
        return render_template('results.html',reviews=reviews)


    


    else:
        return render_template('index.html')        

  
if __name__=='__main__':
   app.run(debug=True)

