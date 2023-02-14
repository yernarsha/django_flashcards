from django.shortcuts import render

from random import randint

# Create your views here.

def index(request):
    return render(request, 'flashapp/index.html', {})

def add(request):
    num1 = randint(0, 9)
    num2 = randint(0, 9)

    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['num1']
        old_num2 = request.POST['num2']

        correct_answer = int(old_num1) + int(old_num2)
        if int(answer) == correct_answer:
            my_answer = f'Correct! {old_num1} + {old_num2} = {answer}'
            color = 'success'
        else:
            my_answer = f'Incorrect! {old_num1} + {old_num2} is not {answer}, it is {correct_answer}'
            color = 'danger'

        return render(request, 'flashapp/add.html', 
                      {'answer': answer, 'my_answer': my_answer, 'num1': num1, 'num2': num2, 'color': color})

    return render(request, 'flashapp/add.html', 
                  {'num1': num1, 'num2': num2})

def subtract(request):
    return render(request, 'flashapp/subtract.html', {})

def multiply(request):
    return render(request, 'flashapp/multiply.html', {})

def divide(request):
    return render(request, 'flashapp/divide.html', {})

