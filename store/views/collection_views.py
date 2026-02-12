from django.shortcuts import render


def collections_page(request):
    collections = [
        {
            "name": "China",
            "slug": "china",
            "flag": "store/img/flags/china.svg",
            "description": "Entre dragões celestiais e dinastias eternas, nascem joias que carregam poder, prosperidade e mistério imperial."
        },
        {
            "name": "Índia",
            "slug": "india",
            "flag": "store/img/flags/india.svg",
            "description": "Cores sagradas, ouro ancestral e espiritualidade vibrante se entrelaçam em adornos que celebram a alma."
        },
        {
            "name": "Japão",
            "slug": "japao",
            "flag": "store/img/flags/japao.svg",
            "description": "Silêncio, honra e delicadeza florescem como sakuras, revelando joias de beleza serena e precisão eterna."
        },
    ]

    return render(request, "store/pages/collections.html", {
        "collections": collections
    })
