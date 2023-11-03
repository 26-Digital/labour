from django.urls import path
from  .views import SetswanaNltkView

urlpatterns = [
    path('setswana-nltk/', SetswanaNltkView.as_view(), name='setswana-nltk')
]