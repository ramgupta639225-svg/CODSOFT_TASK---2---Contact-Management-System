from rest_framework import serializers
from .models import Contact
import re



class ContactSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Name cannot be blank')
        return value.strip()

    def validate_email(self, value):
        email = value.strip().lower()
        existing = Contact.objects.filter(email=email)

        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise serializers.ValidationError('Email already exists')
        return email

    def validate_phone(self, value):
        phone = value.strip()
        if not re.fullmatch(r'(\+91)?[6-9]\d{9}', phone):
            raise serializers.ValidationError('Enter a Valid Indian phone number')

        existing = Contact.objects.filter(phone=phone)

        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise serializers.ValidationError('Phone number already exists')
        return phone



    def validate_address(self, value):
        if not value.strip():
            raise serializers.ValidationError('Address cannot be blank')
        return value.strip()


    def validate_company(self, value):
        if not value.strip():
            raise serializers.ValidationError('Company cannot be blank')
        return value.strip()


    class Meta:
        model = Contact
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


        # fields = ["name", "email", "phone", "address", "company"]


