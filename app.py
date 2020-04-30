from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)

    def __repr__(self):
        return f'<{self.name}>'


@app.route('/', methods=['GET', 'POST'])
def home():
    name = request.form.get('name')
    if name:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()

    users = User.query.order_by(User.name).all()
    print(users)
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)

    # flask db init
    # flask db migrate
    # flask db upgrade