
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from goodbets.forms import ChallengeForm
from django.forms import ModelForm
from goodbets.models import User, Challenge, Bet
import logging
logger = logging.getLogger(__name__)

def index(request):
    return TemplateResponse(request,'index.html')

def login(request):
    return TemplateResponse(request,'login.html')

def profile(request):
   if request.method == 'GET':
    try:
        rgv = request.GET.values()
        logger.debug('requestgetvalues: %s' % rgv)
        if len(rgv) == 1 and rgv[0] != '':
            # Turn FB name into "First Last" format
            username = rgv[0]
            username = username.encode('utf-8')
            # Store user to session
            request.session["username"] = username
            # If the user does not exist save to DB
            if not User.objects.filter(username=username).exists():
                User(username=username).save()
    except Exception as e:
        print e
    user_list = User.objects.all()
    challenge_list = Challenge.objects.all()
    bet_list = Bet.objects.all()
    context = {
        'user_list': user_list, 
        'challenge_list': challenge_list, 
        'bet_list': bet_list,
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
            
            # # charity debug
            # print "charity: ", form.cleaned_data['charity']
            # print type(form.cleaned_data['charity']) # works
            # challengees debug
            # print type(form.cleaned_data['challengees'])
            # for c in form.cleaned_data['challengees']:
            #     print type(c)
            
            # Get Session User
            challenger_name = form.cleaned_data['challenger']
            session_user = User.objects.get(username=challenger_name)

            # Create Bet
            new_bet = Bet(
                user=session_user,
                amount=form.cleaned_data['bet_amount']
                )
            new_bet.save()
            
            # Create Challenge
            new_challenge = Challenge(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                charity=form.cleaned_data['charity'],
                )
            new_challenge.save()

            # Associate Bet with Challenge
            new_challenge.bets.add(new_bet)

            # Associate Challengees with Challenge
            for challengee in form.cleaned_data['challengees']:
                new_challenge.challengees.add(challengee)

            # Update Challenge associations
            new_challenge.save()
            
            # redirect to a new URL:
            return redirect('profile')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ChallengeForm()

    return render(request, 'challenge.html', {'form': form, 'request': request})

def home(request):
    return render(request, 'home.html', {'request': request})

def about(request):
    return render(request, 'about.html', {'request': request},)
def feed(request):
    user_list = User.objects.all()
    challenge_list = Challenge.objects.all()
    context = {
        'user_list': user_list, 
        'challenge_list': challenge_list, 
        'request': request,
    }
    return render(request, 'feed.html', context)



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



