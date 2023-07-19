from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from .models import Task


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def page_account(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "base/account.html")
    sign = request.POST["sign"]
    if sign == "in":
        pass
    elif sign == "up":
        pass
    else:
        pass
    return render(request, "base/account.html")


def page_logout(request, *args, **kwargs):
    return render(request, "base/logout.html")


def page_about(request, *args, **kwargs):
    return render(request, "base/about.html")


def page_service(request, *args, **kwargs):
    return render(request, "base/service.html")


def page_home(request, *args, **kwargs):
    return render(request, "base/home.html")


class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    login_url = "account"

    def post(self, request, *args, **kwargs):
        task_id = request.POST["pk"]
        task = get_or_none(Task, id=task_id)
        if task is not None:
            task.complete = not task.complete
            task.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__icontains=search_input)

        context["search_input"] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "base/task.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")


class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
