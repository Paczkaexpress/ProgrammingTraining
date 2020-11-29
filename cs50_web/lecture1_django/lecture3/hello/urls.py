from django.urls import path
from . import views # can be used to import the local files (same directory)

urlpatterns = [
    path("", views.index, name="index"),
    path("mateusz", views.mateusz, name="mateuszIndex"),
    path("<str:name>",views.greet, name="greet")
]
