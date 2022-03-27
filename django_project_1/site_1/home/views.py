from django.views.generic import ListView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm

from .forms import UserRewiwesForm

from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Reviews

# Меню


def home_page(request):
    return render(request, 'home/home.html')


def ascent(request):
    return render(request, 'home/ascent.html')


def trekking(request):
    return render(request, 'home/trekking.html')


def clients(request):
    return render(request, 'home/clients.html')


def contacts(request):
    return render(request, 'home/contacts.html')


def about(request):
    return render(request, 'home/about.html')


# Регистрация и вход
def sign_up(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():

            user = User.objects.create_user(username=user_form.data['username'],
                                            email=user_form.data['email'],
                                            password=user_form.data['password'])
            login(request, user)
            return redirect('home')
    else:
        user_form = RegisterUserForm()
    return render(request, 'home/sign_up.html', {'user_form': user_form})


# Выпадающее меню

# Восхождения
def aragats(request):
    return render(request, 'home/in_menu/ascent/aragats.html')


def ararat(request):
    return render(request, 'home/in_menu/ascent/ararat.html')


def elbrus(request):
    return render(request, 'home/in_menu/ascent/elbrus.html')


def kazbek(request):
    return render(request, 'home/in_menu/ascent/kazbek.html')


def kilimanjaro(request):
    return render(request, 'home/in_menu/ascent/kilimanjaro.html')


def lenin_peak(request):
    return render(request, 'home/in_menu/ascent/lenin_peak.html')


def manaslu(request):
    return render(request, 'home/in_menu/ascent/manaslu.html')


def monblan(request):
    return render(request, 'home/in_menu/ascent/monblan.html')


def peak_separate(request):
    return render(request, 'home/in_menu/ascent/peak_separate.html')

# Треккинг


def arround_annapurna(request):
    return render(request, 'home/in_menu/trakking/arround_annapurna.html')


def lician_path(request):
    return render(request, 'home/in_menu/trakking/lician_path.html')

# Клиентам


def arcticles(request):
    return render(request, 'home/in_menu/clients/arcticles.html')


def clothes_and_equuipment(request):
    return render(request, 'home/in_menu/clients/clothes_and_equuipment.html')


def phisical_training(request):
    return render(request, 'home/in_menu/clients/phisical_training.html')


def question_answer(request):
    return render(request, 'home/in_menu/clients/question_answer.html')


def treaties(request):
    return render(request, 'home/in_menu/clients/treaties.html')

# О нас


def photo(request):
    return render(request, 'home/in_menu/about/photo.html')


class reviews(ListView):
    model = Reviews
    context_object_name = 'reviewes_list'
    try:
        queryset = Reviews.objects.order_by('-date')[:15]
    except:
        paginate_by = 15
    template_name = 'home/in_menu/about/reviews.html'


def send_reviews(request):
    if request.method == 'POST':
        print('request = ', dir(request.POST), request.POST)
        user_form = UserRewiwesForm(request.POST)
        if user_form.is_valid():
            new_review = Reviews(username=request.user,
                                 title=user_form.data['title'],
                                 rewiew=user_form.data['rewiew'])
            new_review.save()
            return redirect('reviews')
    else:
        user_form = UserRewiwesForm()
    return render(request, 'home/in_menu/about/send_reviews.html', {'user_form': user_form})


def video(request):
    return render(request, 'home/in_menu/about/video.html')


def ourteam(request):
    return render(request, 'home/in_menu/about/ourteam.html')
