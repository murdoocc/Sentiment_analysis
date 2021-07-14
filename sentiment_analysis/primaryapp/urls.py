from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sentiments/', views.SentimentListView.as_view(), name='sentiments'),
    path('sentiment/<int:pk>', views.SentimentDetailView.as_view(), name='sentiment-detail'),
]

urlpatterns += [
    path('sentiment/new', views.new_sentiment, name='new-sentiment'),
]