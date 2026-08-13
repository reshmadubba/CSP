from flask import Flask, send_from_directory
from flask_cors import CORS

from models import (
    db,
    Hospital,
    PoliceStation,
    EmergencyService,
    GovernmentOffice,
    Transport,
    Announcement
)

from routes import api

import os


# =========================================
# PROJECT PATHS
# =========================================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

FRONTEND_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..", "frontend")
)


# =========================================
# CREATE FLASK APPLICATION
# =========================================

app = Flask(__name__)


# =========================================
# ENABLE CORS
# =========================================

CORS(app)


# =========================================
# DATABASE CONFIGURATION
# =========================================

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(BASE_DIR, "database.db")
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# =========================================
# CONNECT DATABASE
# =========================================

db.init_app(app)


# =========================================
# REGISTER API ROUTES
# =========================================

app.register_blueprint(api)


# =========================================
# SERVE FRONTEND FILES
# =========================================

@app.route("/")
def home():

    return send_from_directory(
        FRONTEND_DIR,
        "index.html"
    )


@app.route("/<path:filename>")
def frontend_files(filename):

    return send_from_directory(
        FRONTEND_DIR,
        filename
    )


# =========================================
# CREATE TABLES + INITIAL DATA
# =========================================

with app.app_context():

    db.create_all()


    # -------------------------
    # HOSPITALS
    # -------------------------

    if Hospital.query.count() == 0:

        hospitals = [

            Hospital(
                name="Maharaja Government District Hospital",
                location="Vizianagaram, Andhra Pradesh",
                services="Government hospital and general medical services",
                map_link="https://www.google.com/maps/search/?api=1&query=Maharaja+Government+District+Hospital+Vizianagaram"
            ),

            Hospital(
                name="Tirumala Medicover Hospitals",
                location="Vizianagaram, Andhra Pradesh",
                services="Multi-speciality healthcare services",
                map_link="https://www.google.com/maps/search/?api=1&query=Tirumala+Medicover+Hospitals+Vizianagaram"
            )

        ]

        db.session.add_all(hospitals)


    # -------------------------
    # POLICE
    # -------------------------

    if PoliceStation.query.count() == 0:

        police = [

            PoliceStation(
                name="Vizianagaram I Town Police Station",
                location="Vizianagaram, Andhra Pradesh",
                services="Law and order and public safety services",
                map_link="https://www.google.com/maps/search/?api=1&query=Vizianagaram+I+Town+Police+Station"
            ),

            PoliceStation(
                name="Vizianagaram II Town Police Station",
                location="Vizianagaram, Andhra Pradesh",
                services="Law and order and public safety services",
                map_link="https://www.google.com/maps/search/?api=1&query=Vizianagaram+II+Town+Police+Station"
            )

        ]

        db.session.add_all(police)


    # -------------------------
    # EMERGENCY SERVICES
    # -------------------------

    if EmergencyService.query.count() == 0:

        emergency = [

            EmergencyService(
                name="Ambulance",
                description="Emergency ambulance service",
                service_number="108"
            ),

            EmergencyService(
                name="Police",
                description="Police emergency assistance",
                service_number="112"
            ),

            EmergencyService(
                name="Fire and Rescue",
                description="Fire and rescue emergency service",
                service_number="101"
            )

        ]

        db.session.add_all(emergency)


    # -------------------------
    # GOVERNMENT OFFICES
    # -------------------------

    if GovernmentOffice.query.count() == 0:

        offices = [

            GovernmentOffice(
                name="District Collectorate",
                location="Vizianagaram, Andhra Pradesh",
                services="District administration and public services",
                map_link="https://www.google.com/maps/search/?api=1&query=Vizianagaram+Collectorate"
            ),

            GovernmentOffice(
                name="Municipal Office",
                location="Vizianagaram, Andhra Pradesh",
                services="Municipal and civic services",
                map_link="https://www.google.com/maps/search/?api=1&query=Vizianagaram+Municipality+Office"
            )

        ]

        db.session.add_all(offices)


    # -------------------------
    # TRANSPORT
    # -------------------------

    if Transport.query.count() == 0:

        transport = [

            Transport(
                name="Vizianagaram RTC Bus Station",
                transport_type="Bus",
                location="Vizianagaram, Andhra Pradesh",
                details="Public bus transportation facility",
                map_link="https://www.google.com/maps/search/?api=1&query=Vizianagaram+RTC+Bus+Station"
            ),

            Transport(
                name="Vizianagaram Railway Station",
                transport_type="Railway",
                location="Vizianagaram, Andhra Pradesh",
                details="Railway transportation facility",
                map_link="https://www.google.com/maps/search/?api=1&query=Vizianagaram+Railway+Station"
            )

        ]

        db.session.add_all(transport)


    # -------------------------
    # ANNOUNCEMENTS
    # -------------------------

    if Announcement.query.count() == 0:

        announcements = [

            Announcement(
                title="Local Information System",
                content="Important local services can be accessed through this platform.",
                date="2026-08-12"
            ),

            Announcement(
                title="Emergency Services",
                content="Emergency service information is available through the Emergency section.",
                date="2026-08-12"
            ),

            Announcement(
                title="Public Information",
                content="Users can access information about hospitals, police, transport and government services.",
                date="2026-08-12"
            )

        ]

        db.session.add_all(announcements)


    db.session.commit()


# =========================================
# RUN APPLICATION
# =========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )