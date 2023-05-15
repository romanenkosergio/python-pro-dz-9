from django.http import HttpResponse
from django.shortcuts import render

from .forms import PhoneNumberForm
from .tasks import send_sms_task


def validation_view(request):
    """View function for our validation form."""
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone']
            send_sms_task.delay(phone_number)
            return HttpResponse('Please check your phone for a validation code')
    else:
        form = PhoneNumberForm()

    return render(request, 'phone_validation.html', {'form': form})