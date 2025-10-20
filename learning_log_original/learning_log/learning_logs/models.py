from django.db import models
from django.contrib.auth.models import User
#To hold topic names [max 200 characters] and timestamp
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

"""Each entry needs to be associated with a particular
topic. This relationship is called a many-to-one relationship, meaning many
entries can be associated with one topic"""

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """Return a string representation of the model."""
        #We also add an ellipsis[...] to clarify that we’re not always displaying the entire entry
        return f"{self.text[:50]}..." 