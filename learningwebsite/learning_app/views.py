from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Question, Answer

# Create your views here.

def homepage(request):
    if request.method == 'GET' and 'signup' in request.GET:
        return redirect('signup')
    return render(request, 'base.html')

def signuppage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user-type']
        # save user info to database
        my_user = User.objects.create_user(name,email,password)
        my_user.save()
        if user_type == 'master':
            return redirect('masterlogin')
        if user_type == 'student':
            return redirect('studentlogin')
        else:
            return HttpResponse('password and confirm password in not matched')
    
    return render(request,'signup.html')

def loginpage(request):
    if request.method == 'POST':
        user_type = request.POST['user-type']

        if user_type == 'master':
            return redirect('masterlogin')
        elif user_type == 'student':
            return redirect('studentlogin')
        else:
            return HttpResponse('password and confirm password in not matched')
    
    return render(request,'signin.html')

def masterloginloginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('masterdashboard')
        else:
            return HttpResponse('username or password incorrect')
    return render(request, "master'slogin.html")


def masterdashboardpage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:  # add this check to ensure title field is not empty
            question = Question.objects.create(title=title, description=description, master=request.user)
            question.save()
    questions = Question.objects.filter(master=request.user)
    context = {'questions': questions}
    return render(request, 'masters_dashboard.html', context)


def studentloginloginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('studentdashboard')
        else:
            return HttpResponse('username or password incorrect')
    
    return render(request, "student'slogin.html")

def studentdashboardpage(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        for question in questions:
            answer_text = request.POST.get('answer' + str(question.id))
            if answer_text:
                answer = Answer.objects.create(
                    text=answer_text,
                    question=question,
                    student=request.user
                )
                answer.save()
        return redirect('student_dashboard')
    context = {'questions': questions}
    return render(request, 'student_dashboard.html', context)



def logout_view(request):
    logout(request)
    return redirect('login')


