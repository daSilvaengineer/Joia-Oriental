import os
import django

# Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Category, Product
from django.core.files import File

def seed_data():
    print("Iniciando o cadastro das joias exclusivas...")

    # 1. Criar Categorias
    cat_china = Category.objects.get_or_create(name="Coleção Imperial China")[0]
    cat_japao = Category.objects.get_or_create(name="Essência Zen Japão")[0]
    cat_india = Category.objects.get_or_create(name="Riqueza Ancestral Índia")[0]
    cat_turquia = Category.objects.get_or_create(name="Arte Turca")[0]

    # Lista de Joias para Cadastro
    joias = [
        {
            "name": "Colar de Jade Imperial",
            "cat": cat_china,
            "price": 15000.00,
            "material": "Jade Imperial e Ouro 24k",
            "img": "1. Colar de Jade Imperial (China).jpg",
            "is_featured": True
        },
        {
            "name": "Pingente de Dragão Chinês",
            "cat": cat_china,
            "price": 8500.00,
            "material": "Ouro Maciço 18k",
            "img": "7. Pingente de Dragão Chinês (China).jpg",
            "is_featured": True
        },
        {
            "name": "Anel Flor de Lótus",
            "cat": cat_japao,
            "price": 4200.00,
            "material": "Prata 950 e Diamante",
            "img": "Anel_Flor_de_Lótus(Japão).jpg",
            "is_featured": False
        },
        {
            "name": "Pendente de Pérola Akoya",
            "cat": cat_japao,
            "price": 6800.00,
            "material": "Pérola Natural e Ouro Branco",
            "img": "5. Pendente de Pérola Akoya (Japão).jpg",
            "is_featured": True
        },
        {
            "name": "Gargantilha Navaratna",
            "cat": cat_india,
            "price": 12500.00,
            "material": "Ouro 22k e Pedras Preciosas",
            "img": "6. Gargantilha Navaratna (Índia).jpg",
            "is_featured": True
        },
        {
            "name": "Pulseira de Filigrana",
            "cat": cat_turquia,
            "price": 9800.00,
            "material": "Ouro 18k e Turquesa",
            "img": "4. Pulseira de Filigrana (Turquia).jpg",
            "is_featured": True
        },
    ]

    base_path = r'C:\Users\dasil\ecommerce_project\store\static\store\images'

    for j in joias:
        p, created = Product.objects.get_or_create(
            name=j["name"],
            category=j["cat"],
            defaults={
                'price': j["price"],
                'material': j["material"],
                'description': f"Uma peça magnífica da {j['cat'].name}, refletindo séculos de tradição e requinte.",
                'stock': 5,
                'is_featured': j["is_featured"]
            }
        )
        
        if created:
            img_path = os.path.join(base_path, j["img"])
            if os.path.exists(img_path):
                with open(img_path, 'rb') as f:
                    p.image.save(j["img"], File(f), save=True)
                print(f"Sucesso: {j['name']} cadastrado com imagem.")
            else:
                print(f"Aviso: Imagem não encontrada para {j['name']}")

    print("\n--- População concluída com sucesso! ---")

if __name__ == '__main__':
    seed_data()