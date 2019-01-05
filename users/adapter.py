from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    
    def save_user(self, request, user, form, commit=False):
        print("CustomAccountAdapter.save_user()")
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        print("form.cleaned_data:")
        print(form.cleaned_data)
        user.preferred_locale = data.get('preferred_locale')
        user.save()
        return user