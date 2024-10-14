from app import create_app, db
from app.models import User, StudentProfile

app = create_app()

with app.app_context():
    users = User.query.all()
    for user in users:
        student_profile = StudentProfile(
            id=user.id,
            date_of_birth=None,
            emergency_contact_name=None,
            emergency_contact_phone=None,
            emergency_contact_relationship=None,
            allergies=None,
            medical_conditions=None,
            medications=None,
            enrollment_date=None,
            previous_school=None,
            extra_curricular_activities=None,
            special_needs=None
        )
        db.session.add(student_profile)
    db.session.commit()