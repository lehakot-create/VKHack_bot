from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Employee, JobTitle, Department, Mentor
from .forms import EmployeeForm, JobTitleForm, DepartmentForm, MentorForm
from .filters import EmployeeFilter


class Index(ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employee'


class FindView(ListView):
    model = Employee
    template_name = 'find.html'

    def get_queryset(self):
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EmployeeFilter(self.request.GET,
                                           queryset=Employee.objects.all())
        print(context)
        return context


def login(request):
    return render(request, 'login.html')


class EmployeeCreateView(LoginRequiredMixin,
                         CreateView):
    model = Employee
    template_name = 'create.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('index')


class JobTitleCreateView(LoginRequiredMixin,
                         CreateView):
    model = JobTitle
    template_name = 'update.html'
    form_class = JobTitleForm
    success_url = reverse_lazy('index')


class DepartmentCreateView(LoginRequiredMixin,
                           CreateView):
    model = Department
    template_name = 'update.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('index')


class MentorCreateView(LoginRequiredMixin,
                       CreateView):
    model = Mentor
    template_name = 'update.html'
    form_class = MentorForm
    success_url = reverse_lazy('index')
