from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.mail import send_mail, get_connection
from django.contrib import messages
from .models import Car
from .forms import ContactForm


class CarListView(ListView):
    model = Car
    template_name = 'garage/home.html'
    context_object_name = 'cars'
    ordering = ['-created']


class CarDetailView(DetailView):
    model = Car


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['make', 'model', 'fuel', 'color', 'date_of_production', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    template_name = 'garage/car_update.html'
    fields = ['make', 'model', 'fuel', 'color', 'date_of_production', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        car = self.get_object()
        if self.request.user == car.owner:
            return True
        return False


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    success_url = '/'

    def test_func(self):
        car = self.get_object()
        if self.request.user == car.owner:
            return True
        return False


@login_required
def my_cars(request):
    cars = Car.objects.all().filter(owner=request.user)
    return render(request, 'garage/my_cars.html', {'cars': cars})


def contact_us(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Email Inquery'
            body = {
                'full_name': form.cleaned_data['full_name'],
                'subject': form.cleaned_data['subject'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = f"""
            From: {body['full_name']}\n
            Subject: {body['subject']}\n
            Email address: {body['email_address']}\n
            Message: {body['message']}\n
            """
            conn = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(subject, message, body['email_address'], ['owngaragebg@gmail.com'], fail_silently=False,
                      connection=conn)
            messages.success(request, f'Thank you! We will contact you as soon as possible!')
            return redirect('garage-home')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'garage/contact_us.html', {'form': form, 'submitted': submitted})

