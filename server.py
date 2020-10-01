from flask import Flask, render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)# The "@" decorator associates this route with the function immediately following

@app.route('/')
def hello_world(boxcountx=8,boxcounty=8):
    return render_template('index.html',boxcountx = boxcountx,boxcounty = boxcounty)


@app.route('/<int:boxcountx>/')
def phrase(boxcountx,boxcounty= 8):
    return render_template('index.html',boxcountx = boxcountx,boxcounty = boxcounty)

@app.route('/<int:boxcountx>/<int:boxcounty>/')
def catch2phrase(boxcountx,boxcounty):
    return render_template('index.html',boxcountx = boxcountx,boxcounty = boxcounty)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Well now you dun 404'd.  Probably shouldn't be here.  Run along."

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
