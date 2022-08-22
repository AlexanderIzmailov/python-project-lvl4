import django_filters
from .models import *
from django import forms
import logging





class TaskFilter(django_filters.FilterSet):
    # labels = django_filters.ModelChoiceFilter(lookup_expr='iexact')
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())
    self_tasks = django_filters.BooleanFilter(field_name='author', widget=forms.CheckboxInput, method='is_author')
    # mine = forms.BooleanField()

    def is_author(self, queryset, name, value):
        user = self.request.user
        if value:
            return queryset.filter(author=user.id)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    # @property
    # def qs(self):
    #     parent = super().qs
    #     mine = getattr(self.request, 'mine', None)
    #     user = getattr(self.request, 'user', None)
    #     print("BBBB_1")

    #     if mine == "on":
    #         print("BBBB_2")
    #         return parent.filter(author=user)
    #         # return User.objects.all()
    #     return parent

    # widget = {
    #     'labels': forms.TextInput(attrs={'class': 'form-control'})
    # }

