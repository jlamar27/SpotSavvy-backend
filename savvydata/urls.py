from django.urls import path
from .views import (
    signup_view,
    login_view,
    logout_view,
    review_list,
    create_review,
    edit_review,
    delete_review,
    get_csrf
)

urlpatterns = [
    path('get-csrf-token/', get_csrf, name='get_csrf'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reviews/<str:restaurant_id>/', review_list, name='review-list'),
    path('review/create/', create_review, name='create-review'),
    path('review/edit/<uuid:pk>/', edit_review, name='edit-review'),
    path('review/delete/<uuid:pk>/', delete_review, name='delete-review'),
]