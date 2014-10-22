from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, render
from goodbets.forms import ChallengeForm
# from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# from django.core.urlresolvers import reverse_lazy
from goodbets.models import Challenge


def index(request):
    return TemplateResponse(request,'index.html')

def profile(request):
	return TemplateResponse(request,'profile.html')

def challenge(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ChallengeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print "I'm Valid Bitches!"
            # redirect to a new URL:
            return HttpResponseRedirect('/profile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ChallengeForm()

    return render(request, 'challenge.html', {'form': form})


# class ChallengeCreate(CreateView):
# 	model = Challenge
# 	fields = ['title', 'description', 'bet', 'challengees']

# class ChallengeUpdate(UpdateView):
# 	model = Challenge
# 	fields = ['title', 'description', 'bet', 'challengees']

# class ChallengeDelete(DeleteView):
#     model = Challenge
#     success_url = reverse_lazy('challenge-list')
    
# class ChallengeView(FormView):
# 	template_name = 'challenge.html'
# 	form_class = ChallengeForm
# 	success_url = '/profile/'

# 	def form_valid(self, form):
# 		# This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         # DO STUFF (i.e CRUD to DB)
# 		return super(ChallengeView, self).form_valid(form)