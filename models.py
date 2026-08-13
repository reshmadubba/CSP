from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# =========================
# HOSPITALS
# =========================

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    services = db.Column(db.Text, nullable=True)
    map_link = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<Hospital {self.name}>"


# =========================
# POLICE STATIONS
# =========================

class PoliceStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    services = db.Column(db.Text, nullable=True)
    map_link = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<PoliceStation {self.name}>"


# =========================
# EMERGENCY SERVICES
# =========================

class EmergencyService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    service_number = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<EmergencyService {self.name}>"


# =========================
# GOVERNMENT OFFICES
# =========================

class GovernmentOffice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    services = db.Column(db.Text, nullable=True)
    map_link = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<GovernmentOffice {self.name}>"


# =========================
# TRANSPORT
# =========================

class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    transport_type = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(250), nullable=True)
    details = db.Column(db.Text, nullable=True)
    map_link = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<Transport {self.name}>"


# =========================
# ANNOUNCEMENTS
# =========================

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Announcement {self.title}>"


# =========================
# ADMIN
# =========================

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Admin {self.username}>"