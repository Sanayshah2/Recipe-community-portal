from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.models import User
from myapp.models import Food, Category, Comment
from django.contrib.auth.decorators import login_required
from .models import Profile,Subscriber
from .forms import ProfileEditForm, UserEditForm, UserModifiedForm,SubscriptionForm
from django.contrib import messages


def register(request):
    if request.method=='POST':
        form=UserModifiedForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, f'{user}, your account has been created successfully! Please log in to your account.')
            return redirect('login')  
    else: 
        form=UserModifiedForm()
    return render(request, 'users/register.html', {'form' : form})



def profile(request,myid,profilename):
    userprofile = Profile.objects.get(id=myid)
    name = userprofile.user
    recipe = Food.objects.filter(author=name)
    a = Food.objects.filter(author=name).count()
    subscribers=Subscriber.objects.filter(to_name=myid).count()
    c=0
    for f in recipe:
        c= c + f.visits
    
    if request.method=='POST':
        form = SubscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.to_name=userprofile
            instance.save()
            return redirect(reverse("profile",kwargs={"myid":myid, 'profilename' : profilename}))
            
    else:
        form=SubscriptionForm()    
        return render(request, 'users/profile.html', {'userprofile' : userprofile,'c' : c,'form':form,'recipe': recipe, 'count':a,'subscribers':subscribers})


@login_required
def editprofile(request, myid, profilename):
    if request.method == 'POST':
        p_form = ProfileEditForm(request.POST, request.FILES, instance = request.user.profile)
        u_form = UserEditForm(request.POST, instance = request.user)
        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect(reverse("profile", kwargs={"myid": myid, "profilename":profilename}))
    else:
            p_form = ProfileEditForm(instance=request.user.profile)
            u_form = UserEditForm(instance=request.user)
    return render(request, 'users/editprofile.html', {'u_form' : u_form, 'p_form' : p_form})

def chefs(request):
    chefs=Profile.objects.all()

    return render(request,'users/chefs.html',{'chefs': chefs})
    
    