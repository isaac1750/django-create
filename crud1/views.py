


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from crud1.models import Author
from django.shortcuts import render



class AuthorCreateView(CreateView):
    model = Author
    fields = ['name']
  
    template_name = 'author_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context



class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']
    template_name = 'author_update_form.html'


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')
    
def detail(request):
    return render(request, 'detail.html')

