from django.shortcuts import render
from django.http import JsonResponse
import json
import random  # Import 'random' for 'randint'
import datascraper.datascraper as ds  # Import 'datascraper'


# View to return a random number as JSON
def Get_A_Number(request):
    int_response = random.randint(0, 99)
    return JsonResponse({'resp': int_response})

# View to handle chat responses
def chat_response(request):
    # Assuming 'create_response' returns a string
    question = request.GET.get('question', '')
    print("question is: " ,question)
    #print(request.body)
    message_response = ds.create_response(question)
    return JsonResponse({'resp': message_response})
