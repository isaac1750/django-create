from django.urls import path
from crud1.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView
from . import views


app_name = 'crud1'
urlpatterns = [
    # ...

    path('', AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    path('author-detail/', views.detail, name='detail'),
]




