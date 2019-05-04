from django.views.generic.base import TemplateView

from employees.api import WebAPIClient


class IndexView(TemplateView):
    template_name = 'index.html'


class EmployeesListView(TemplateView):
    template_name = 'employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = WebAPIClient.from_request(self.request)
        employees = client.get_employees(self.request)
        context['employees'] = employees
        #TODO: pagination
        return context

