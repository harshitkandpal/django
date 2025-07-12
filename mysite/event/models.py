from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    time = models.TimeField()
    event_type = models.CharField(max_length=50, choices=[
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('webinar', 'Webinar'),
        ('meetup', 'Meetup'),
        ('networking', 'Networking'),
        ('festival', 'Festival'),
        ('concert', 'Concert'),
        ('exhibition', 'Exhibition'),
        ('trade_show', 'Trade Show'),
        ('panel_discussion', 'Panel Discussion'),
        ('product_launch', 'Product Launch'),
        ('community_event', 'Community Event'),
        ('charity_event', 'Charity Event'),
        ('sports_event', 'Sports Event'),
        ('cultural_event', 'Cultural Event'),
        ('educational_event', 'Educational Event'),
        ('corporate_event', 'Corporate Event'),
        ('social_event', 'Social Event'),
        ('wedding', 'Wedding'),
        ('birthday_party', 'Birthday Party'),
        ('anniversary', 'Anniversary'),
        ('family_reunion', 'Family Reunion'),
        ('graduation', 'Graduation'),
        ('holiday_party', 'Holiday Party'),
        ('retirement_party', 'Retirement Party'),
        ('theater_performance', 'Theater Performance'),
        ('film_screening', 'Film Screening'),
        ('art_show', 'Art Show'),
        ('book_signing', 'Book Signing'),
        ('food_festival', 'Food Festival'),
        ('other', 'Other'),
    ])
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
