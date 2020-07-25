from django.shortcuts import render

# Create your views here.

companies = [
    {
    "name": "JOOJOO",
    "desc": "MOOOJOO",
    "email": "mojoJOJO",
    }
]
user = {
    "name": "Anshul",
    "email": "anshul@sss.com",
}
def home(request):
    return render(request, 'home/home.html', {'companies': companies, 'user': user })

def form(request):
    return render(request, 'company_form/form.html')