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
    success_url = reverse_lazy('calc_create_view')

class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = Operation.objects.all()
        return context

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class CalculatorCreateView(CreateView):
    model = Operation
    success_url = reverse_lazy('calc_create_view')
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
    fields = ('access_level', )

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])
