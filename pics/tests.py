from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):
  
    # Set up method
    def setUp(self):
        self.mombasa= Location(name = 'Mombasa', description ='Pwani ya Kenya')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mombasa,Location))

    # Testing Save Method
    def test_save_method(self):
        self.mombasa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
  
    # Set up method
    def setUp(self):
        self.health= Category(name = 'health', description ='An apple a day keeps the doctor away')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.health,Category))

    # Testing Save Method
    def test_save_method(self):
        self.health.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)