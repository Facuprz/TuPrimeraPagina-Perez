from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm, PageSearchForm
from django.db.models import Q

# Vistas simples (home / about)
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# CBVs para Pages
class PageListView(ListView):
    model = Page
    template_name = "pages_list.html"
    context_object_name = "pages"
    paginate_by = 10  # opcional

    def get_queryset(self):
        qs = super().get_queryset()
        self.search_form = PageSearchForm(self.request.GET or None)
        if self.search_form.is_valid():
            q = self.search_form.cleaned_data.get('q')
            if q:
                qs = qs.filter(titulo__icontains=q) | qs.filter(subtitulo__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['search_form'] = getattr(self, 'search_form', PageSearchForm())
        return ctx

class PageDetailView(DetailView):
    model = Page
    template_name = "page_detail.html"
    context_object_name = "page"

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "page_form.html"
    success_url = reverse_lazy('pages_list')

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "page_form.html"
    success_url = reverse_lazy('pages_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "page_confirm_delete.html"
    success_url = reverse_lazy('pages_list')

def search(request):
    form = PageSearchForm(request.GET or None)
    results = []
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            results = Page.objects.filter(
                Q(titulo__icontains=q) |
                Q(subtitulo__icontains=q) |
                Q(contenido__icontains=q)
            )
    return render(request, 'search.html', {'form': form, 'results': results})
