from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    preferred_locale = serializers.CharField(
        required=False,
        max_length=2,
    )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['preferred_locale'] = self.validated_data.get('preferred_locale', '')
        return data_dict