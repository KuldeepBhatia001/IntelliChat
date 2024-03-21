from django.shortcuts import render
from django.http import JsonResponse
import openai
from requests import auth

open_api_key = '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'
openai.api_key = open_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]


    )

    answer = response.choices[0].message.content.strip()
    return answer



def chatbot(request):
    if request.method == 'POST':
        message= request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message,'response': response })
    return render(request,  'chatbot.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)




