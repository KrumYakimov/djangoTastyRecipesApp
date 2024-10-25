from django import forms


class RecipeFormPlaceholderMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Setting the placeholders for each field
        form.fields["ingredients"].widget = forms.Textarea(
            attrs={"placeholder": "ingredient1, ingredient2, ..."}
        )

        form.fields["instructions"].widget = forms.Textarea(
            attrs={"placeholder": "Enter detailed instructions here..."}
        )

        form.fields["image_url"].widget = forms.URLInput(
            attrs={"placeholder": "Optional image URL here..."}
        )
        return form


class RecipeFormHelpTextMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields["ingredients"].help_text = "Ingredients must be separated by a comma and space."
        form.fields["cooking_time"].help_text = "Provide the cooking time in minutes."

        return form
