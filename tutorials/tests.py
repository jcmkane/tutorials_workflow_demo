from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

# @pytest.mark.django_db
# def test_create_tutorial():
#     tutorial = Tutorial.objects.create(
#         title='Pytest',
#         tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#         description='Tutorial on how to apply pytest to a Django application',
#         published=True
#     )
#     assert tutorial.title == "Pytest"

@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# The following two functions use new_tutorial as a parameter, causing the
#  new_tutorial() fixture to be run first when either of test runs.

# Check that the object created by the fixture exists
def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

# Update the title of the new_tutorial object, save update, and
#  assert that a tutorial with the update name exists in the db.
def test_update_tutorial(new_tutorial):
    #Inside this function, new_tutorial refers to the 
    #  oject returned by the new_tutorial fn.
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

# Now, we add another fixture fn that creates a different Tutorials object
@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# Add a test that uses both fixtures as parameters
def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk