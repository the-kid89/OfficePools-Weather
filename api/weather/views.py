# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from rest_framework import viewsets
from rest_framework.response import Response

import requests

from officepools_weather.open_weather_map_settings import OPEN_WEATHER_MAP_URI
from .serializers import WeatherSerializer


class WeatherViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        http://api.openweathermap.org/data/2.5/forcast?q=London,uk&appid=a1cc1a050abfbded18d587f0a98f04ef
        http://api.openweathermap.org/data/2.5/forecast?q=London,us&appid=a1cc1a050abfbded18d587f0a98f04ef
        :param request:
        :return:
        """
        serializer = WeatherSerializer(data=request.GET)
        if serializer.is_valid():
            uri = OPEN_WEATHER_MAP_URI.format(
                city=serializer.validated_data['city'], country_code=serializer.validated_data['country_code'])
            weather_response = requests.get(uri)
            response = Response(weather_response.json())
            if settings.DEBUG:
                response['Access-Control-Allow-Origin'] = '*'
            return response

        return Response(serializer.errors)
