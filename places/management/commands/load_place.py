import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Picture, Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'place_url',
            type=str,
            help='Ссылка на локации',
        )

    def handle(self, *args, **options):
        url = options['place_url']
        response = requests.get(url)
        response.raise_for_status()
        place = response.json()
        current_place, _ = Place.objects.get_or_create(
            title=place['title'],
            defaults={
                'short_description': place['description_short'],
                'long_description': place['description_long'],
                'lat': place['coordinates']['lat'],
                'lon': place['coordinates']['lng'],
            },
        )

        image_urls = place['imgs']
        for image_url in image_urls:
            response = requests.get(image_url)
            response.raise_for_status()
            image_content = ContentFile(response.content, name=os.path.split(image_url)[1])
            Picture.objects.create(place_pic=current_place, image=image_content)
