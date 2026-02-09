import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Producto

class Command(BaseCommand):
    help = 'Seeds the database with realistic test products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding realistic data...')
        
        # Ensure admin user exists
        user, created = User.objects.get_or_create(username='admin2')
        if created:
            user.set_password('admin')
            user.save()

        # Clear existing products
        Producto.objects.all().delete()
        self.stdout.write('Deleted existing products.')

        products_data = [
            ('Confites', ['Trululu Gusanos', 'Bon Bon Bum', 'Chocolate Jet', 'Galletas Festival', 'Chocas', 'Super Coco', 'Barrilete', 'Mentas Heladas', 'Chokis', 'Sparkies']),
            ('Alimentos', ['Arroz Diana', 'Aceite Premier', 'Atún Van Camps', 'Pasta Doria', 'Harina PAN', 'Lentejas', 'Frijoles Bola Roja', 'Sal Refisal', 'Azúcar Manuelita', 'Café Sello Rojo']),
            ('Otros', ['Jabón Rey', 'Detergente Fab', 'Papel Higiénico Familia', 'Servilletas', 'Clorox', 'Lavaloza Axion', 'Shampoo Savital', 'Crema Dental Colgate', 'Desodorante Rexona', 'Afeitar Gillette']),
        ]

        count = 0
        for category, items in products_data:
            for item in items:
                price = round(random.uniform(5.0, 50.0) * 100, 2) # Realistic prices
                description = f"Presentación económica de {item}. Calidad garantizada."
                
                Producto.objects.create(
                    nombre=item,
                    categoria=category,
                    descripcion=description,
                    precio=price,
                    usuario=user
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {count} realistic products'))
