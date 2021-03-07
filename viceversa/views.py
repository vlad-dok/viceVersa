from django.shortcuts import render

def home(request):
	return render (request,'home.html')

def reverse(request):
	text_ru = request.GET['message']
	reversed_text = text_ru[::-1]
	words = text_ru.split()
	number_of_words = len(words)
	return render (request,'reverse.html', {'message':text_ru, 
		'reversedtext':reversed_text,'number_of_words':number_of_words})

# def quantity(request):
# 	words_text = print(len(text_ru.split())
# 	# print(len(set(text_ru.split())))





# 	words = set()
# 	for _ in range(int(input())):
#    		words.update(input().split())
# 	# words_text = (len(words))
# 	# return render (request,'reverse.html',{'message':text_ru, 
# 	# 	})