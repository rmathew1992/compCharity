from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class ChallengeForm(forms.Form):
    title = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea)
    bet = forms.FloatField()
    challengees = forms.CharField()

    # django-crispy-forms
    # gist example: 
    # https://github.com/maraujop/django-crispy-forms#example
    # https://gist.github.com/maraujop/1838193
    helper = FormHelper()
    helper.form_id = "Wrapper"
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('title', css_class='input-xlarge'),
        Field('description', css_class='input-xlarge'),
        AppendedText('bet', '.00'), # dollars x, $x.00
        PrependedText('challengees', '@'),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )