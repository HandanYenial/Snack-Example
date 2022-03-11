from flask_wtf import FlaskForm
from wtforms import StringField,FloatField, BooleanField, IntegerField, RadioField,SelectField
#import the fields you will use.


class AddSnackForm(FlaskForm): #the parent class is FlaskForm
    """Form for adding new snacks"""
    name = StringField("Snack Name")
    price = FloatField("Price in USD")
    quantity = IntegerField("How many packets?")
    is_healty = BooleanField("Is the snack healthy?")
    category = RadioField("Category", choices=[('IC' , 'Ice-cream'), ('chips' , 'Patoto Chips'), ('CA', 'Candy/Sweet')])
    new_category = SelectField("New_category" , choices= [('TH' , 'Thai Snack'),('US' , 'US Snack'), ('K' , 'Korean Snack')])


#list of choices is the list of tuples. When we use radio button we need to add choices.
#radio:name=BooleanField("Name" , choices(as keyword argument)[('abb' , 'choice'), ('' , '')])
#IC is the what it sends to server Ice-cream is what we see
