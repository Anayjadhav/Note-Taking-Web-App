from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def generate_Note_id():
    return str(uuid.uuid4()).split("-")[-1] #generate unique note id

class TakeNotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    Note_id = models.CharField(max_length=255, blank=True)
    Add_notes = models.TextField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    def __str__(self):  
        return "{} - {}".format(self.title, self.note_id)

    def save(self, *args, **kwargs):
        if len(self.Note_id.strip(" "))==0:
            self.Note_id = generate_Note_id()

        super(TakeNotes, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-created"]

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    def __str__(self):
        return self.user.username