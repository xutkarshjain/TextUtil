from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    input_text=request.POST.get('text','Enter Some text first')
    upp=request.POST.get('upperval',0)
    exsp=request.POST.get('extraspace',0)
    newl=request.POST.get('newlineval',0)
    pun=request.POST.get('punchval',0)
    final_text='Enter some Text or select at least one operation.'
    operation='Error'

    if upp:
        final_text=''
        for i in input_text:
            final_text+=i.upper()
        input_text=final_text
        operation="Your text has been Tranformed."

    if exsp:
        final_text=''
        for index in range(len(input_text)-1):
            if not(input_text[index]==' ' and input_text[index+1]==' '):
                final_text+=input_text[index]
        input_text=final_text
        operation="Your text has been Tranformed."

    if newl:
        final_text=''
        for char in input_text:
            if char!='\n' and char!='\r':
                final_text+=char
        input_text=final_text
        operation="Your text has been Tranformed."

    if pun:
        final_text=''
        for char in input_text:
            if char not in '''!@#$%^&*(){}[]<>",'.?|/:\;''':
                final_text+=char
        operation="Your text has been Tranformed."

    para={'final_text':final_text,'status':operation}
    return render(request,'index2.html',para)
