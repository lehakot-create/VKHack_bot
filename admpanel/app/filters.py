from django_filters import FilterSet

from .models import Employee


class EmployeeFilter(FilterSet):
    class Meta:
        model = Employee
        fields = ('surname',
                  'name',
                  'surname2',
                  'birthday',
                  'job_title',
                  'date_time_contract',
                  'department',
                  'mentor',)
