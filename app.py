# Now lets import Flask 

from flask import Flask

# Now lets call the object or instance from  Flask class

app=Flask(__name__)


# Now lets create decorator for above one we use route for going to needed page

@app.route('/') # This (/) indicates the page you want to move 

# Now create a fuction to show message when user enter to this page
def hello():
    return "hello everyone this our first flask web application"



# usually we use this because after import of libraries code will excute from this line
if __name__=='__main__':

    # This will run the the flask app by below line of code  
    app.run(debug=True )# debug=true will indicate run time changes are allowed  