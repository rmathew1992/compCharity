from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from goodbets.models import User, Charity

class ChallengeForm(forms.Form):
    challenger = forms.CharField()
    title = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.TextInput)
    chipin_amount = forms.FloatField(min_value=0)
    challengees = forms.ModelMultipleChoiceField(User.objects.all())
    charity = forms.ModelChoiceField(Charity.objects.all())
    # django-crispy-forms
    # gist example: 
    # https://github.com/maraujop/django-crispy-forms#example
    # https://gist.github.com/maraujop/1838193
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    # bootstrap stuff
    # http://stackoverflow.com/questions/19865158/what-is-the-difference-among-col-lg-col-md-and-col-sm-in-twitter-bootstra
    helper.label_class = 'col-lg-2 control-label'
    helper.field_class = 'col-lg-8 control-label' # form-control
    helper.form_id = "Wrapper"
    helper.layout = Layout(
        # in app.js, the elements of id='status' will take on value = request.name
        Field('challenger', type='hidden', id='challenger'),
        Field('title'),
        Field('challengees'),
        Field('charity'),
        Field('chipin_amount'),
        Field('description'),
        Div(FormActions(
                Submit('save_changes', 'Save changes', css_class="btn btn-primary"),
                Submit('cancel', 'Cancel', css_class="btn btn-default"),
            ),
            css_class="col-lg-10 col-lg-offset-2")
    )
