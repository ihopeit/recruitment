from django.conf.urls import url
from job.views import joblist

urlpatterns = [
    url(r"^joblist/", joblist, name="joblist"),
]