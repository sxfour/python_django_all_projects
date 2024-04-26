from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from myprogram.forms import AddPostForm, UploadFileForm
from myprogram.models import Program, Category, TagPost, UploadFiles
from myprogram.utils import DataMixin


class ProgramHome(DataMixin, ListView):
    template_name = 'program/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Program.published.all().select_related('cat')


@login_required
def about(request):
    contact_list = Program.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'program/about.html',
                  {'title': 'О Сайте', 'page_obj': page_obj})


class ShowPost(DataMixin, DetailView):
    # model = Program
    template_name = 'program/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Program.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'program/addpage.html'
    title_page = "Добавление статьи"

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(DataMixin, UpdateView):
    model = Program
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'program/addpage.html'
    success_url = reverse_lazy('home')
    title_page = "Редактирование статьи"


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Войти')


class ProgramCategory(DataMixin, ListView):
    template_name = 'program/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Program.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat

        return self.get_mixin_context(context, title='Категория - ' + cat.name, cat_selected=cat.pk, )


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1 align="center" style="color:rgb(169,169,169)"> '
                                '— Ну вот, я так и думал.'
                                ' С этой стороны ничуть не лучше...</h1>')


class TagPostList(DataMixin, ListView):
    template_name = 'program/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])

        return self.get_mixin_context(context, title='Тег: ' + tag.tag)

    def get_queryset(self):
        return Program.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')
