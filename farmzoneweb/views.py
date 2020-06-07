# Create your views here.
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import NewUserForm

User = get_user_model()


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'index.html')


def about(request):
    """

    :param request:
    :return:
    """
    return render(request, 'about.html')


def contact(request):
    """

    :param request:
    :return:
    """
    return render(request, 'contact.html')


def forum(request):
    """

    :param request:
    :return:
    """
    return render(request, 'forum_home.html')


def listings(request):
    """

    :param request:
    :return:
    """
    return render(request, 'listings.html')


def listing_single(request):
    """

    :param request:
    :return:
    """
    return render(request, 'listings-single.html')

    # def login(request):
    """

    :param request:
    :return:
    """


#    return render(request, 'accounts/login.html')


def post_item(request):
    """

    :param request:
    :return:
    """
    return render(request, 'postitem.html')


def profile(request):
    """

    :param request:
    :return:
    """
    return render(request, 'accounts/profile.html')


def register(request):
    """

    :param request:
    :return:
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("farmzoneweb:index")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="accounts/register.html",
                          context={"form": form})

    form = NewUserForm
    return render(request=request,
                  template_name="accounts/register.html",
                  context={"form": form})


def login(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="accounts/login.html",
                  context={"form": form})


def logout(request):
    """

    :param request:
    :return:
    """
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("farmzoneweb:index")
