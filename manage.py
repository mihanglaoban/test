# 15. extract config class from manage.py to a new file
from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# 11. create manager to enable command line control
from info import create_app, db

# 19. create specified name by specified name
app = create_app("development")

manager = Manager(app)
# 13. use migrate to relate the app and mySQL
Migrate(app, db)
# 14. add migrate command to manager
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    session['name'] = "itheima"
    return "success!"


def main():
    #12. use manager to run the app
    manager.run()


if __name__ == "__main__":
    main()
