from django.urls import include, path
from bookmark.views import BookmarkLV, BookmarkDV

app_name='bookmark'
urlpatterns = [
    # Class-based views
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:id>', BookmarkDV.as_view, name='detail'),
]