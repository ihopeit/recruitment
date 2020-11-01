from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Job, Resume
from interview.dingtalk import send

import json, logging
logger = logging.getLogger(__name__)

# 使用 decorator 来注册 信号处理器
@receiver(signal=post_save, sender=Resume, dispatch_uid="resume_post_save_dispatcher")
@receiver(signal=post_save, sender=Job, dispatch_uid="job_post_save_dispatcher")
def post_save_callback(sender, instance=None, created=False, **kwarg):
    message = ""
    if isinstance(instance, Job):
        message = "Job for %s has been saved" % instance.job_name
    else:
        message = "Resume for %s %s has been saved " % (instance.username , instance.apply_position)
    
    logger.info(message)
    send(message)


from django.forms.models import model_to_dict

def post_delete_callback(sender, instance=None, using=None, **kwarg):
    dict_obj = model_to_dict( instance, exclude=("picture","attachment", "created_date", "modified_date") )
    message = "Instance of %s has been deleted: %s" % (type(instance), json.dumps(dict_obj, ensure_ascii=False))
    logger.info(message)
    send(message)

## 手工注册信号处理器
post_delete.connect(post_delete_callback, sender=Resume, dispatch_uid="resume_post_delete_dispatcher")
