from . import models

def todo_count(request):
    dict2= {}
    dict2["todo_count"] = models.Task.objects.all().count
    return dict2