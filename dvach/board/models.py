from django.db import models
from django.contrib import admin

class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    reply_to = models.ForeignKey("Message", null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text

    def get_replies(self):
        return list(Message.objects.filter(reply_to=self))

    replies = property(get_replies)
        
admin.site.register(Message)