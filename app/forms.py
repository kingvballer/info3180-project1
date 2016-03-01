from flask.ext.wtf import Form
from wtforms.fields import TextField, FileField, IntegerField, SubmitField, SelectField
from wtforms.validators import Required, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired

class userForm(Form):
    firstname = TextField('FirstName', validators = [Required()])
    lastname = TextField('LastName', validators = [Required()])
    age = TextField('Age', validators = [Required()])
    sex = SelectField('Sex', validators = [Required()], choices = [('M', 'Male'),('F', 'Female')])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    #submit = SubmitField('Submit')
    
