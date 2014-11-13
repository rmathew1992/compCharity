
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect, render_to_response
from goodbets.forms import ChallengeForm
from django.forms import ModelForm
from goodbets.models import User, Challenge, Chipin
from paypal.standard.forms import PayPalPaymentsForm
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
            #print "Zoher is the dumps"
            #print username
            username = username.encode('utf-8')
            # Store user to session
            # request.session["username"] = username

            # If the user does not exist save to DB
            if not User.objects.filter(username=username).exists():
                User(username=username).save()

            meh = User.objects.get(username=username)
            meh.is_active = True
            meh.save()
            print "Zoher zoher"
            print meh
            print meh.is_active
    except Exception as e:
        print e
    user_list = User.objects.all()
    challenge_list = Challenge.objects.all()
    chipin_list = Chipin.objects.all()
    context = {
        'user_list': user_list, 
        'challenge_list': challenge_list, 
        'chipin_list': chipin_list,
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
            # Get Session User
            challenger_name = form.cleaned_data['challenger']
            session_user = User.objects.get(username=challenger_name)

            # Create Chipin
            new_chipin = Chipin(
                user=session_user,
                amount=form.cleaned_data['chipin_amount']
                )
            new_chipin.save()
            
            # Create Challenge
            new_challenge = Challenge(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                charity=form.cleaned_data['charity'],
                )
            new_challenge.save()

            # Associate Chipin with Challenge
            new_challenge.chipins.add(new_chipin)

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
    challenge_list = Challenge.objects.all()
    context = {
        'challenge_list': challenge_list, 
        'request': request,
    }
    return render(request, 'feed.html', context)

def paypal_test(request):
    # What you want the button to do.
    paypal_dict = {
        "business": "a@a.com",
        "amount": "00.01",
        "item_name": "the feeling of goodnesss in your heart",
        "invoice": "unique-invoice-id",
        "notify_url": "https://www.example.com",
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        "form": form,
        'request': request,
    }
    return render_to_response("payment.html", context)

def material(request):
    return render(request, 'material-demo.html')
