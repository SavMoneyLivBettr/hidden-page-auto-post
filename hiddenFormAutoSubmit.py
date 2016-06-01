from flask import Flask, request, render_template

app = Flask(__name__)


### Going to this link will create an invisible iframe that will cause a form to be submitted in the background ###
# "/" means it's the home directory
# This means that going the root page will go to this page unless this is changed
@app.route("/", methods=['GET', 'POST'])
def index(hiddenPage=None):
    # Change this when "/hidden" is changed in the hidden function below
    hiddenPage = "hidden"
    # Checks to see if the request was POST
    if request.method == "POST":
        # This is the info that the visible form will return back when submitted
        # Prints to console and goes to a page saying Form Submitted and showing what was submitted for now
        info = request.form['formInfo']
        print("Visible Form: " + info)
        return("<h1>Form Submitted</h1>\n<h2>" + info + "</h2>")
    return(render_template("ShownPage.html", hidden=hiddenPage))


# This is the page that the invisible iframe will open.  The data can be anything, and it will be used to submit in the form
# If /hidden is changed, makes sure to change the hiddenPage variable in the index function above
@app.route("/hidden", methods=['GET', 'POST'])
def hidden(data=None):
    # Opens the test_data_file.txt file and submits the contents into the form
    file = open("test_data_file.txt", "r")
    data = file.read()
    # Checks to see if the request is POST
    if request.method == "POST":
        # This is the info that the invisible form will return back once submitted.
        # For now, it simply prints it out to the console.
        info = request.form['formInfo']
        print("Hidden Form: " + info)
        # Returns Form Submitted just for debugging purposes, but also to avoid an infinite loop of submitting forms
        return("<h1>Form Submitted</h1>")
    return(render_template("HiddenPage.html", data=data))



if __name__ == "__main__":
    app.run(debug=True)