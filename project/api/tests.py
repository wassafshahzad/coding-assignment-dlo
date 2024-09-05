from django.test import TestCase

# Create your tests here.
from api.utils import DLOBuilder


def test_url():
    b = DLOBuilder()
    print(b.generate_dlo("https://ca-walnaof.minddistrict.dev", "123", "careprovider"))

test_url()