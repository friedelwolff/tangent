from collections import defaultdict
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from employees.api import get_client_class


class IndexView(TemplateView):
    template_name = 'index.html'


class EmployeesListView(LoginRequiredMixin, TemplateView):
    login_url = '/auth/login/'
    template_name = 'employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = get_client_class().from_request(self.request)
        employees = client.get_employees()
        context['employees'] = employees
        #TODO: pagination
        return context


class EmployeeStatsView(LoginRequiredMixin, TemplateView):
    login_url = '/auth/login/'
    template_name = 'statistics.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.today = date.today()

    def _date_soon(self, d):
        """Helper function to say if the given date is in the next month."""
        today = self.today
        d = date.fromisoformat(d)
        d = date(today.year, d.month, d.day)
        if d < today:
            d = date(today.year + 1, d.month, d.day)
        delta = d - today
        return delta.days < 28

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = get_client_class().from_request(self.request)
        employees = client.get_employees()

        context['n_employees'] = len(employees)

        next_birthdays = []
        employees_by_position = defaultdict(list)
        no_position =  []
        employees_by_level = defaultdict(list)
        no_level =  []
        for e in employees:
            birth_date = e['birth_date']
            if birth_date and self._date_soon(birth_date):
                next_birthdays.append(e)

            position = e['position']
            if position:
                employees_by_position[position['name']].append(e)
                employees_by_level[position['level']].append(e)
            else:
                no_position.append(e)
                no_level.append(e)

        # We add this afterwards so that it appears last:
        if employees_by_position:
            employees_by_position["(no position)"] = no_position
            employees_by_level["(no level)"] = no_level

        context['next_birthdays'] = next_birthdays
        context['employees_by_position'] = dict(employees_by_position)
        context['employees_by_level'] = dict(employees_by_level)

        return context

