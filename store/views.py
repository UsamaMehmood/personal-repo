from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Fan, Item
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from store import forms
from django.urls import reverse_lazy

def index(request):
    template='index.html'
    context={'page_title': 'Home'}
    return render(request, template_name=template, context=context)

class ItemsList(ListView):
    model = Item
    template_name = 'store/items.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Items'
        return context

    def get_queryset(self):
        name = self.request.GET.get('name', '')
        if not name == '':
            return Item.objects.filter(name__icontains=name)
        else:
            return Item.objects.all()


class UpdateItem(UpdateView):
    template_name = 'store/update_item.html'
    form_class = forms.ItemUpdateForm
    success_url = reverse_lazy('store:items')
    context_object_name = 'form'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Item Update'
        return context

class ItemDelete(DeleteView):
    template_name = 'store/delete.html'
    success_url = reverse_lazy('store:items')
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete'
        return context

class AddItem(CreateView):
    success_url = reverse_lazy('store:items')
    model = Item
    context_object_name = 'form'
    template_name = 'store/update_item.html'
    form_class = forms.ItemUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add'
        return context


class FansList(ListView):
    model = Fan
    template_name = 'store/fans.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Fans'
        return context

    def get_queryset(self):
        name = self.request.GET.get('name', '')
        if not name == '':
            return Fan.objects.filter(name__icontains=name)
        else:
            return Fan.objects.all()


class UpdateFan(UpdateView):
    template_name = 'store/update_item.html'
    form_class = forms.ItemUpdateForm
    success_url = reverse_lazy('store:fans')
    context_object_name = 'form'
    model = Fan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Fan Update'
        return context

class FanDelete(DeleteView):
    template_name = 'store/delete_fan.html'
    success_url = reverse_lazy('store:fans')
    model = Fan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete'
        return context

class AddFan(CreateView):
    success_url = reverse_lazy('store:fans')
    model = Fan
    context_object_name = 'form'
    template_name = 'store/update_item.html'
    fields = ['name', 'quantity', 'seller', 'total_amount', 'amount_paid']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add'
        return context
