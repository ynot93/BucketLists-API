from app import db, app

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
