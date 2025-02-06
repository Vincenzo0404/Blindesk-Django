from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Customer


class SimpleCustomerUpdateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            name="Old Name",
        )
        self.update_url = reverse("customer-update", kwargs={"pk": self.customer.pk})

    def test_update_customer_name(self):
        # Recupera il cliente con id=1
        customer = Customer.objects.get(id=self.customer.id)

        # Modifica il nome del cliente
        customer.name = "New Name"

        # Prepara il payload per la richiesta PUT
        payload = {
            "name": customer.name,
        }

        # Invia la richiesta PUT all'endpoint di aggiornamento
        response = self.client.put(self.update_url, data=payload, format="json")

        # Aggiorna l'istanza del cliente dal database
        customer.refresh_from_db()

        # Verifica che la risposta sia 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica che il nome del cliente sia stato aggiornato correttamente
        self.assertEqual(customer.name, "New Name")
