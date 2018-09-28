from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.annstella= Image(name = 'house', description ='I like it', category ='basic', location = 'Nairobi')