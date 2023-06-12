from django.shortcuts import render

def home(request):
    return render(request, "main/home.html")

def services(request):
    return render(request, "main/services.html")

def work(request):
    img = "img/drone1.jpg"
    video = 'video/drone1.mp4'
    text = "Vous êtes propriétaire d'un Mas provençal ? Avec son charme authentique et ses environs pittoresques, votre Mas mérite d'être vu sous son meilleur jour.  Nos vidéos et photos, une fois intégrées sur votre site ou plateformes de réservation, peuvent augmenter votre visibilité en ligne, attirer plus de visiteurs et potentiellement augmenter le nombre de réservations."

    exemples = []

    exemple = {'img': 'img/ex_mas.jpg', 'title':'Mas provençal', 'text':"Vous êtes propriétaire d'un Mas provençal ? Avec son charme authentique et ses environs pittoresques, votre Mas mérite d'être vu sous son meilleur jour. Nos vidéos et photos, une fois intégrées sur votre site ou plateformes de réservation, peuvent augmenter votre visibilité en ligne, attirer plus de visiteurs et potentiellement augmenter le nombre de réservations."}
    exemples.append(exemple)

    exemple = {'img': 'img/ex_gite.jpg', 'title':'Gîte de Famille', 'text':"Votre gîte de famille est le lieu de souvenirs inoubliables et de moments de détente partagés. Il est essentiel de transmettre cette atmosphère chaleureuse à vos futurs clients. Le résultat ? Des images engageantes qui peuvent renforcer votre présence en ligne, générer plus d'intérêt et conduire à une augmentation des réservations."}
    exemples.append(exemple)

    exemple = {'img': 'img/ex_villa.jpg', 'title':'Villa de Luxe', 'text':"Vous possédez une villa de luxe ? Ces demeures sont souvent synonymes d'élégance et de grandeur, et méritent une représentation qui traduit leur prestige. Les images haut de gamme que nous produisons peuvent améliorer la perception de votre propriété, augmenter sa visibilité en ligne et attirer une clientèle de luxe, contribuant ainsi à une croissance des réservations."}
    exemples.append(exemple)

    exemple = {'img': 'img/ex_chalet.jpg', 'title':'Chalet de Montagne', 'text':"Votre chalet de montagne est niché dans un cadre naturel spectaculaire ? Nos images aériennes mettent en valeur l'architecture unique de votre chalet et son environnement époustouflant. Ces visuels attrayants peuvent stimuler votre visibilité en ligne, susciter plus d'intérêt et augmenter le nombre de réservations."}
    exemples.append(exemple)

    return render(request, "main/work.html", {'list_exemples': exemples})

def price(request):
    return render(request, "main/price.html")

def blog(request):
    return render(request, "main/blog.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def template(request):
    return render(request, "main/template.html")
