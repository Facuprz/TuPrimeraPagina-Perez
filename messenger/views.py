# messenger/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Message
from .forms import MessageForm


class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messenger/inbox.html"
    context_object_name = "messages"
    paginate_by = 15

    def get_queryset(self):
        return (
            Message.objects
            .filter(recipient=self.request.user)
            .select_related("sender", "recipient")
        )


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "messenger/detail.html"
    context_object_name = "message"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.sender != self.request.user and obj.recipient != self.request.user:
            raise PermissionDenied("No podés ver este mensaje.")
        if obj.recipient == self.request.user and not obj.read:
            obj.read = True
            obj.save(update_fields=["read"])
        return obj


class ComposeView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "messenger/compose.html"
    success_url = reverse_lazy("inbox")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user  # para excluirse del selector
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        to = self.request.GET.get("to")
        if to and to.isdigit():
            initial["recipient"] = int(to)
        return initial

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
