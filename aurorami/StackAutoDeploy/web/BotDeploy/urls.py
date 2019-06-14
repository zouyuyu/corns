
from django.urls import path
from BotDeploy.views  import Bot    # new

urlpatterns = [
    path('', Bot.index,name='index'),  # new
    path('add/', Bot.add,name='add'),
    path('add/<int:a>/<int:b>/',Bot.add2, name='add'),
]