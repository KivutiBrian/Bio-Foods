from app import db
from sqlalchemy.sql import func

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(), nullable= False)
    orderdate = db.Column(db.DateTime(timezone= True), server_default = func.now())
    company = db.Column(db.String(), nullable=True)
    status = db.Column(db.String(), default="pending")
    customer_name = db.Column(db.String(), nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    product_id = db.Column(db.Integer,  db.ForeignKey('products.id'))

    # create
    def create_record(self):
        db.session.add(self)
        db.session.commit()

    
    # fetch by id
    @classmethod
    def fetch_by_id(cls,id):
        return cls.query.filter_by(customer_id=id).all()

    
    # fetch all
    @classmethod
    def fetch_all(cls):
        return cls.query.all()
        
    
    # update
    @classmethod
    def update_by_id(cls,id,product=None,email=None,orderdate=None,company=None,status=None):
        record = cls.query.filter_by(id=id).first()

        if product:
            record.product = product
        if email:
            record.email = email
        if orderdate:
            record.orderdate = orderdate
        if company:
            record.company = company
        if status:
            record.status = status

        db.session.commit()
        return True
    
