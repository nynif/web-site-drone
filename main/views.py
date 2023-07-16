from django.shortcuts import render
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file_path = os.path.join(base_dir, 'custom/custom_data.json')

# Chargement du fichier JSON
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# data1 = json.load(json_file_path) # deserialises it

def home(request):
    return render(request, "main/home.html", data)

def work(request):
    return render(request, "main/work.html", data)

def price(request):
    return render(request, "main/price.html", data)

# def services(request):
#     return render(request, "main/services.html", data)

# def blog(request):
#     return render(request, "main/blog.html")

# def about(request):
#     return render(request, "main/about.html")

# def contact(request):
#     return render(request, "main/contact.html")

# def template(request):
#     return render(request, "main/template.html")
