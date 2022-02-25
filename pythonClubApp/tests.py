from django.test import TestCase
from .models import Meeting, MeetMinute, Resource, Event
# Create your tests here.
class MeetingTest(TestCase):
    def setup(self):
        
        meeting=Meeting(meetingTitle='meetingTest', meetingDate='10/25/2022',meetingTime='12:00', meetingLocation='virtual')
        return meeting

    def test_string(self):
        meet = self.setup()
        self.assertEqual(str(meet),meet.meetingTitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table),'meeting')

#error: MeetMinute has no meetingId
# class MeetMinuteTest(TestCase):
#     def setUp(self):
#         meeting=Meeting(meetingTitle='meetingTest', meetingDate='10/25/2022',meetingTime='12:00', meetingLocation='virtual')

#     def testString(self):
#         type=MeetMinute(minuteText='TestingMeetMinute')
#         self.assertEqual(str(type), type.minuteText)

class ResourceTest(TestCase):
   def test_string(self):
       res=Resource(resourceName="library")
       self.assertEqual(str(res), res.resourceName)

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
   def test_string(self):
       event=Event(eventTitle="Testing event table")
       self.assertEqual(str(event), event.eventTitle)

   def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')
