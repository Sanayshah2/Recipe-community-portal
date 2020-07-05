from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponse
from.models import Food
from.models import Category, Comment
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from users.models import Subscriber,Profile

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user}, your account has been created successfully! Please log in to your account.')
            return redirect('/myapp/')
    else:
        form=UserCreationForm()
        return render(request,'myapp/signup.html',{'form':form})







def home(request):
    dict_1={
        '01':2,
        '02':3,

    }   

    for key in dict_1:
        dict_1[key]=dict_1[key]+1
    
    
    return render(request,'myapp/home.html',{'dict_1':dict_1}) 

def index(request):
    category1=Category.objects.all()   
    food=Food.objects.all()
    
    context={
        'food':food,
        'category' : category1
    }
    return render(request,'myapp/index.html',context)


def foodview(request, cname, myid, recipename):
    food=Food.objects.get(id=myid)
    ing=food.ingredients.splitlines()
    if food.author != request.user:
        food.visits=food.visits+1
    food.save()
    number=food.visits
    allfoods=Food.objects.all()
    f=food.id
    name = food.category
    food.category=name
    comments=Comment.objects.filter(food=f)
    
    

    rating=0
    d=0
    if comments:
        for c in comments:
            rating=rating+c.rating
            d=d+1
        rate=rating/d
        rate=rate+1
        if rate > 5:
            rate=rate-1
        rate1=int(rate)

    else:
        rate1=0
    
    
    
    context={
        'food1':food,
        'comments':comments,
        'rate':range(rate1),
        'allfoods':allfoods,
        'count':number,
        'ing':ing,
    }
    return render(request,'myapp/foodview.html',context)

def recipes(request):
    category1=Category.objects.all()   
    food=Food.objects.all()
    context={
        'food':food,
        'category' : category1,
    }
    return render(request,'myapp/recipes.html',context)

def categoryview(request,cid,cname):
    category1=Category.objects.get(id=cid)   
    categoryname=category1.name
    food=Food.objects.filter(category=categoryname)
    context={
        'food':food,
        'category' : category1,
    }
    return render(request,'myapp/categoryview.html',context)


@login_required
def foodform(request, profilename):
    profile=Profile.objects.get(user=request.user)
    if request.method == 'POST':

        
        form=FoodForm(request.POST, request.FILES)
        

        if form.is_valid():
            
            instance=form.save(commit=False)
            instance.author=request.user
            instance.count=0
            instance.save()
            name = form.cleaned_data.get('name')
            
             
            subs=Subscriber.objects.filter(to_name=profile.id)
            for s in subs:
                send_mail(
                '',    
                f'Hey {s.name},a new recipe of {name} was just uploaded by {request.user}',
                'feastrecipes69@gmail.com',
                [s.email],    
                fail_silently = True
                )

            messages.success(request, f'Your recipe, {name} has been added successfully.Go to Recipes page and select your category and view your added recipe.')
            return redirect('home')
    
    else:
        form=FoodForm()
    return render(request,'myapp/foodform.html',{'form':form,'profile':profile})

#@login_required    
#def addcategory(request, profilename):
 #   if request.method == 'POST':
  #      categoryname = request.POST.get("categoryname")
   #     categoryimage = request.POST.get("categoryimage")
    #    newcategory = Category(name=categoryname, image=categoryimage)
     #   newcategory.save()
      #  messages.success(request, f'Your category has been added. Now add your recipe.')
       # return redirect(reverse('foodform', kwargs={'profilename':profilename}))

def addComment(request,myid, recipename, cname):
        food = get_object_or_404(Food,id = myid)

        if request.method == "POST":
            comment_author = request.POST.get("comment_author")
            comment_content = request.POST.get("comment_content")
            rating = request.POST.get('rating')
           
            newComment = Comment(author  = comment_author, comment = comment_content, rating=rating)
            newComment.food = food
            newComment.save()
        return redirect(reverse("foodview",kwargs={"myid":myid, 'cname' : cname, 'recipename' : recipename}))
    
@login_required
def updaterecipe(request,myid, recipename, cname):
    food = get_object_or_404(Food,id = myid)
    form = RecipeEditForm(request.POST, request.FILES, instance = food)
    if request.method == 'POST':
        if form.is_valid():
                food = form.save(commit=False)
                food.author=request.user
                name = form.cleaned_data.get('name')
                food.save()
                messages.success(request, f'Your recipe {name} has been updated.')
                return redirect(reverse("foodview", kwargs={"myid": myid, "recipename":recipename, 'cname':cname}))
    return render(request, 'myapp/editrecipe.html', {'form' : form})

@login_required
def deleterecipe(request, profileid, profilename, myid, cname, recipename):
    food = Food.objects.get(id=myid)
    name = food.name
    food.delete()
    messages.success(request, f'Your recipe, {name}, was deleted successfully!')
    return redirect('home')
    #return redirect('profile', kwargs={'profileid':profileid, 'profilename':profilename})


def modaltest(request):
    return render(request,'myapp/modal.html')