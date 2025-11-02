from app import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # creates tables if not exist
    app.run(debug=True)
