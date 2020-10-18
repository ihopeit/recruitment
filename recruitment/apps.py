from django.contrib import admin
from django.apps import apps, AppConfig


class AdminClass(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        # 列表页自动显示所有的字段：
        self.list_display = [field.name for field in model._meta.fields]
        super(AdminClass, self).__init__(model, admin_site)

# automatically register all models
class UniversalManagerApp(AppConfig):
    """
    应用配置在 所有应用的 Admin 都加载完之后执行
    """
    # the name of the AppConfig must be the same as current application
    name = 'recruitment'

    def ready(self):
        models = apps.get_app_config('running').get_models() 
        for model in models:
            try:
                admin.site.register(model, AdminClass)
            except admin.sites.AlreadyRegistered:
                pass
