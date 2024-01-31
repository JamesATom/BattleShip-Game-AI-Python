from django.http import JsonResponse
from django.views import View

class AIBotView(View):
    difficulty = 'easy'  # default difficulty

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Easy level response'})
    