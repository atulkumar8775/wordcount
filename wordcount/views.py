from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    list_lenght =len(word_list)

    worddictionary={}

    for word in word_list:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] =1

    sorted_list=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{'fulltext':data,'words':list_lenght,'worddict':sorted_list})



def about(request):
    return render(request,'about.html')







#def contact(request):
#    return HttpResponse("<h1>contact us</h1><br> This is contact page")