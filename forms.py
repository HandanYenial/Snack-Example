from flask_wtf import FlaskForm
from wtforms import StringField,FloatField, BooleanField, IntegerField, RadioField,SelectField
#import the fields you will use. in this exercise we'll use only stringfield
#and floatfield
from wtforms.validators import InputRequired, Email, Optional
#to add validators, import validators from wtffoms first

class AddSnackForm(FlaskForm): #the parent class is FlaskForm
    """Form for adding new snacks"""
    name = StringField("Snack Name",  validators=[
                       InputRequired(message="Snack Name can't be blank")])
    email = StringField("Email", validators=[Optional(), Email()])
    price = FloatField("Price in USD")
    quantity = IntegerField("How many packets?")
    is_healty = BooleanField("Is the snack healthy?")
    category = RadioField("Category", choices=[('IC' , 'Ice-cream'), ('chips' , 'Patoto Chips'), ('CA', 'Candy/Sweet')])
    new_category = SelectField("New_category" , choices= [('TH' , 'Thai Snack'),('US' , 'US Snack'), ('K' , 'Korean Snack')])


#list of choices is the list of tuples. When we use radio button we need to add choices.
#radio:name=BooleanField("Name" , choices(as keyword argument)[('abb' , 'choice'), ('' , '')])
# category = RadioField("Category", choices=[('IC' , 'Ice-cream'), ('chips' , 'Patoto Chips'), ('CA', 'Candy/Sweet')])
#IC is the what it sends to server Ice-cream is what we see

#validators
#InputRequired() Validates that input provided
#Length: Length(min=-1, max=-1, message=None)
#NumberRange: NumberRange(min=None,max=None,message=None)
#Optional=Allows empty input and stops validation
#AnyOf: Compares the incoming data to a sequence of valid inputs.
#AnyOf(values, message=None,values_formatter=None) 
#None of: Compares the incoming data to a sequence of invalid inputs.
#NoneOf(values, message=None,values_formatter=None) 
