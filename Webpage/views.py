from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Laptop, Processor, GraphicsCard, StorageDrive, RAM, Display


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

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_laptops': num_laptops, 'num_processors': num_processors,
                 'num_nvidia_graphics_cards': num_nvidia_graphics_cards, 'num_graphics_cards': num_graphics_cards},
    )

class LaptopListView(generic.ListView):
    model = Laptop
    paginate_by = 10


class LaptopDetailView(generic.DetailView):
    model = Laptop


class ProcessorDetailView(generic.DetailView):
    model = Processor