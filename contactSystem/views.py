from django.shortcuts import render
from contactSystem import models
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        userId = models.get_user_id(username, password)
        if userId != 0:
            contacts = models.get_contact_list(userId)
            usercontext = {"userfirstname": username}
            context = {
                "nameUser": usercontext,
                "contactList": contacts
            }
            return render(request, "contacts.html", context)
        else:
            return HttpResponse("Invalid username or password",
                      content_type="text/plain")
    else:
        return render(request, "login.html")

def logout(request):
    return render(request, "login.html")

def share(request):
    searchId = request.GET.get('id')
    contactDetails = models.get_contact_details(searchId)
    print(contactDetails)
    return render(request, "shareContact.html", {"details": contactDetails})
