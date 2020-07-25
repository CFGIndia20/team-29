from django.shortcuts import render, redirect
from .models import company_details, skills_required 
from django.contrib.auth.models import User, auth 
# Create your views here.

companies = [
    {
    "name": "JOOJOO",
    "desc": "MOOOJOO",
    "email": "mojoJOJO",
    },
        {
    "name": "JOOJOO",
    "desc": "MOOOJOO",
    "email": "mojoJOJO",
    },
        {
    "name": "JOOJOO",
    "desc": "MOOOJOO",
    "email": "mojoJOJO",
    },
        {
    "name": "JOOJOO",
    "desc": "MOOOJOO",
    "email": "mojoJOJO",
    },
        {
    "name": "JOOJOO",
    "desc": "MOOOJOO",
    "email": "mojoJOJO",
    },
        {
    "name": "JOOJOO",
    "desc": "MOOOJOO",
    "email": "mojoJOJO",
    },
]
user = {
    "name": "Anshul",
    "email": "anshul@sss.com",
}
def home(request):
    user = request.user
    if(not user.is_authenticated):
        return render(request, 'home/home.html', {'companies': companies, 'user': user })
    else:
        return render(request, 'home/landing_page.html')

def form(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        profile = request.POST['jobProfile']
        description = request.POST['description']
        skills = request.POST.getlist('skills[]')
        
        company = company_details.objects.create(
            company_name = name,
            contact_email = email,
            job_profile = profile,
            job_description = description
        )
        company.save()
        company = company_details.objects.get(company_name = name, contact_email = email,job_profile = profile)

        for skill in skills:
            temp = skills_required.objects.create(
                company_id = company,
                skills_required = skill
            )
            temp.save()
        return redirect('/')

    else:
        return render(request, 'company_form/form.html')