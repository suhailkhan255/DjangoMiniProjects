from django.contrib.auth import authenticate, logout, login
from .EmailBackEnd import EmailBackEnd

from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages


# Create your views here.
def Registration(request):
    return render(request, 'registration.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'), )

        print("use authentication done ", user)
        if user is not None:
            login(request, user)
            user = CustomUser.objects.get(email=request.POST.get('email'))
            # Pass the users queryset to the template for rendering
            context = {'user': user}
            return render(request, 'userhome.html', context)


        else:
            print('invalid user')
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')


def save_user_profile(request):
    if request.method == 'POST':
        # Retrieve data from the form
        profile_picture = request.FILES.get('profile_picture')
        description = request.POST.get('description')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        nationality = request.POST.get('nationality')
        pan_number = request.POST.get('pan_number')
        gstin_number = request.POST.get('gstin_number')
        password = request.POST.get('password')

        # Create a new CustomUser instance
        user = CustomUser(
            profile_picture=profile_picture,
            description=description,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            nationality=nationality,
            pan_number=pan_number,
            gstin_number=gstin_number,
            username=first_name + last_name,
            password=password
        )
        # Save the user instance
        user.save()
        messages.success(request, 'Profile saved successfully!')
        return redirect('login')  # Replace 'profile_page' with your actual profile page URL name

    return render(request, 'your_template.html')  # Replace 'your_template.html' with the path to your template
