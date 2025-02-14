
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User


from .serializers import UserDetailSerializer
from property.serializers import ReservationsListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserDetailSerializer(user, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def reservations_list(request):
    reservations = request.user.reservations.all()
    print('user', request.user)
    print(reservations)
    serializer = ReservationsListSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST', 'FILES'])
def profile_detail(request):
    try:
        user = User.objects.get(pk=request.user.id)
        user.avatar= request.FILES['avatar']
        user.name = request.POST.get('name', '')
        user.save()

        return JsonResponse({'success': True})
    except Exception as e:
        print('Error', e)
        return JsonResponse({'success': False})
