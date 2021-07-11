from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import joblib
from .f import SignUpForm
import pickle
# Create your views here.
def home(request):
    return render(request, "home.html", {})


def login_user(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ("login Successful")) 
                return redirect("form")       
            else:
                messages.success(request, ("Login Failed"))
                return redirect("register")
                 
        
    else:
        return render(request,'login.html',context={})

    
def csv(request):
    return render(request, "csv.html",)

def logout_user(request):
    messages.success(request, ('you have been logged out'))
    return redirect ('login')

def student_page(request):
    return render(request, "form.html")

def student_result(request):
    return render(request, "result.html")



def register_user(request):
    if request.method == "POST":
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ('You have Registered'))
            return redirect ('home')
    else:
        form = SignUpForm()
    context = {'form' : form}
    return render(request, 'register.html', context)

#def getPredictions(English, Mathematics, Agricultural_Science, Basic_Science, Basic_Technology, Business_Studies,Social_Studies):
    print('hello world')
    classifier = pickle.load(open("school_recom\classes.sav"))

    prediction = classifier.predict([English, Mathematics, Agricultural_Science, Basic_Science, Basic_Technology, Business_Studies,Social_Studies])

# def result(request):
#     English = int(request.GET['English'])
#     Mathematics = int(request.GET['Mathematics'])
#     Agricultural_Science = int(request.GET['Agricultural_Science'])
#     Basic_Science = int(request.GET['Basic_Science'])
#     Basic_Technology = int(request.GET['Basic_Technology'])
#     Business_Studies = int(request.GET['Business_Studies'])
#     Social_Studies = int(request.GET['Social_Studies'])
    
#     result = getPredictions(English, Mathematics, Agricultural_Science, Basic_Science, Basic_Technology, Business_Studies, Social_Studies)
#     return render(request, 'result.html', {"result": result})

# reload= joblib.load('./school_recom/models/classification_work3.pkl')

def result(request):
    print (request)
    if request.method == 'POST':
        temp = {}
        temp['English']=request.POST.get('English')
        temp['MAthematics']=request.POST.get('MAthematics')
        temp['Agricultural_Science']=request.POST.get('Agricultural_Science')
        temp['Basic_Science']=request.POST.get('Basic_Science')
        temp['Basic_Technology']=request.POST.get('Basic_Technology')
        temp['Business_Studies']=request.POST.get('Business_Studies')
        temp['Social_Studies']=request.POST.get('Social_Studies')

    
    context = {'a':'Hello New world'}
    return render(request,'result.html',context)
    


