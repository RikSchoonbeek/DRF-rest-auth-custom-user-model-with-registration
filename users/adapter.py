from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        keys_to_get = ['preferred_locale', 'telephone_number']
        for key in keys_to_get:
            value = data.get(key)
            setattr(user, key, value)
        user.save()
        return user
