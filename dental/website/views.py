from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_details(request):
    return render(request, 'blog-details.html', {})


def contact(request):
    # activates if somebody post stuff (fills out the form)
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(message_name, message, message_email, ['example@gmail.com'], fail_silently=False)

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def service(request):
    return render(request, 'service.html', {})