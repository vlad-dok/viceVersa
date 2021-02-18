from django.shortcuts import render

def home(request):
	return render (request,'home.html')

def reverse(request):
	text_ru = request.GET['message']
	reversed_text = text_ru[::-1]
	return render (request,'reverse.html',{'message':text_ru, 
		'reversedtext':reversed_text})