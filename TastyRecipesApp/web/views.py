from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from TastyRecipesApp.profiles.models import Profile
from TastyRecipesApp.utils.profile_helpers import get_profile


class ProfileCreateView(CreateView):
    model = Profile
    fields = ["nickname", "first_name", "last_name", "chef"]
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IndexView(TemplateView):
    template_name = "web/home-page.html"

    def get(self, request, *args, **kwargs):
        profile = get_profile()

        if profile is None:
            return redirect("profile-create")

        return self.render_to_response({'profile_exists': True})