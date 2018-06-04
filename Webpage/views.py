from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

from .models import Laptop, Processor, GraphicsCard, StorageDrive, RAM, Display, LaptopInstance


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


class LikedLaptopsByUserListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing laptops liked to current user.
    """
    permission_required = 'Webpage.can_mark_liked'
    model = LaptopInstance
    template_name = 'Webpage/laptopinstance_list_liked_user.html'
    paginate_by = 10

    def get_queryset(self):
        return LaptopInstance.objects.filter(person=self.request.user).filter(status__exact='l')


class DislikedLaptopsByUserListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing laptops disliked to current user.
    """
    permission_required = 'Webpage.can_mark_disliked'
    model = LaptopInstance
    template_name = 'Webpage/laptopinstance_list_disliked_user.html'
    paginate_by = 10

    def get_queryset(self):
        return LaptopInstance.objects.filter(person=self.request.user).filter(status__exact='d')



class AllLikedLaptopsByUsersListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing all laptops liked to staff users.
    """
    permission_required = 'Webpage.can_see_all_liked'
    model = LaptopInstance
    template_name = 'Webpage/laptopinstance_list_all_liked_users.html'
    paginate_by = 10

    def get_queryset(self):
        return LaptopInstance.objects.filter(status__exact='l')


class AllDislikedLaptopsByUsersListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing all laptops disliked to staff users.
    """
    permission_required = 'Webpage.can_see_all_disliked'
    model = LaptopInstance
    template_name = 'Webpage/laptopinstance_list_all_disliked_users.html'
    paginate_by = 10

    def get_queryset(self):
        return LaptopInstance.objects.filter(status__exact='d')


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