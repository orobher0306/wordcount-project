# escribir texto en formato http
from django.http import HttpResponse
# para poder direccionar a las paginas
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'homepage.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    dictionary = {}
    for word in wordlist:
        if word in dictionary:
            dictionary[word] += 1
        elif word not in dictionary:
            dictionary[word] = 1

    sorteddictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sorteddictionary':sorteddictionary})

def about(request):
    return render(request, 'about.html')