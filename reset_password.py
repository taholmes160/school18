from app import create_app, db
from app.models import User

app = create_app()
app.app_context().push()

# Query the user by username
username = 'taholmes160'
new_password = 'school1234'

user = User.query.filter_by(username=username).first()

# Check if the user exists
if user:
    # Reset the password
    user.set_password(new_password)
    db.session.commit()
    print(f"Password reset successful for user: {username}")
else:
    print(f"User not found: {username}")