#!/usr/bin/python3

from tests.test_models.test_base_model import test_base_model
from models.amenity import Amenity

class TestAmenity(test_base_model):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
    
    def test_name2(self):
        new = self.value()
        self.assertEqual(type(new.name), str)
