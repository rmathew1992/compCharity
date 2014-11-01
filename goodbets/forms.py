from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from goodbets.models import User, Charity

class ChallengeForm(forms.Form):
    challenger = forms.CharField()
    title = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.TextInput)
    bet_amount = forms.FloatField(min_value=0)
    challengees = forms.ModelMultipleChoiceField(User.objects.all())
    charity = forms.ModelChoiceField(Charity.objects.all())
    # django-crispy-forms
    # gist example: 
    # https://github.com/maraujop/django-crispy-forms#example
    # https://gist.github.com/maraujop/1838193
    helper = FormHelper()
    helper.form_id = "Wrapper"
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        # in app.js, the elements of id='status' will take on value = request.name
        Field('challenger', type='hidden', id='challenger'),
        Field('title', css_class='input-xlarge'),
        Field('challengees', css_class='input-xlarge'),
        Field('charity', css_class='input-xlarge'),
        Field('bet_amount'),
        Field('description', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )
