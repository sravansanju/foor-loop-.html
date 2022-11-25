from django.shortcuts import render

# Create your views here.
'''def a2_first(request):
    d={'a':100,'b':2000,'c':300}
    return render(request,'a2_first.html',d)
    '''

def a2_second(request):
    d={'name':'Sanju'}
    return render(request,'a2_second.html',d)