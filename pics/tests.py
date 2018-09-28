from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.annstella= Image(name = 'house', description ='I like it', category ='basic', location = 'Nairobi')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.annstella,Image))

 # Testing Save Method
    def test_save_method(self):
        self.annstella.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)