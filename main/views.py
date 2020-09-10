from django.views.generic import ListView, DetailView
from .models import Post

col_pub = 1


class ListPostViews(ListView):
    model = Post
    paginate_by = col_pub


class CustomListPostViews(ListPostViews):

    def get_queryset(self):
        return Post.objects.filter(tags__name__contains=self.kwargs['tag_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag_slug']
        return context


class PostDetailView(DetailView):
    model = Post
