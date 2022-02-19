import pytest
from django.urls import reverse_lazy
from django.test import Client

pytestmark = pytest.mark.django_db


def test_resume_list_view():
    url = reverse_lazy('resume:home')
    response = Client().get(url)
    assert response.status_code == 200
