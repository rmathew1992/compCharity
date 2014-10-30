
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, render, redirect
from goodbets.forms import ChallengeForm
from django.forms import ModelForm
from goodbets.models import User, Challenge, Bet


def index(request):
    return TemplateResponse(request,'index.html')

def login(request):
    return TemplateResponse(request,'login.html')

def profile(request):
   if request.method == 'GET':
    try:
        #if the user does not exist save to DB
        if not User.objects.filter(username=request.GET.values()).exists():
            User(username=request.GET.values()).save()
    except Exception as e:
        print e
    user_list = User.objects.all()
    challenge_list = Challenge.objects.all()
    context = {
        'user_list': user_list, 
        'challenge_list': challenge_list, 
        'request': request,
    }
    return render(request, 'profile.html', context)

def challenge(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ChallengeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            # get current User model from Session?
            # current_user = 
            u = User(username='Ryan')
            u.save()            
            new_bet = Bet(user=u, amount=1) # hardcoded for now
            new_bet.save()
            new_challengee0 = User(username='Nitya')
            new_challengee0.save()
            new_challengee1 = User(username='Kevin')
            new_challengee1.save()

            new_challenge = Challenge(title=form.cleaned_data['title'], 
                                      description=form.cleaned_data['description'])
                        
            new_challenge.save()
            new_challenge.bets.add(new_bet)
            new_challenge.challengees.add(new_challengee0)

            new_challenge.save()
            # redirect to a new URL:
            return redirect('profile')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ChallengeForm()

    return render(request, 'challenge.html', {'form': form, 'request': request})

def home(request):
    return render(request, 'home.html', {'request': request})

def material(request):
    return render(request, 'material-demo.html')

# class ChallengeCreate(CreateView):
#   model = Challenge
#   fields = ['title', 'description', 'bet', 'challengees']

# class ChallengeUpdate(UpdateView):
#   model = Challenge
#   fields = ['title', 'description', 'bet', 'challengees']

# class ChallengeDelete(DeleteView):
#     model = Challenge
#     success_url = reverse_lazy('challenge-list')
    
# class ChallengeView(FormView):
#   template_name = 'challenge.html'
#   form_class = ChallengeForm
#   success_url = '/profile/'

#   def form_valid(self, form):
#       # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         # DO STUFF (i.e CRUD to DB)
#       return super(ChallengeView, self).form_valid(form)



