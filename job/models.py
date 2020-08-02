from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

JobTypes = [
    (0,"技术类"),
    (1,"产品类"),
    (2,"运营类"),
    (3,"设计类"),
    (4,"市场营销类")
]

Cities = [
    (0,"北京"),
    (1,"上海"),
    (2,"深圳"),
    (3,"杭州"),
    (4,"广州")
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="工作地点")
    job_responsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", default=datetime.now)