from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import *
# Create your tests here.

class AccountTestCase(APITestCase):

    def setUp(self):
        self.create_url = reverse('create')
        Account.objects.create(name='Alina',
                               last_name='Turga',
                               username='Coldcoil',
                               email='ta064948@gmail.com',
                               password='123456aa'

        )

    def test_account_create(self):
        data = {
            "name":"Alina1",
            "last_name":"T",
            "email":"ta0649408@gmail.com",
            "username":"Alina1",
            "password":"123456aa",
            "password2":"123456aa"
        }
        self.response = self.client.post(self.create_url,data)
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)
        print(self.response.data)


    def test_account_create_empty_username(self):
        data = {
            "name": "Alina1",
            "last_name": "T",
            "email": "ta064948@gmail.com",
            "username": "",
            "password": "123456aa",
            "password2": "123456aa"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)

    def test_account_create_empty_password(self):
        data = {
            "name": "Alina1",
            "last_name": "T",
            "email": "ta064948@gmail.com",
            "username": "Alina1",
            "password": "",
            "password2": "123456aa"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)

    def test_account_create_empty_email(self):
        data = {
            "name": "Alina1",
            "last_name": "T",
            "email": "",
            "username": "Alina1",
            "password": "123456aa",
            "password2": "123456aa"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)

    def test_account_create_different_passwords(self):
        data = {
            "name": "Alina1",
            "last_name": "T",
            "email": "ta064948@gmail.com",
            "username": "Alina1",
            "password": "123456aa",
            "password2": "4343434tt"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)


    def test_account_create_empty_last_name(self):
        data = {
            "name": "Alina1",
            "last_name": "",
            "email": "ta064948@gmail.com",
            "username": "Alina1",
            "password": "123456aa",
            "password2": "123456aa"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)

    def test_account_create_empty_name(self):
        data = {
            "name": "",
            "last_name": "T",
            "email": "ta064948@gmail.com",
            "username": "Alina1",
            "password": "123456aa",
            "password2": "123456aa"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)


    def test_account_create_username_dublicate(self):
        data = {
            "name": "Alina1",
            "last_name": "T",
            "email": "ta064948dd@gmail.com",
            "username": "Coldcoil",
            "password": "123456aa",
            "password2": "123456aa"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)


    def test_account_create_email_dublicate(self):
        data = {
            "name": "Alina",
            "last_name": "Turga",
            "email": "ta064948@gmail.com",
            "username": "Coldcoil",
            "password": "123456aa",
            "password2": "123456aa"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)


class AuthTestCase(APITestCase):

    def setUp(self):
        self.login_url = reverse('login')
        Account.objects.create(name='Alina',
                               last_name='Turga',
                               username='Coldcoil',
                               email='ta064948@gmail.com',
                               password='123456aa'

                               )


    def test_auth_create(self):
        data = {
            "name": "Alina",
            "last_name": "Turga",
            "email": "ta0649408@gmail.com",
            "username": "Coldcoil",
            "password": "123456aa",
            "password2": "123456aa"
        }
        self.response = self.client.post(self.login_url,data)
        self.assertEqual(self.response.status_code,status.HTTP_200_OK)


    def test_auth_create_different_password(self):
        data = {
            "name": "Alina",
            "last_name": "Turga",
            "email": "ta0649408@gmail.com",
            "username": "Coldcoil",
            "password": "463637",
            "password2": "3567880"
        }
        self.response = self.client.post(self.login_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)






