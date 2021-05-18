import json

from django.db import models


class Sequence(models.Model):
    items = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return json.dumps({"items": self.items, "result": self.result})

    @property    
    def result(self):
        items_json = json.loads('{"items": %s}' % self.items)
        return list(flatten(items_json["items"]))


def flatten(lst):
     for x in lst:
         if isinstance(x, list):
             for x in flatten(x):
                 yield x
         else:
             yield x