from app import db,bcrypt

class CustomerModel(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    company = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(), nullable=True)
    orders = db.relationship('Orders', backref='customer', lazy=True)

    # insert_record
    def insert_record(self):
        db.session.add(self)
        db.session.commit()


    # check if a email exist
    @classmethod
    def check_email_exists(cls,email):
        customer =  cls.query.filter_by(email=email).first()
        if customer:
            return True
        else:
            return False

    # fetch all customer records
    @classmethod
    def fetch_all_customers(cls):
        return cls.query.all()

    # update a customer
    @classmethod
    def update_customer_by_id(cls,id,name=None,email=None,phone=None,address=None,city=None):
        customer = cls.query.filter_by(id=id).first()

        if customer:
            if name:
                customer.name = name
            if email:
                customer.email = email
            if phone:
                customer.phone = phone_number
            if address:
                customer.address = address
            if city:
                customer.city = city
            db.session.commit()
            return True
        else:
            return False

    # delete a customer
    @classmethod
    def delete_by_id(cls,id):
        customer = cls.query.filter_by(id=id)
        if customer.first():
            customer.delete()
            db.session.commit()
            return True
        else:
            return False

    # confirm password
    @classmethod
    def compare_password(cls,email,password):
        customer = cls.query.filter_by(email=email).first()

        if customer and bcrypt.check_password_hash(customer.password,password):
            return True
        else:
            return False

    # get customer id
    @classmethod
    def get_customer_id(cls,email):
        return cls.query.filter_by(email=email).first().id
    
    # get customer id
    @classmethod
    def get_customer_company(cls,email):
        return cls.query.filter_by(email=email).first().company


