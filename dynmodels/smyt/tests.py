from django.test import TestCase
from smyt.models import get_app_models, get_app_models_by_name
import datetime

class SmytTestCase(TestCase):
#     fixtures = ['data.json']
    
    def testUsersModels(self):
        Users = get_app_models_by_name('Users')[0]
        ob = Users(paycheck=100, date_joined=datetime.date.today())
        ob.save()
        self.assertEqual(ob.pk, 1)
        
        ob1 = Users.objects.get(pk=1)
        
        self.assertEqual(ob1.paycheck, 100)
        self.assertEqual(ob1.date_joined, datetime.date.today())
        
    def testRoomsModels(self):
        Rooms = get_app_models_by_name('Rooms')[0]
        ob = Rooms(department='one', spots=3)
        ob.save()
        self.assertEqual(ob.pk, 1)
        
        ob1 = Rooms.objects.get(pk=1)
        
        self.assertEqual(ob1.department, 'one')
        self.assertEqual(ob1.spots, 3)
        
    def testMainPage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)