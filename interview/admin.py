from django.contrib import admin
from datetime import datetime
from interview.models import Candidate


# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')

    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer', 'second_score',
        'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'hr_interviewer', 'last_editor')

    # 分组展示字段，分三块，基础信息、第一轮面试记录、第二轮面试（专业复试）、HR复试
    fieldsets = (
        (None, {'fields': ("userid", ("username", "city", "phone"), ("email", "apply_position", "born_address", "gender", "candidate_remark"), ("bachelor_school", "master_school", "doctor_school"), ("major", "degree"), ("test_score_of_general_ability", "paper_score"),)}),
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