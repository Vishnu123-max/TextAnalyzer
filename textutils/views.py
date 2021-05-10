# I have  created this file  - Vishnu
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    # get the text
    purpose = ""
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get ('removepunc', 'off')
    fullcaps = request.POST.get ( 'fullcaps', 'off' )
    newlineremover = request.POST.get ( 'newlineremover', 'off' )
    extraspaceremover = request.POST.get ( 'extraspaceremover', 'off' )
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext :
            if char not in punctuations :
                analyzed = analyzed + char
        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed
        purpose += ' | Removed Punctuations'

    if (fullcaps == "on"):
         analyzed = djtext.upper()
         params = {'purpose' : 'Changed to Uppercase', 'analyzed_text' : analyzed}
         djtext = analyzed
         purpose += ' | Changed to Uppercase'

    if newlineremover == "on":
         analyzed = ""
         for char in djtext:
             if char != "\n" and char !="\r":
                    analyzed = analyzed + char
         params = {'purpose' : 'Removed New Lines', 'analyzed_text' : analyzed}
         djtext = analyzed
         purpose += ' | Removed New Lines'

    if extraspaceremover == "on":
         analyzed = ""
         for index,char in enumerate(djtext):
             if not (djtext [ index ] == " " and djtext [ index + 1 ] == " ") :
                 analyzed = analyzed + char

         params = {'purpose' : 'Removed Extra Space', 'analyzed_text' : analyzed}
          # Analyze the text
         djtext = analyzed
         purpose += ' | Removed Extra Space'

    params = {'purpose' : purpose, 'analyzed_text' : analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on") :
        return HttpResponse ( "please select any operation and try again" )

    return render(request, 'analyze.html', params)

