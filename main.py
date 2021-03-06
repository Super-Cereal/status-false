from flask import Flask, render_template
from blueprints import user_authenticate, tasks, groups, users

from flask_restful import Api
from api import resourses_users, resourses_groups

from data import db_session


app = Flask(__name__)
app.config.from_object('config')
user_authenticate.login_manager.init_app(app)
db_session.global_init('db/SQLiteBase.sqlite')

app.register_blueprint(user_authenticate.blueprint)
app.register_blueprint(groups.blueprint)
app.register_blueprint(tasks.blueprint)
app.register_blueprint(users.blueprint)
app.register_blueprint(tasks.blueprint)

api = Api(app)
api.add_resource(resourses_users.UserListResourse, '/api/users')
api.add_resource(resourses_users.UserResourse, '/api/users/<int:user_id>')
api.add_resource(resourses_groups.GroupListResourse, '/api/groups')
api.add_resource(resourses_groups.GroupResourse, '/api/groups/<int:group_id>')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    if True:
        # port = int(os.environ.get("PORT", 5000))
        # app.run(host='0.0.0.0', port=port)
        app.run()
