
from django.urls import path
from ai_easy_app.views import AIBotView

urlpatterns = [
    path('ai_bot/easy/', AIBotView.as_view(difficulty='easy'), name='ai_bot_easy'),
]
