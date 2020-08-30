from django.forms import ModelForm

from .models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume

        fields = ["username", "city", "phone",
        "email", "apply_position", "born_address", "gender",
        "bachelor_school", "master_school", "major", "degree", 'created_date', 'modified_date',
        "candidate_introduction", "work_experience", "project_experience"]