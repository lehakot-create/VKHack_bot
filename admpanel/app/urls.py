from django.urls import path

from .views import Index, EmployeeCreateView, JobTitleCreateView, \
     DepartmentCreateView, MentorCreateView, FindView, MyLoginView, \
     MyLogoutView


urlpatterns = [
    path('', Index.as_view(), name='index'),
#     path('accounts/login/', MyLoginView.as_view(), name='accounts_login'),
#     path('accounts/logout/', MyLogoutView.as_view(), name='accounts_logout'),

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
