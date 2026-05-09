from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import MongoClient

# Sample data for superheroes, teams, activities, leaderboard, and workouts
data = {
    'users': [
        {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'DC'},
        {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'DC'},
        {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
        {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
        {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com', 'team': 'Marvel'},
        {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'team': 'Marvel'},
    ],
    'teams': [
        {'name': 'Marvel', 'members': ['Tony Stark', 'Steve Rogers', 'Natasha Romanoff']},
        {'name': 'DC', 'members': ['Clark Kent', 'Bruce Wayne', 'Diana Prince']},
    ],
    'activities': [
        {'user': 'Clark Kent', 'activity': 'Flying', 'duration': 60},
        {'user': 'Bruce Wayne', 'activity': 'Martial Arts', 'duration': 45},
        {'user': 'Tony Stark', 'activity': 'Weight Lifting', 'duration': 30},
        {'user': 'Steve Rogers', 'activity': 'Running', 'duration': 50},
    ],
    'leaderboard': [
        {'team': 'Marvel', 'points': 150},
        {'team': 'DC', 'points': 120},
    ],
    'workouts': [
        {'name': 'Super Strength', 'suggested_for': 'DC'},
        {'name': 'Agility Training', 'suggested_for': 'Marvel'},
    ]
}

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        for collection in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[collection].delete_many({})

        # Insert data
        db['users'].insert_many(data['users'])
        db['teams'].insert_many(data['teams'])
        db['activities'].insert_many(data['activities'])
        db['leaderboard'].insert_many(data['leaderboard'])
        db['workouts'].insert_many(data['workouts'])

        # Ensure unique index on email for users
        db['users'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
