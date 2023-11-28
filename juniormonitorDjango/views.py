# Asegúrate de tener estas importaciones al principio de tu archivo
import json

from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views import View
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

# views.py

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})



@csrf_exempt
@login_required
def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        user = request.user
        if user.groups.filter(name__in=['padres', 'profesores']).exists():
            try:
                verificar_usuario(request)
                enviar_correo(request)
                return JsonResponse({'message': 'Operación exitosa'})
            except ValidationError as ve:
                return JsonResponse({'error': str(ve)}, status=400)
            except BadHeaderError:
                return JsonResponse({'error': 'Encabezado de correo no válido'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Acceso no autorizado'}, status=403)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def LoginView(request):  # Asegúrate de tener 'request' como parámetro
    if request.method == 'POST':
        data = request.POST
        username = data.get('username', '')
        password = data.get('password', '')
        
        try:
            padre = Padre.objects.get(username=username)
            user = authenticate(request, username=padre.user.username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Inicio de sesión exitoso'})
            else:
                return JsonResponse({'error': 'Credenciales no válidas'}, status=401)
        except Padre.DoesNotExist:
            return JsonResponse({'error': 'Padre no encontrado'}, status=404)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)


@require_POST
def enviar_correo(request):
    try:
        # Verificar si el usuario está autenticado
        if request.user.is_authenticated:
            user = request.user
            remitente = user.email
        else:
            raise ValidationError('Usuario no autenticado')

        data = json.loads(request.body)
        destinatario = data.get('destinatario', '')
        asunto = data.get('asunto', '')
        mensaje = data.get('mensaje', '')

        # Validar la dirección de correo electrónico
        validate_email(destinatario)

        if not destinatario or not asunto or not mensaje:
            raise ValidationError('Se requieren destinatario, asunto y mensaje')

        # Envía el correo utilizando EmailMessage para permitir HTML en el mensaje
        email = EmailMessage(asunto, mensaje, remitente, [destinatario])
        email.send()

        return JsonResponse({'mensaje': 'Correo enviado exitosamente'})
    except ValidationError as ve:
        raise ve
    except BadHeaderError:
        raise BadHeaderError('Encabezado de correo no válido')
    except Exception as e:
        raise e
