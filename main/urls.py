from django.urls import path
from .views import ListPostViews, PostDetailView, CustomListPostViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ListPostViews.as_view(), name='list_posts'),
    path('tag/<slug:tag_slug>/',
         CustomListPostViews.as_view(), name='list_posts_tag'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
