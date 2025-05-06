from django.shortcuts import render , redirect
from .models import Tweet
from .forms import TweetForm , userRegistrationForm, ProfileEditForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 
from django.contrib import messages

from .models import Profile


# Create your views here

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form=TweetForm(request.POST, request.FILES )
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form=TweetForm()
    return render(request, 'tweet_form.html', {'form':form})

@login_required
def tweet_edit(request, tweet_id):
    tweet_instance = get_object_or_404(Tweet , id=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet_instance)
        if form.is_valid():
            tweets=form.save(commit=False)
            tweets.user=request.user
            tweets.save()
            # form.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet_instance)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet_instance = Tweet.objects.get(id=tweet_id)
    if request.method == 'POST':
        tweet_instance.delete()
        return redirect("tweet_list")
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet_instance})

def register(request):
    if request.method == 'POST':
        form=userRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)# save the form data to the database
            user.set_password(form.cleaned_data['password1'])# set the password
            user.save()# save the user to the db
            login(request, user)# login the user 
            return redirect('tweet_list')
    else:
        form=userRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})


 # Import your Tweet model

def search_tweet(request):
    query = request.GET.get('q')  # Get the search query from the URL
    results = Tweet.objects.none()  # Initialize empty queryset 
    if query:
        results = Tweet.objects.filter(text__icontains=query)  # Search in 'content' field
    return render(request, 'search_tweet.html', {'results': results, 'query': query})

#profile

@login_required
def user_profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ProfileEditForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form})
   