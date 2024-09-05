from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.models import UserModel
from api.serializers import UserSerializer, DLOSerializer
from api.utils import DLOBuilderUtil

class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class GenerateDLO(RetrieveAPIView):
    serializer_class = DLOSerializer
    queryset = UserModel.objects.all()

    def retrieve(self, _, *args, **kwargs):
        id = kwargs.get("pk")
        user = get_object_or_404(UserModel, pk= id)
        url = DLOBuilderUtil().generate_dlo(user.user_id, user.user_type)
        response = self.get_serializer({"url": url})
        return Response(response.data)

