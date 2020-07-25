from django.shortcuts import render, redirect
from .models import company_details, skills_required 
# Create your views here.

def home(request):
    return render(request, 'base/base.html')

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