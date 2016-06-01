This was built using the Python microframework Flask.  Flask is very good when it comes to web development, and makes things really easy.

There are two HTML pages inside the templates folder.  One is ShownPage.html and the other is HiddenPage.html
ShowPage.html contains an iframe with no width, height, or borders, making it invisible, and contains HiddenPage.

HiddenPage has a form, with some Javascript code attached, that will cause the form to be submitted upon the page loading.

The main logic of this entire thing is in hiddenFormAutoSubmit.py.
It takes care of all the requests, and allows data to be passed through the HTML.
Everything is commented and explained in the code, and changing things around should be pretty easy.

The data that is passed through the forms is very easy to change.  Simply read from files, a database, etc., and it can be implemented within the logic of the script.
Implementing your idea of getting the user's IP Address will be straightforward at this point.
For now, the invisible form is reading data from test_data_file.txt, which for now just contains a line of text.

To run the server, and access the page using your web browser, make sure all of the necessary files are present, and that you have Flask.
Run the script,and go to 127.0.0.1:5000 on your web browser to access the local server, and to view the site.

Everything else is explained through the comments in the source code.  If you have any other questions, please feel free to email me at jacobsskowronek@gmail.com.