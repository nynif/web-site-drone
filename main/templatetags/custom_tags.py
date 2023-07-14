from django import template
import json
import os

register = template.Library()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file_path = os.path.join(base_dir, '../custom/custom_data.json')
# Chargement du fichier JSON
with open(json_file_path, 'r') as f:
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