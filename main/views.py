from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.mail import send_mail

from .models import SiteModel
from .serializers import SiteSerializer



class SiteListView(APIView):
    """Выводит список сайтов из портфолио"""

    def get(self, request):
        sites = SiteModel.objects.all()
        serializer = SiteSerializer(sites, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)


class SiteDetailView(APIView):
    """Выводит детальную информацию по сайту"""

    def get(self, request, site_id):
        site = get_object_or_404(SiteModel, id=site_id) 
        serializer = SiteSerializer(site)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactMailView(APIView):
    """Отправляет сообщение на мою почту"""

    def post(self, request):
        data = request.data
        print(data)
        name = data['name']
        email = data['email']
        text = data['text']

        message = f'Сообщение от {name}:\n\n{text} \n\nС уважением: {email}'

        try:
            send_mail('Сообщение с сайта-портфолио',
                      message,
                      email,
                      ['grekovdima7@gmail.com'])
            return Response({'status': 'ok'})
        except:
            error = "Сообщение не отправлено"
            return Response({'status': 'bad_request'})