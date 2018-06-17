from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

from .models import Laptop, Processor, GraphicsCard, StorageDrive, RAM, Display, DreamLaptop


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_laptops = Laptop.objects.all().count()
    num_processors = Processor.objects.all().count()
    # Available books (status = 'a')
    num_nvidia_graphics_cards = GraphicsCard.objects.filter(manufacturer='Nvidia').count()
    num_graphics_cards = GraphicsCard.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_laptops': num_laptops, 'num_processors': num_processors,
                 'num_nvidia_graphics_cards': num_nvidia_graphics_cards, 'num_graphics_cards': num_graphics_cards, 'num_visits':num_visits}, # num_visits appended
    )

class LaptopListView(generic.ListView):
    model = Laptop
    paginate_by = 10


class LaptopDetailView(generic.DetailView):
    model = Laptop


class ProcessorDetailView(generic.DetailView):
    model = Processor


class GraphicsCardDetailView(generic.DetailView):
    model = GraphicsCard


class RamDetailView(generic.DetailView):
    model = RAM


class StorageDriveDetailView(generic.DetailView):
    model = StorageDrive


class DisplayDetailView(generic.DetailView):
    model = Display


class DreamLaptopDetailView(generic.DetailView):
    model = DreamLaptop



from .models import Favorite
from .forms import FavoriteForm
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.middleware.csrf import get_token
from django.conf import settings

class FavAlterView(FormView):

    """
    Enables authenticated users to Favorite/Unfavorite objects.
        getattr method sets default values for POSITIVE_NOTATION,
    NEGATIVE_NOTATION, ALLOW_ANONYMOUS in the case they are not
    set in settings.py
    """

    form_class = FavoriteForm
    model = Favorite
    template_name = 'fav/fav_form.html'

    def form_valid(self, form):
        fav_value = self.request.POST['fav_value']
        csrf_token_value = get_token(self.request)
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        try:
            content_type = ContentType.objects.get(app_label=self.request.POST['app_name'], model=self.request.POST['model'].lower())
            model_object = content_type.get_object_for_this_type(id=self.request.POST['model_id'])
            if fav_value == getattr(settings, 'POSITIVE_NOTATION', 'Favorite'):
                fav = form.save(commit=False)
                fav.content_object = model_object
                if self.request.user.is_authenticated:
                    fav.save()
                else:
                    if getattr(settings, 'ALLOW_ANONYMOUS', 'TRUE') == "TRUE":
                        fav.cookie = self.request.session.session_key
                        fav.save()
                    else:
                        return JsonResponse({
                            'success': 0,
                            'error': "You have to sign in "})
                Favorite.objects.get(id=fav.id)
            else:
                if self.request.user.is_authenticated:
                    Favorite.objects.get(
                        object_id=model_object.id,
                        user=self.request.user,
                        content_type=content_type).delete()
                elif getattr(settings, 'ALLOW_ANONYMOUS', 'TRUE') == "TRUE":
                    Favorite.objects.get(
                        object_id=model_object.id,
                        cookie=self.request.session.session_key,
                        content_type=content_type).delete()
        except Exception as e:
            print("type error: " + str(e))
            print('type is:', e.__class__.__name__)
            return JsonResponse({
                'success': 0,
                'error': "You have to sign in "})
        return JsonResponse({"csrf": csrf_token_value})

    def form_invalid(self, form):
        return JsonResponse({
            'success': 0,
            'error': form.errors})


class FavoritedLaptopsByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing laptops favorited to current user.
    """
    model = Laptop
    template_name = 'Webpage/laptop_list_favorited_user.html'
    paginate_by = 10

    def get_queryset(self):
        #return Laptop.objects.filter(person=self.request.user).filter(status__exact='l')
        return Laptop.objects.filter(favorites__in=Favorite.objects.filter(user=self.request.user))


class AllFavoritedLaptopsByUsersListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing laptops favorited to current user.
    """
    permission_required = 'Webpage.can_see_all_favorited'
    model = Laptop
    template_name = 'Webpage/laptop_list_all_favorited_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Laptop.objects.filter(favorites__in=Favorite.objects.all())


class LaptopCreate(CreateView, PermissionRequiredMixin):
    permission_required = 'Webpage.can_create_laptop'
    model = Laptop
    fields = ['model_name', 'brand_name', 'width', 'height', 'depth', 'weight', 'processor', 'graphics_card', 'ram', 'storage_drive', 'display', 'operating_system', 'date_of_release']


class DreamLaptopCreate(CreateView, PermissionRequiredMixin):
    permission_required = 'Webpage.can_create_dream_laptop'
    model = DreamLaptop
    fields = ['name', 'weight', 'processor', 'graphics_card', 'ram', 'storage_drive', 'display', 'operating_system', 'description']

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(DreamLaptopCreate, self).form_valid(form)


class UserDreamLaptopListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'Webpage.can_create_dream_laptop'
    model = DreamLaptop
    template_name = 'Webpage/dreamlaptop_user_list.html'
    paginate_by = 10

    def get_queryset(self):
        return DreamLaptop.objects.filter(user=self.request.user)


class AllUsersDreamLaptopListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'Webpage.can_see_all_dream_laptops'
    model = DreamLaptop
    template_name = 'Webpage/alldreamlaptops_users_list.html'
    paginate_by = 10

    def get_queryset(self):
        return DreamLaptop.objects.all()
