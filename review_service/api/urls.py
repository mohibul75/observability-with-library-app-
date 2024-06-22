from django.urls import path
from .views import ReviewListCreateAPIView, ReviewDetailView

urlpatterns = [
    path('reviews/<int:book_id>/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:review_id>/', ReviewDetailView.as_view(), name='review-detail'),
]
