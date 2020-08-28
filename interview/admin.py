from django.contrib import admin
from django.http import HttpResponse

import csv
from datetime import datetime

from interview.models import Candidate

exportable_fields = ('username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interviewer',
                     'second_result', 'second_interviewer', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer')

### define export action
def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'recruitment-candidates',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )

    ### 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )

    for obj in queryset:
        ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)

    return response


export_model_as_csv.short_description = u'导出为CSV文件'

# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')

    actions = (export_model_as_csv,)

    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer', 'second_score',
        'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'hr_interviewer',)

    ### 右侧筛选条件
    list_filter = ('city','first_result','second_result','hr_result','first_interviewer','second_interviewer','hr_interviewer')

    ### 查询字段
    search_fields = ('username', 'phone', 'email', 'bachelor_school')

    ### 列表页排序字段
    ordering = ('hr_result','second_result','first_result',)

    # 分组展示字段，分三块，基础信息、第一轮面试记录、第二轮面试（专业复试）、HR复试
    fieldsets = (
        (None, {'fields': ("userid", ("username", "city", "phone"), ("email", "apply_position", "born_address", "gender", "candidate_remark"), ("bachelor_school", "master_school", "doctor_school"), ("major", "degree"), "test_score_of_general_ability", "paper_score",)}),
        ('第一轮面试', {'fields': (("first_score", "first_learning_ability", "first_professional_competency"), "first_advantage", "first_disadvantage", "first_result", "first_recommend_position", "first_interviewer", "first_remark",)}),
        ('第二轮面试（专业复试）', {'fields': (("second_score", "second_learning_ability", "second_professional_competency"),("second_pursue_of_excellence", "second_communication_ability", "second_pressure_score"), "second_advantage", "second_disadvantage", "second_result", "second_recommend_position", "second_interviewer", "second_remark",)}),
        ('HR复试', {'fields': ("hr_score", ("hr_responsibility", "hr_communication_ability", "hr_logic_ability"), ("hr_potential", "hr_stability"), "hr_advantage", "hr_disadvantage", "hr_result", "hr_interviewer", "hr_remark",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user.username
        if not obj.creator:
            obj.creator = request.user.username
        obj.modified_date = datetime.now()
        obj.save()


admin.site.register(Candidate, CandidateAdmin)