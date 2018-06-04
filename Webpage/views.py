from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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


class LikedLaptopsByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = LaptopInstance
    template_name = 'Webpage/laptopinstance_list_liked_user.html'
    paginate_by = 10

    def get_queryset(self):
        return LaptopInstance.objects.filter(user=self.request.user).filter(status__exact='l')


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