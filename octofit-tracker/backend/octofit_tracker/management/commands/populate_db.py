from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Example models for demonstration (replace with your actual models)
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)

        # Create Activities
        app_models.Activity.objects.create(user=ironman, type='run', duration=30)
        app_models.Activity.objects.create(user=batman, type='cycle', duration=45)
        app_models.Activity.objects.create(user=superman, type='swim', duration=60)
        app_models.Activity.objects.create(user=captain, type='run', duration=25)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes')

        # Create Leaderboard
        app_models.Leaderboard.objects.create(user=ironman, score=100)
        app_models.Leaderboard.objects.create(user=batman, score=90)
        app_models.Leaderboard.objects.create(user=superman, score=95)
        app_models.Leaderboard.objects.create(user=captain, score=85)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
