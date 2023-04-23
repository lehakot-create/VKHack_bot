from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from allauth.account.views import LoginView, LogoutView

from .models import Employee, JobTitle, Department, Mentor
from .forms import EmployeeForm, JobTitleForm, DepartmentForm, MentorForm
from .filters import EmployeeFilter
from .utils import get_uuid
from admpanel.settings import BOT_PATH


class Index(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employee'


class FindView(ListView):
    model = Employee
    template_name = 'find.html'

    def get_queryset(self):
        if self.request.GET.get('surname') is not None:
            return self.queryset
        return Employee.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EmployeeFilter(self.request.GET,
                                           queryset=self.get_queryset())
        return context


class MyLoginView(LoginView):
    template_name = 'login.html'


class MyLogoutView(LogoutView):
    template_name = 'logout.html'


class EmployeeCreateView(LoginRequiredMixin,
                         CreateView):
    model = Employee
    template_name = 'create.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.uuid = get_uuid()
            employee.save()
            url_bot = BOT_PATH + '?start=' + employee.uuid
            return render(request, 'uuid.html', {'url_bot': url_bot})
        return render(request, 'create.html', {'form': form})


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
