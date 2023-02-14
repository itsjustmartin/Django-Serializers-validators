# Question 3 & 4: Add any imports you need
from math import floor
from rest_framework import serializers

from assessment.models import AppointmentRequest, Stylist


# We want to ensure that the stylist’s name contains both first and last names, i.e. that it contains a space anywhere in it
def validate_full_name(value):
    # Question 2: Complete this function
    if " " not in value:
        raise serializers.ValidationError(
            "Name must have first and last name(s) separated by space(s)."
        )

    return value


class AppointmentRequestSerializer(serializers.Serializer):
    # Question 1 & 2: Create and edit fields
    #should have a maximum length of 70 characters
    stylist_name = serializers.CharField(max_length=70, validators=[validate_full_name])
     #  The datetime field should contain the date and time of the appointment
    start_datetime = serializers.DateTimeField()
    # should have a minimum value of 5 and maximum value of 60. This field is not required as we provide a default in the AppointmentRequest class.
    session_length = serializers.IntegerField(min_value=5, max_value=60, required=False)

    # Question 3: Implement validation method
    #Sessions can only be booked in 5-minute increments. Any request session_length should be rounded down to the nearest 5 minutes. For example, 49 minutes becomes 45, 44 to 40
    @staticmethod
    def validate_session_length(value):
        return 5 * floor(value / 5)

    def create(self, validated_data):
        return AppointmentRequest(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

# Stylist model has been created to store information about stylists who work at a salon. Complete the StylistSerializer class to serialize it, including all the fields.
class StylistSerializer(serializers.ModelSerializer):
    # Question 4: Implement this serializer
    class Meta():
        model = Stylist
        fields = "__all__"