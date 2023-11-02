# Hello guys now lets jump to Day-3 hope u liked my Day-2 class

# DAY-3

# Importing the libary 
# render_template will help to access the html file from templates folder
from flask import Flask,render_template

# Now lets call the object or instance from  Flask class
app=Flask(__name__)


# Now lets create decorator for above one we use route for going to needed page

@app.route('/home') # This (/home) indicates the page you want to move 
def home():
    return render_template('index.html')# here we have given file name with render_template


# usually we use this because after import of libraries code will excute from this line
if __name__=='__main__':
     # This will run the the flask app by below line of code  
    app.run(debug=True) # debug=true will indicate run time changes are allowed 