from django.test import TestCase


# Create your tests here.
class Login_Test(TestCase):
    def test_login(self):
        response = self.client.post('/account/login/', {'username': 'Dmitriy', 'password': 'Chaki128'})
        self.assertEqual(response.status_code, 200)


class Create_Group_Test(TestCase):
    def test_create_group_form(self):
        response = self.client.post('/group/add/', {'group_title': 'group 3'})
        self.assertEqual(response.status_code, 302)


class Add_Student_Test(TestCase):
    def test_add_student_form(self):
        response = self.client.post('/student/add/', {'fio': 'Siouxsie Sioux',
                                                      'date_of_birth': '2015-05-05', 'student_ticket': '8676',
                                                      'group': '8e52'})
        self.assertEqual(response.status_code, 302)
