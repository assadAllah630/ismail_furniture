from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ar = db.Column(db.String(255), nullable=False)
    name_en = db.Column(db.String(255), nullable=False)
    item_uid = db.Column(db.String(255), nullable=False)
    item_code = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    short_description = db.Column(db.Text)
    total_cost = db.Column(db.Numeric(10,2))
    barcode = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    inventory_location = db.Column(db.String(255))
    price = db.Column(db.Numeric(10,2))
    cost = db.Column(db.Numeric(10,2))
    photos = db.relationship('ProductPhoto', backref='product', lazy=True)
    tags = db.relationship('Tag', secondary='product_tags', backref='products')
    media = db.relationship('Media', secondary='product_media', backref='products')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

product_tags = db.Table('product_tags',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class ProductPhoto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    photo_url = db.Column(db.String(512), nullable=False)
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    media_type = db.Column(db.Enum('post', 'reel', 'story'), nullable=False)
    description = db.Column(db.Text)
    file_url = db.Column(db.String(512), nullable=False)
    upload_date = db.Column(db.DateTime, server_default=db.func.now())
    published = db.Column(db.Boolean, default=False)

product_media = db.Table('product_media',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('media_id', db.Integer, db.ForeignKey('media.id'), primary_key=True)
) 