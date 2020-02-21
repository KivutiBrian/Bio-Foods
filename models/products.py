from app import db

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.String(30), nullable=False)
    cust = db.relationship('Orders', backref='order')

    # CREATE
    def insert_record(self):
        db.session.add(self)
        db.session.commit()

    # check if a product exists
    @classmethod
    def check_product_exists(cls,name):
        prd = cls.query.filter_by(name=name).first()

        if prd:
            return True
        else:
            return False
    
    # Fetch all products
    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    # update a product
    @classmethod
    def update_by_id(cls,id,name=None,price=None):
        product = cls.query.filter_by(id=id).first()
        if product:
            if name:
                product.name = name
            if price:
                product.price = price
                
            db.session.commit()
            return True
        else:
            return False

    # delete a product
    @classmethod
    def delete_by_id(cls,id):
        record = cls.query.filter_by(id=id)
        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False