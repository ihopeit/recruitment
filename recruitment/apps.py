from django.contrib import admin
from django.apps import apps, AppConfig

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        # 列表页自动显示所有的字段：
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


class UniversalManagerApp(AppConfig):
    """
    应用配置在 所有应用的 Admin 都加载完之后执行
    """
    verbose_name = 'Universal Model Managers'

    # the name of the AppConfig must be the same as current application
    name = 'recruitment'

    def ready(self):
        models = apps.get_app_config('running').get_models() 
        for model in models:
            admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
            try:
                admin.site.register(model, admin_class)
            except admin.sites.AlreadyRegistered:
                pass
