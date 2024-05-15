from django.urls import path
from . import views

urlpatterns = [
    path('BookStore/', views.login_page, name='website_books'),
    path('BookDetails/', views.show_signup, name='details')
]
