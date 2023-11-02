# Hello guys now lets jump to Day-2 As we have completed Day-1 basics

from flask import Flask

app=Flask(__name__)



# Now in this day-2 lets try to add some h1 tag in return and lets run the code.

@app.route('/')
def hello():

# h1 tag refers to heading one tag
    return "<h1>hello world this Akshay Kumar</h1>"


# now lets try with h4 tag will it work lets checkout 
# In order to run this in browser after past of ip number make sure u have given (/h4).
# example:- http://127.0.0.2:5000/h4 this only refers try to past your ip server ip number  

# this route is used to switch between the pages of the function

@app.route('/h4')
def tagchange():
    return "<h4>hello world this h4 tag</h4>"


if __name__=='__main__':

    # This below code is used for running the app 
    # to run the this file use and command u have used in Day-1  
    app.run(debug=True)

