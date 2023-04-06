from django import forms

from .models import Employee, JobTitle, Department, Mentor


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'date_time_contract': forms.DateInput(
                                        format=('%d/%m/%Y'),
                                        attrs={'class': 'form-control',
                                               'placeholder': 'Select a date',
                                               'type': 'date'}),
            'birthday': forms.DateInput(
                                        format=('%d/%m/%Y'),
                                        attrs={'class': 'form-control',
                                               'placeholder': 'Select a date',
                                               'type': 'date'}),
        }


class JobTitleForm(forms.ModelForm):
    class Meta:
        model = JobTitle
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'
