from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=254)
    country_code = serializers.CharField(max_length=254)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
