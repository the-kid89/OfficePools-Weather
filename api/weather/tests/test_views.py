# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict

from django.test import TestCase

from rest_framework.test import APIRequestFactory

import responses

from weather.views import WeatherViewSet
from weather.test_data.weather_viewset import forecast_response
from officepools_weather.open_weather_map_settings import OPEN_WEATHER_MAP_URI


class TestWeatherViewSet(TestCase):
    @responses.activate
    def test_get_with_valid_data(self):
        responses.add(
            responses.GET,
            OPEN_WEATHER_MAP_URI.format(city='london', country_code='uk'),
            json=forecast_response,
            status=200
        )

        factory = APIRequestFactory()
        request = factory.get('/api/weather/', {'city': 'london', 'country_code': 'uk'}, format='json')
        response = WeatherViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(200, response.status_code)
        self.assertEqual(forecast_response, response.data)

    @responses.activate
    def test_get_with_extra_values(self):
        responses.add(
            responses.GET,
            OPEN_WEATHER_MAP_URI.format(city='london', country_code='uk'),
            json=forecast_response,
            status=200
        )

        factory = APIRequestFactory()
        request = factory.get('/api/weather/', {'city': 'london', 'country_code': 'uk', 'test': 'test'}, format='json')
        response = WeatherViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(200, response.status_code)
        self.assertEqual(forecast_response, response.data)

    @responses.activate
    def test_get_with_missing_country_code(self):
        responses.add(
            responses.GET,
            OPEN_WEATHER_MAP_URI.format(city='london', country_code='uk'),
            json=forecast_response,
            status=200
        )

        factory = APIRequestFactory()
        request = factory.get('/api/weather/', {'city': 'london'}, format='json')
        response = WeatherViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(200, response.status_code)
        self.assertEqual({"country_code": ["This field is required."]}, response.data)

    @responses.activate
    def test_get_with_missing_city(self):
        responses.add(
            responses.GET,
            OPEN_WEATHER_MAP_URI.format(city='london', country_code='uk'),
            json=forecast_response,
            status=200
        )

        factory = APIRequestFactory()
        request = factory.get('/api/weather/', {'country_code': 'uk'}, format='json')
        response = WeatherViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(200, response.status_code)
        self.assertEqual({"city": ["This field is required."]}, response.data)

    def test_post(self):
        factory = APIRequestFactory()
        request = factory.post('/api/weather/', {}, format='json')
        response = WeatherViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(405, response.status_code)
        self.assertEqual({"detail": "Method \"POST\" not allowed."}, response.data)

    def test_put(self):
        factory = APIRequestFactory()
        request = factory.put('/api/weather/')
        response = WeatherViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(405, response.status_code)
        self.assertEqual({"detail": "Method \"PUT\" not allowed."}, response.data)

    def test_delete(self):
        factory = APIRequestFactory()
        request = factory.delete('/api/weather/')
        response = WeatherViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(405, response.status_code)
        self.assertEqual({"detail": "Method \"DELETE\" not allowed."}, response.data)

    def test_options(self):
        factory = APIRequestFactory()
        request = factory.options('/api/weather/')
        response = WeatherViewSet.as_view({'get': 'list'})(request)

        self.assertEqual(200, response.status_code)
        expected_response = OrderedDict([
            (u'name', u'Weather'), (u'description', u''), (u'renders', [u'application/json', u'text/html']),
            (u'parses', [u'application/json', u'application/x-www-form-urlencoded', u'multipart/form-data'])])

        self.assertEqual(expected_response, response.data)
