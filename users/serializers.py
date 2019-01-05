from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    preferred_locale = serializers.CharField(
        required=False,
        max_length=2,
    )
    telephone_number = serializers.CharField(
        max_length=63,
        required=False,
    )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        keys_to_get = ['preferred_locale', 'telephone_number']
        for key in keys_to_get:
            try:
                data_dict[key] = self.validated_data.get(key, '')
            except KeyError:
                pass
        return data_dict
