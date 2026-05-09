from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User, Team, Activity, Workout, LeaderboardEntry

class UserTests(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.username, 'testuser')

class TeamTests(APITestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='member', password='pass')
        team = Team.objects.create(name='TeamA')
        team.members.add(user)
        self.assertEqual(team.members.count(), 1)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='active', password='pass')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, calories_burned=200, date='2024-01-01')
        self.assertEqual(Activity.objects.count(), 1)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(Workout.objects.count(), 1)

class LeaderboardEntryTests(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create_user(username='leader', password='pass')
        entry = LeaderboardEntry.objects.create(user=user, score=100)
        self.assertEqual(LeaderboardEntry.objects.count(), 1)
