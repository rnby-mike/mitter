from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mike'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in St Petersburg'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avatar movie was so cool!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avatar movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)