from django import forms

class ChallengeForm(forms.Form):
	title = forms.CharField(max_length=150)
	description = forms.CharField(widget=forms.Textarea)
	bet = forms.FloatField()
	challengees = forms.CharField()