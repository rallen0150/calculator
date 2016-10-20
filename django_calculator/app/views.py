from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from app.models import Operation, Profile

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'

class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = Operation.objects.all()
        return context

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return Profile.objects.all()
        return Profile.objects.filter(user=self.request.user)

class CalculatorCreateView(CreateView):
    model = Operation
    success_url = '/'
    fields = ('num1', 'operator', 'num2')

    def get_context_data(self):
        context = super().get_context_data()
        context['operation'] = Operation.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user

        if instance.operator == '+':
            instance.answer = instance.num1 + instance.num2
        elif instance.operator == '-':
            instance.answer = instance.num1 - instance.num2
        elif instance.operator == '*':
            instance.answer = instance.num1 * instance.num2
        else:
            if instance.num2 == 0:
                instance.answer = "Can't Divide by 0"
            else:
                instance.answer = instance.num1 / instance.num2
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    model = Profile
    success_url = reverse_lazy('calc_create_view')
    fields = ('access_level', )
