# -*- coding: utf-8 -*-
import os, yaml
os.sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dynmodels.settings")
from django.db import models
from django.db.models import get_app, get_models
import pymorphy2


TYPES_DICT = {
    'char': models.CharField,
    'int': models.IntegerField,
    'date': models.DateField,
}


def get_app_models():
    app = get_app('smyt')
    return get_models(app)


def get_app_models_by_name(class_name):
    app = get_app('smyt')
    models = get_models(app)
    return filter(lambda x: x.__name__.upper()==class_name.upper(), models)


def get_models_dict():
    app_path = os.path.dirname(__file__)
    models_path = os.path.join(app_path, 'models.yaml')

    f = open(models_path)
    modelsData = yaml.safe_load(f)
    f.close()

    return modelsData


def dynmodels_create():
    models_dict = get_models_dict()
    morph = pymorphy2.MorphAnalyzer()
    
    for key, val in models_dict.items():
        v_name = morph.parse(val.get('title', ''))[0]
        v_name_plur = v_name.inflect({'plur', 'nomn'})
        
        class Meta:
            verbose_name = v_name.normal_form
            verbose_name_plural = v_name_plur.word
        model = type(key.title(), (models.Model,), {'__module__': __name__, 'Meta': Meta})
        
        for field in val.get('fields',[]):
            kwargs = {
                'verbose_name': field['title'],
            }
            if field['type'] == 'char':
                kwargs['max_length'] = 255
                
            model.add_to_class(field['id'], TYPES_DICT[field['type']](**kwargs))


dynmodels_create()