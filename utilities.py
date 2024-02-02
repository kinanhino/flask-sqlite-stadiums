from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


from views import home, add_stadium,register,login,logout,stadium_details, delete_stadium, edit_stadium

def configure_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/login', 'login', login,methods=['POST','GET'])
    app.add_url_rule('/logout', 'logout', logout,methods=['POST','GET'])
    app.add_url_rule('/register', 'register',register,methods=['POST','GET'])
    app.add_url_rule('/add_stadium', 'add_stadium', add_stadium, methods=['GET', 'POST'])
    app.add_url_rule('/stadium/<stadium_id>', 'stadium_details', stadium_details, methods=['GET', 'POST'])
    app.add_url_rule('/delete_stadium/<stadium_id>', 'delete_stadium', delete_stadium, methods=['POST'])
    app.add_url_rule('/edit_stadium/<stadium_id>', 'edit_stadium', edit_stadium, methods=['GET', 'POST'])

