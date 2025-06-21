from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalField, IntegerField, TextAreaField, SelectField, BooleanField, FileField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ProductForm(FlaskForm):
    name_ar = StringField('Name (AR)', validators=[DataRequired()])
    name_en = StringField('Name (EN)', validators=[DataRequired()])
    item_uid = StringField('Item UID', validators=[DataRequired()])
    item_code = StringField('Item Code', validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    short_description = TextAreaField('Short Description', validators=[Optional()])
    total_cost = DecimalField('Total Cost', validators=[Optional()])
    barcode = StringField('Barcode', validators=[Optional()])
    quantity = IntegerField('Quantity', validators=[Optional()])
    inventory_location = StringField('Inventory Location', validators=[Optional()])
    price = DecimalField('Price', validators=[Optional()])
    cost = DecimalField('Cost', validators=[Optional()])
    tags = SelectMultipleField('Tags', coerce=int, validators=[Optional()])
    submit = SubmitField('Save')

class ProductPhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[Optional()])
    submit = SubmitField('Upload')

class MediaForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    media_type = SelectField('Media Type', choices=[('post', 'Post'), ('reel', 'Reel'), ('story', 'Story')], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    file = FileField('Media File', validators=[Optional()])
    file_url = StringField('Google Drive Link', validators=[Optional()])
    published = BooleanField('Published')
    submit = SubmitField('Save') 