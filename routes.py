from flask import Blueprint, jsonify, request

from models import (
    db,
    Hospital,
    PoliceStation,
    EmergencyService,
    GovernmentOffice,
    Transport,
    Announcement
)


# =========================================
# CREATE API BLUEPRINT
# =========================================

api = Blueprint("api", __name__)


# =========================================
# HOSPITALS
# =========================================

@api.route("/api/hospitals", methods=["GET"])
def get_hospitals():

    hospitals = Hospital.query.all()

    data = []

    for hospital in hospitals:

        data.append({
            "id": hospital.id,
            "name": hospital.name,
            "location": hospital.location,
            "services": hospital.services,
            "map_link": hospital.map_link
        })

    return jsonify(data)


@api.route("/api/hospitals", methods=["POST"])
def add_hospital():

    data = request.get_json()

    hospital = Hospital(
        name=data["name"],
        location=data["location"],
        services=data.get("services", ""),
        map_link=data.get("map_link", "")
    )

    db.session.add(hospital)
    db.session.commit()

    return jsonify({
        "message": "Hospital added successfully",
        "id": hospital.id
    }), 201


@api.route("/api/hospitals/<int:id>", methods=["PUT"])
def update_hospital(id):

    hospital = Hospital.query.get_or_404(id)

    data = request.get_json()

    hospital.name = data.get("name", hospital.name)
    hospital.location = data.get("location", hospital.location)
    hospital.services = data.get("services", hospital.services)
    hospital.map_link = data.get("map_link", hospital.map_link)

    db.session.commit()

    return jsonify({
        "message": "Hospital updated successfully"
    })


@api.route("/api/hospitals/<int:id>", methods=["DELETE"])
def delete_hospital(id):

    hospital = Hospital.query.get_or_404(id)

    db.session.delete(hospital)
    db.session.commit()

    return jsonify({
        "message": "Hospital deleted successfully"
    })


# =========================================
# POLICE STATIONS
# =========================================

@api.route("/api/police", methods=["GET"])
def get_police_stations():

    stations = PoliceStation.query.all()

    data = []

    for station in stations:

        data.append({
            "id": station.id,
            "name": station.name,
            "location": station.location,
            "services": station.services,
            "map_link": station.map_link
        })

    return jsonify(data)


@api.route("/api/police", methods=["POST"])
def add_police_station():

    data = request.get_json()

    station = PoliceStation(
        name=data["name"],
        location=data["location"],
        services=data.get("services", ""),
        map_link=data.get("map_link", "")
    )

    db.session.add(station)
    db.session.commit()

    return jsonify({
        "message": "Police station added successfully",
        "id": station.id
    }), 201


@api.route("/api/police/<int:id>", methods=["PUT"])
def update_police_station(id):

    station = PoliceStation.query.get_or_404(id)

    data = request.get_json()

    station.name = data.get("name", station.name)
    station.location = data.get("location", station.location)
    station.services = data.get("services", station.services)
    station.map_link = data.get("map_link", station.map_link)

    db.session.commit()

    return jsonify({
        "message": "Police station updated successfully"
    })


@api.route("/api/police/<int:id>", methods=["DELETE"])
def delete_police_station(id):

    station = PoliceStation.query.get_or_404(id)

    db.session.delete(station)
    db.session.commit()

    return jsonify({
        "message": "Police station deleted successfully"
    })


# =========================================
# EMERGENCY SERVICES
# =========================================

@api.route("/api/emergency", methods=["GET"])
def get_emergency_services():

    services = EmergencyService.query.all()

    data = []

    for service in services:

        data.append({
            "id": service.id,
            "name": service.name,
            "description": service.description,
            "service_number": service.service_number
        })

    return jsonify(data)


@api.route("/api/emergency", methods=["POST"])
def add_emergency_service():

    data = request.get_json()

    service = EmergencyService(
        name=data["name"],
        description=data.get("description", ""),
        service_number=data.get("service_number", "")
    )

    db.session.add(service)
    db.session.commit()

    return jsonify({
        "message": "Emergency service added successfully",
        "id": service.id
    }), 201


@api.route("/api/emergency/<int:id>", methods=["PUT"])
def update_emergency_service(id):

    service = EmergencyService.query.get_or_404(id)

    data = request.get_json()

    service.name = data.get(
        "name",
        service.name
    )

    service.description = data.get(
        "description",
        service.description
    )

    service.service_number = data.get(
        "service_number",
        service.service_number
    )

    db.session.commit()

    return jsonify({
        "message": "Emergency service updated successfully"
    })


@api.route("/api/emergency/<int:id>", methods=["DELETE"])
def delete_emergency_service(id):

    service = EmergencyService.query.get_or_404(id)

    db.session.delete(service)
    db.session.commit()

    return jsonify({
        "message": "Emergency service deleted successfully"
    })


# =========================================
# GOVERNMENT OFFICES
# =========================================

@api.route("/api/government", methods=["GET"])
def get_government_offices():

    offices = GovernmentOffice.query.all()

    data = []

    for office in offices:

        data.append({
            "id": office.id,
            "name": office.name,
            "location": office.location,
            "services": office.services,
            "map_link": office.map_link
        })

    return jsonify(data)


@api.route("/api/government", methods=["POST"])
def add_government_office():

    data = request.get_json()

    office = GovernmentOffice(
        name=data["name"],
        location=data["location"],
        services=data.get("services", ""),
        map_link=data.get("map_link", "")
    )

    db.session.add(office)
    db.session.commit()

    return jsonify({
        "message": "Government office added successfully",
        "id": office.id
    }), 201


@api.route("/api/government/<int:id>", methods=["PUT"])
def update_government_office(id):

    office = GovernmentOffice.query.get_or_404(id)

    data = request.get_json()

    office.name = data.get(
        "name",
        office.name
    )

    office.location = data.get(
        "location",
        office.location
    )

    office.services = data.get(
        "services",
        office.services
    )

    office.map_link = data.get(
        "map_link",
        office.map_link
    )

    db.session.commit()

    return jsonify({
        "message": "Government office updated successfully"
    })


@api.route("/api/government/<int:id>", methods=["DELETE"])
def delete_government_office(id):

    office = GovernmentOffice.query.get_or_404(id)

    db.session.delete(office)
    db.session.commit()

    return jsonify({
        "message": "Government office deleted successfully"
    })


# =========================================
# TRANSPORT
# =========================================

@api.route("/api/transport", methods=["GET"])
def get_transport():

    transport_items = Transport.query.all()

    data = []

    for item in transport_items:

        data.append({
            "id": item.id,
            "name": item.name,
            "transport_type": item.transport_type,
            "location": item.location,
            "details": item.details,
            "map_link": item.map_link
        })

    return jsonify(data)


@api.route("/api/transport", methods=["POST"])
def add_transport():

    data = request.get_json()

    transport = Transport(
        name=data["name"],
        transport_type=data.get("transport_type", ""),
        location=data.get("location", ""),
        details=data.get("details", ""),
        map_link=data.get("map_link", "")
    )

    db.session.add(transport)
    db.session.commit()

    return jsonify({
        "message": "Transport information added successfully",
        "id": transport.id
    }), 201


@api.route("/api/transport/<int:id>", methods=["PUT"])
def update_transport(id):

    transport = Transport.query.get_or_404(id)

    data = request.get_json()

    transport.name = data.get(
        "name",
        transport.name
    )

    transport.transport_type = data.get(
        "transport_type",
        transport.transport_type
    )

    transport.location = data.get(
        "location",
        transport.location
    )

    transport.details = data.get(
        "details",
        transport.details
    )

    transport.map_link = data.get(
        "map_link",
        transport.map_link
    )

    db.session.commit()

    return jsonify({
        "message": "Transport information updated successfully"
    })


@api.route("/api/transport/<int:id>", methods=["DELETE"])
def delete_transport(id):

    transport = Transport.query.get_or_404(id)

    db.session.delete(transport)
    db.session.commit()

    return jsonify({
        "message": "Transport information deleted successfully"
    })


# =========================================
# ANNOUNCEMENTS
# =========================================

@api.route("/api/announcements", methods=["GET"])
def get_announcements():

    announcements = Announcement.query.all()

    data = []

    for announcement in announcements:

        data.append({
            "id": announcement.id,
            "title": announcement.title,
            "content": announcement.content,
            "date": announcement.date
        })

    return jsonify(data)


@api.route("/api/announcements", methods=["POST"])
def add_announcement():

    data = request.get_json()

    announcement = Announcement(
        title=data["title"],
        content=data["content"],
        date=data.get("date", "")
    )

    db.session.add(announcement)
    db.session.commit()

    return jsonify({
        "message": "Announcement added successfully",
        "id": announcement.id
    }), 201


@api.route("/api/announcements/<int:id>", methods=["PUT"])
def update_announcement(id):

    announcement = Announcement.query.get_or_404(id)

    data = request.get_json()

    announcement.title = data.get(
        "title",
        announcement.title
    )

    announcement.content = data.get(
        "content",
        announcement.content
    )

    announcement.date = data.get(
        "date",
        announcement.date
    )

    db.session.commit()

    return jsonify({
        "message": "Announcement updated successfully"
    })


@api.route("/api/announcements/<int:id>", methods=["DELETE"])
def delete_announcement(id):

    announcement = Announcement.query.get_or_404(id)

    db.session.delete(announcement)
    db.session.commit()

    return jsonify({
        "message": "Announcement deleted successfully"
    })


# =========================================
# ADMIN LOGIN
# =========================================

@api.route("/api/login", methods=["POST"])
def admin_login():

    data = request.get_json()

    username = data.get("username", "")
    password = data.get("password", "")

    # Demo credentials for CSP project
    if username == "admin" and password == "admin123":

        return jsonify({
            "success": True,
            "message": "Login successful"
        }), 200

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    }), 401