from django.test import TestCase
# from django.urls import reverse
# from .models import Snack
# from django.contrib.auth import get_user_model
# # Create your tests here.
# class TestSnackDetailView(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='ahmad',
#             email = 'ahamd1232gmail.com',
#             password = 'ah123456789'
#         )
#         self.snack = Snack.objects.create(
#             purchaser = self.user,
#             name = 'test case',
#             description = 'good'

#         )
#     def test_status_code(self):
#         expected = 200
#         actual = self.client.get(reverse('snack_list')).status_code
#         self.assertEqual(expected,actual)

#     def test_movie_list(self):
#         response = self.client.get('snack_list').items()
#         expected = len(response)
#         self.assertNumQueries(expected)
    
#     def test_movie_create(self):
#         response = self.client.post(reverse('snack_create'),{'purchaser' : self.user,
#             'name' : 'test case',
#             'description' : 'good'})
#         get_response = self.client.get(reverse('snack_list'))
#         self.assertEqual(response.status_code,200)
#         self.assertContains(response,'case')
   
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class ThingTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            name="pickle", description='hhhhhhhhh', purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "pickle")

    def test_thing_content(self):
        self.assertEqual(f"{self.snack.name}", "pickle")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.description, 'hhhhhhhhh')

    def test_thing_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_thing_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        # no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "purchaser : tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "name": "Rake",
                "description": "2222222",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        # self.assertContains(response, "Details about Rake")

    def test_thing_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name","description":"3","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_thing_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)