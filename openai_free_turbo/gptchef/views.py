from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai

openai.api_key = ""  # Заменить на свой ключ!


class CookAssistantView(APIView):
    def post(self, request):
        message = request.data.get('message', '').strip()
        if not message:
            return Response({'error': 'No message provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": "Ты — дружелюбный кулинарный помощник. Отвечай кратко, только о еде и рецептах, избегая 18+ и взрослых тем."},
                    {"role": "user", "content": message}
                ],
                max_tokens=256,
                temperature=0.7
            )
            answer = response['choices'][0]['message']['content'].strip()
            return Response({'answer': answer})
        except Exception as e:
            return Response({'error': f'OpenAI error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CookGPT4View(APIView):
    def post(self, request):
        message = request.data.get('message', '').strip()
        if not message:
            return Response({'error': 'No message provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "system",
                     "content": "Ты — дружелюбный, игривый кулинарный помощник. Отвечай кратко, ясно и пошагово, делясь рецептами и советами. Говори только о еде и напитках, включая алкогольные, избегая 18+ и взрослого контента. Добавляй юмор и легкую пошлость, чтобы общение было веселым и запоминающимся."},
                    {"role": "user", "content": message}
                ],
                max_tokens=512,
                temperature=0.7
            )
            answer = response['choices'][0]['message']['content'].strip()
            return Response({'answer': answer})
        except Exception as e:
            return Response({'error': f'OpenAI error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
