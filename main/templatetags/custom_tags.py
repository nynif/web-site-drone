from django import template
import json
import os
import environ


env = environ.Env()


register = template.Library()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(base_dir, '../custom/.envfile'))

json_path =  '../' + env.str("CUSTOMLINK", "custom") + '/custom_data.json'
json_file_path = os.path.join(base_dir,json_path)

# Chargement du fichier JSON
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

@register.simple_tag
def custom_json(path):
    parts = path.split('.')
    value = data
    for part in parts:
        if isinstance(value, dict) and part in value:
            value = value[part]
        else:
            return ''
    return value