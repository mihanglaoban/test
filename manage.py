from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# 11. create manager to enable command line control
from info import create_app, db, models

# 19. create specified name by specified name
from info.models import User

app = create_app("development")

manager = Manager(app)
# 13. use migrate to relate the app and mySQL
Migrate(app, db)
# 14. add migrate command to manager
manager.add_command('db', MigrateCommand)


@manager.option('-n', '-username', dest="username")
@manager.option('-p', '-password', dest="password")
def createsuperuser(username, password):
    if not all([username, password]):
        print("参数不足")

    user = User()
    user.nick_name = username
    user.mobile = username
    user.password = password
    user.is_admin = True

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        return

    print("添加成功")


def main():
    # 12. use manager to run the app
    manager.run()


if __name__ == "__main__":
    main()
