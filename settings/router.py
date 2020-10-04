# settings/router.py
# database router to multiple database by app label
class DatabaseRouter:
    route_app_labels = {'running'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'running'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'running'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        遗留数据库中的表不允许迁移
        """
        if app_label in self.route_app_labels:
            return False
        return True