from django.shortcuts import render

# Create your views here.\
def root(request):
    return render(request, "index.html")
    
 
def submission(request):
    if request.method == 'POST':
        language = request.POST['language']
        name = request.POST['name']
        location = request.POST['Location']
        Comments =request.POST['Comments']
        context = {
    	    "name_on_template" : name,
    	    "location_on_template" : location,
            "language_on_template" : language,
            "comments_on_template" : Comments,
        }      
    return render(request, 'result.html', context)