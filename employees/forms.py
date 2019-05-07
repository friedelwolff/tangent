from django import forms


class SearchForm(forms.Form):
    email__contains = forms.CharField(required=False)
    position = forms.ChoiceField(required=False, choices=(
        (None, ''),
        ('2', 'Back-end Developer (Junior)'),
        ('1', 'Front-end Developer (Senior)'),
        ('3', 'Project Manager (Senior)'),
        ('4', 'Projct Manager (Junior)'),
    ))
    gender = forms.ChoiceField(required=False, choices=(
        (None, ''),
        ('M', 'Male'),
        ('F', 'Female'),
    ))
    race = forms.ChoiceField(required=False, choices=(
        (None, ''),
        ('B', 'Black'),
        ('C', 'Coloured'),
        ('I', 'Indian or Asian'),
        ('W', 'White'),
        ('N', 'None dominant'),
    ))
