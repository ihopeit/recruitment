from django.contrib import admin
from datetime import datetime
from interview.models import Candidate


# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')

    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer', 'second_score',
        'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'hr_interviewer', 'last_editor')

    # add_form_template = 'admin/add_candidate.html'
    # change_form_template = 'admin/edit_candidate.html'

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user.username
        if not obj.creator:
            obj.creator = request.user.username
        obj.modified_date = datetime.now()
        obj.save()


admin.site.register(Candidate, CandidateAdmin)