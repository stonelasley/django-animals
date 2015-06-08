from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from animals.models import Animal
from animals.forms import AnimalForm

class Index(ListView):
    context_object_name = 'animals'
    template_name = "animals/list.html"

    def get_queryset(self):
        return Animal.objects.order_by('-created')[:5]

class AnimalNewIndex(ListView):
    context_object_name = 'animals'
    template_name = "animals/list.html"

    def get_queryset(self):
        return Animal.objects.order_by('-created')[:5]

class AnimalDetail(DetailView):
    model = Animal
    template_name = "animals/detail.html"

class AnimalUpdate(UpdateView):
    model = Animal
    template_name = "animals/form.html"
    form_class = AnimalForm
    success_url = '/pups'

class AnimalCreate(CreateView):
    model = Animal
    template_name = "animals/form.html"
    form_class = AnimalForm
    success_url = '/pups'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user.is_authenticated():
            self.object.user = self.request.user
        self.object.save()

        return super(AnimalCreate, self).form_valid(form)

class AnimalDelete(DeleteView):
    model = Animal
    success_url = reverse_lazy('/pups')