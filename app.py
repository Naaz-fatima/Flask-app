from flask import Flask, render_template, request
from flask_alchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define a model for the data
class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    college = db.Column(db.String(100))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.form['name']
        college = request.form['college']
        
        # Create a new FormData object
        form_data = FormData(name=name, college=college)
        
        # Add the form data to the database
        db.session.add(form_data)
        db.session.commit()
    
    # Retrieve all form data from the database
    form_data_list = FormData.query.all()
    
    return render_template('index.html', form_data_list=form_data_list)

if __name__ == '__main__':
    # Create the database tables if they don't exist
    db.create_all()
    app.run()
