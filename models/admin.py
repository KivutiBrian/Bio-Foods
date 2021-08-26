from app import db,bcrypt

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    # create
    def insert_record(self):
        db.session.add(self)
        db.session.commit()

    # check if an admin already exist
    @classmethod
    def check_admin_exist(cls,email):
        admin = cls.query.filter_by(email=email).first()
        if admin:
            return True
        else:
            return False

    # get admin id
    @classmethod
    def get_admin_id(cls,email):
        return cls.query.filter_by(email=email).first().id

    # validate password
    @classmethod
    def validate_password(cls,email,password):
        adm = cls.query.filter_by(email=email).first()

        if adm and bcrypt.check_password_hash(adm.password,password):
            return True
        else:
            return False
            