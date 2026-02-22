from django.db import models

# Hamper Request Data Fields
# This model represents a single hamper request submitted by a user
class HamperRequest(models.Model):

    # Stores the the priority of the request
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    # Stores the name of the student requesting a hamper
    student_name = models.CharField(max_length=100)
    
    # Stores the family size  of the student
    family_size = models.PositiveIntegerField()
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="medium"
    )
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.get_priority_display()} priority)"