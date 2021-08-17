from entries.models import Entry
from entries.serializers import EntrySerializer

from django.http import Http404

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'entries': reverse('entry-list', request=request, format=format)
    })

class EntryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Entry.objects.all().order_by('entry_title')
    serializer_class = EntrySerializer
    permission_classes = []


    @method_decorator(cache_page(60*60*1))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class EntryDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Entry.objects.get(pk=pk)
        except Entry.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)
