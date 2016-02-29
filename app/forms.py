from flask.ext.wtf import form
from wtforms.fields import TextField, FileField, IntegerField, SubmitField, SelectField
from wtforms.validators import Required, Allowed

class userForm(form):
    firstname = TextField('FirstName', validators = [Required()])
    lastname = TextField('LastName', validators = [Required()])
    age = TextField('Age', validators = [Required()])
    sex = SelectField('Sex', validators = [Required()], choices = [('M', 'Male'),('F', 'Female')])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')
    
    
    def validate_firstname(form, field):
        if len(field.data) < 1:
            raise ValidationError('Please enter your First Name')
            
    def validate_lastname(form, field):
        if len(field.data) < 1:
            raise ValidationError('Please enter your Last Name')
            
    def validate_age(form, field):
        if len(field.data) < 1:
            raise ValidationError('Please enter your Age')
            
    def validate_sex(form, field):
        if len(field.data) < 1:
            raise ValidationError('Please enter your Sex')
            
    