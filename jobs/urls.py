from django.conf.urls import url
from django.urls import path
from django.conf import settings

from jobs import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),

    # 管理员创建 HR 账号的 页面:
    path('create_hr_user/', views.create_hr_user, name='create_hr_user'),

    # 职位详情
    #url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
    path('job/<int:job_id>/', views.detail, name='detail'),

    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),

    path('sentry-debug/', trigger_error),

    # 首页自动跳转到 职位列表
    #url(r"^$", views.joblist, name="name"),
    path("", views.joblist, name="name"),

]

if settings.DEBUG :
    # 有 XSS 漏洞的视图页面，
    urlpatterns += [url(r'^detail_resume/(?P<resume_id>\d+)/$', views.detail_resume, name='detail_resume'),]