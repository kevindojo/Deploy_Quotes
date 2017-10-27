from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.contrib.messages import error


# Create your views here.

def index(request):
    return render(request,'quotes/index.html')


def create(request):
    errors= User.objects.validate_registration(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/')
    else:
        user = User.objects.valid_user(request.POST)
        request.session['user_id'] = user.id
        #keeps track of the current user_id that is "logged in", 
        # you can directly use it as argument, no need to pass into parameters: def example(x,y):
        messages.success(request, "registered")
        return redirect ('/success')



def login(request):
    errors= User.objects.validate_login(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/')
    else:
        user = User.objects.valid_login(request.POST)
        request.session['user_id'] = user.id
        messages.success(request, "Logged in")
        return redirect('/success')



def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'quotes/success.html', context)




################  END END LOGIN END END  ################################################################################



################  QUOTES START  #########################################################################################


def home(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])
    quotes = Quote.objects.filter(favorite=user)
    #many to many 
    context = {
        'recent_quotes': Quote.objects.order_by('-created_at')[0:4].all(),  #matches over in html
        'favorite': quotes
    }
    return render(request, 'quotes/home.html', context)


def add(request):
    errors= Quote.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/home')

    else:   #create into database
        Quote.objects.create(
            author= request.POST['author'],
            description= request.POST['description'],
            user_upload_id = request.session['user_id'],   # this makes id for ForeignKey
        )
    return redirect('/home')


def user_page(request,id):
    user = User.objects.get(id=id)
    quote = Quote.objects.filter(user_upload = user)
    #displays the quotes of the specific user after calling the "user" on previous line.
    # one to many
    count = quote.count()
    context = {
        'user': user,
        'upload_quote': quote,
        'counter': count,
    }
    return render(request, 'quotes/user_page.html', context)




def favorite(request,quote_id):
    User.objects.get(id=request.session['user_id']).user_favorite.add(Quote.objects.get(id=quote_id))
    #many to many using "related_name"
    return redirect('/home')





def remove(request, quote_id):  # () parameter, inside are called arguments
    Quote.objects.get(id=quote_id).favorite.remove(User.objects.get(id=request.session['user_id']))
    return redirect('/home')
    #request.session does not need to be passed into the parameter



def logout(request):
    context = {
        'logout': request.session.pop('user_id')
    }
    return render(request,'quotes/index.html', context)