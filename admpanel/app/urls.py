from django.urls import path

from .views import login, Index, EmployeeCreateView, JobTitleCreateView, \
     DepartmentCreateView, MentorCreateView, FindView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', login, name='login'),

    path('emp_create/',
         EmployeeCreateView.as_view(),
         name='create_employee'),
    path('jobtitle_create/',
         JobTitleCreateView.as_view(),
         name='create_jobtitle'),
    path('department_create/',
         DepartmentCreateView.as_view(),
         name='create_department'),
    path('mentor_create/',
         MentorCreateView.as_view(),
         name='create_mentor'),
    path('find/',
         FindView.as_view(),
         name='find'),
]
