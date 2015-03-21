import datetime
import random
from django.db import models

class GiveawaySubmission(models.Model):
    date_created = models.DateTimeField(default=datetime.datetime.now)
    address = models.TextField()
    winner = models.BooleanField(default=False)

    def is_eligible(self):
        """
        Consult the blockchain to see if they are actually tipping.
        """
        return True

def draw_winner(drawing_date):
    """
    For a given drawling date, select one submission out of the prior week
    randomly
    """
    week_ago = drawing_date - datetime.timedelta(days=7)

    all_submissions = GiveawaySubmission.objects.filter(
        date_created__gt=week_ago,
        date_created__lt=drawing_date,
        winner=False
    )

    while True:
        candidate = random.choice(all_submissions)
        if candidate.is_eligible():
            return candidate
