from collections import defaultdict
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from employees.api import get_client_class
from employees import forms


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
        for e in employees:
            birth_date = e['birth_date']
            if birth_date and self._date_soon(birth_date):
                next_birthdays.append(e)

            position = e['position']
            if position:
                name = position['name']
                if position['level']:
                    name = "{name} ({level})".format(**position)
                employees_by_position[name].append(e)
            else:
                no_position.append(e)

        # We add this afterwards so that it appears last:
        if employees_by_position:
            employees_by_position["(no position)"] = no_position

        context['next_birthdays'] = next_birthdays
        context['employees_by_position'] = dict(employees_by_position)

        return context


class SearchView(LoginRequiredMixin, TemplateView):
    login_url = '/auth/login/'
    template_name = 'employees.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = forms.SearchForm(request.GET)
        context["form"] = form
        if form.is_valid() and 'position' in request.GET:
            # the parameters were passed, so we need to search:
            data = form.cleaned_data
            client = get_client_class().from_request(self.request)
            employees = client.employees_search(params=data)
            context["employees"] = employees

        return self.render_to_response(context)


class MyProfileView(LoginRequiredMixin, TemplateView):
    login_url = '/auth/login/'
    template_name = 'myprofile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = get_client_class().from_request(self.request)
        profile = client.get_my_profile()
        #replace a few values with better alternatives:
        profile['gender'] = forms.GENDERS.get(profile.pop('gender'), None)
        profile['race'] = forms.RACES.get(profile.pop('race'), None)
        for review in profile['employee_review']:
            review['type'] = forms.REVIEW_TYPES.get(review.pop('type'), None)
        context['profile'] = profile
        context['github_avatar_url'] = client.github_avatar_url(profile['github_user'])

        return context
