from django.shortcuts import render
from django.views.generic import View
from .forms import ContactUsForm
from .models import ContactUs
from django.http import JsonResponse


class ContactUsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            forms = ContactUsForm(initial={'name': request.user.fullname, 'email': request.user.email})
        else:
            forms = ContactUsForm()
        return render(request, 'contact_app/contact.html', {'forms': forms})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactUs.objects.create(user=request.user, name=cd['name'], email=cd['email'], title=cd['title'], message=cd['message'])
            return JsonResponse({'status': 200})
        else:
            return JsonResponse({'status': 400})



