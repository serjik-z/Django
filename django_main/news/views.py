from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView



def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'django_main/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'django_main/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'django_main/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'django_main/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'django_main/create.html', data)
