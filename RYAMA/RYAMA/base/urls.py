from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import path

from .views import (
    TaskCreate,
    TaskDelete,
    TaskDetail,
    TaskList,
    TaskUpdate,
    page_about,
    page_account,
    page_home,
    page_service,
)

urlpatterns = [
    path(
        "test/",
        lambda request, *args, **kwargs: render(request, "base/test.html"),
        name="test",
    ),
    path("about/", page_about, name="about"),
    path("service/", page_service, name="service"),
    path("account/", page_account, name="account"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("", page_home, name="home"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("tasks/", TaskList.as_view(), name="tasks"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
]
