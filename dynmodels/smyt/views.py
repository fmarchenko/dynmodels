# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from smyt.models import get_app_models, get_app_models_by_name
from django.http import Http404, HttpResponse
from django.core import serializers
from django.forms.models import modelform_factory


class FrontPage(TemplateView):
    template_name="frontpage.html"
    
    def get_context_data(self, **kwargs):
        context = super(FrontPage, self).get_context_data(**kwargs)
        context['models_list'] = get_app_models()
        return context
    

class GetDataView(ListView):
    def get(self, request, *args, **kwargs):
        try:
            self.model = get_app_models_by_name(kwargs.get('model_class'))[0]
        except IndexError as ex:
            raise Http404("Class model %s not found!" % kwargs.get('model_class'))
        
        data = serializers.serialize('json', self.get_queryset())
        
        return HttpResponse(data, content_type='application/json')


class SetDataView(ListView):
    def get(self, request, *args, **kwargs):
        raise Http404("Page not found!")
    
    def post(self, request, *args, **kwargs):
        try:
            self.model = get_app_models_by_name(kwargs.get('model_class'))[0]
        except IndexError as ex:
            raise Http404("Class model %s not found!" % kwargs.get('model_class'))
        
        Form = modelform_factory(self.model)
        instance=(self.model.objects.filter(id=request.POST.get('id')) or [None])[0]
        form = Form(request.POST or None, instance=instance)
        if form.is_valid():
            obj = form.save()
        
        data = serializers.serialize('json', self.get_queryset())
        
        return HttpResponse(data, content_type='application/json')