from django import forms


GENDERS = {
        'M': 'Male',
        'F': 'Female',
}

RACES = {
        'B': 'Black',
        'C': 'Coloured',
        'I': 'Indian or Asian',
        'W': 'White',
        'N': 'None dominant',
}

REVIEW_TYPES = {
        'P': 'Performance increase',
        'S': 'Starting salary',
        'A': 'Anual increase',
        'E': 'Expectation review',
}


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
        (None, ''),) + tuple(GENDERS.items()))
    race = forms.ChoiceField(required=False, choices=(
        (None, ''),) + tuple(RACES.items()))
