from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import  messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm,UserUpdateForm
#from user.models import UserProfile


@login_required(login_url='/login') # Check login
def UserProfileView(request):
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'profile':profile}
    return render(request,'user_profile.html',context)

def login_form(request):
    if request.method == 'POST':
        username = request.POST['user-name']
        password = request.POST['user-password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user =request.user
            userprofile=UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            #*** Multi Langugae
            #request.session[translation.LANGUAGE_SESSION_KEY] = userprofile.language.code
            #request.session['currency'] = userprofile.currency.code
            #translation.activate(userprofile.language.code)

            #Redirect to a success page.
            return HttpResponseRedirect('/accounts/')
        else:
            messages.warning(request,"Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/')
    # Return an 'invalid login' error message.

    #category = Category.objects.all()
    context = {#'category': category
     }
    return render(request, 'login.html')

def logout_func(request):
    logout(request)
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]
    #     del request.session['currency']
    return HttpResponseRedirect('/')

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(username,password)
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')


    form = SignUpForm()
    #category = Category.objects.all()
    context = {#'category': category,
               'form': form,
               }
    return render(request, 'signup_form.html', context)

def recover(request):
    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)
    # content = body['content']
    # print(body)
    return render(request,'recover-password.html')

def recover_email(request):
    return render(request,'recover-password_email.html')

def profile(request):
    return render(request,'account-setting.html')


def import_xlsx(request):
    #xlsx_file='C://Users//Vishnu Porno//Downloads//Book1.xlsx'
    xlsx_file='C://Users//Vishnu Porno//Downloads//game2.xlsx'
    import openpyxl
    from pathlib import Path

    #xlsx_file = Path('SimData', 'play_data.xlsx')
    wb_obj = openpyxl.load_workbook(xlsx_file)
    sheet = wb_obj.active
    # msg= 'False'
    # if msg =='Done':
    #   msg ='File has been uploaded'
    # if msg =='False':
    #     msg ='File is not uploaded'
    return render(request,'xlsx.html',{'sheet':sheet})
