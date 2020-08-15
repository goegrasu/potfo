from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# @app.route('/<username>/<int:post_id>')
# def hello_username(username=None, post_id=None):
#     return render_template('./index.html', name=username, post_id=post_id)
#
# @app.route('/<username>')
# def hello_username(username=None):
#     return render_template('./index.html', name=username)
#
# @app.route('/')
# def hello_world():
#     return render_template('./index.html', name='')
#
# @app.route('/blog/2020/dogs')
# def blog():
#     return 'this is my dog'
#
# @app.route('/about.html')
# def about():
#     return render_template('./about.html')

@app.route('/')
@app.route('/<string:html_name>.html')
def pages(html_name='index'):
    return render_template(html_name+".html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html', 301)
        except:
            return 'did not save to database'
    else:
        return 'something went wrong try again'


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
         email = data["email"]
         subject = data["subject"]
         message = data["message"]
         csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
         csv_writer.writerow([email, subject, message])