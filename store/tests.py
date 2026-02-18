from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal
from store.models import Product, Category


class ProductModelTest(TestCase):

    def setUp(self):
        
        self.category = Category.objects.create(name="Colares")

      
        self.test_image = SimpleUploadedFile(
            name='test.jpg',
            content=b'file_content',
            content_type='image/jpeg'
        )

        
        self.product = Product.objects.create(
            name="Colar Dragão",
            description="Colar oriental artesanal",
            price=Decimal("199.90"),
            category=self.category,
            image=self.test_image,
            material="Prata",
            stock=10
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Colar Dragão")
        self.assertEqual(self.product.category.name, "Colares")
        self.assertEqual(self.product.stock, 10)

    def test_string_representation(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_has_discount_property(self):
        self.product.old_price = Decimal("249.90")
        self.product.save()
        self.assertTrue(self.product.has_discount)
