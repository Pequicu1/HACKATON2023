from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.us, name="us"),
    path("dia", views.dia, name="dia"),
    path("grades", views.grades, name="grades"),
    path("nextstep", views.nextstep, name="nextstep"),
    path("todo", views.todo, name="todo"),
]