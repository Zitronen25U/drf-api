
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import BlogSerializer
from .models import Blog



class blogpostlist(ListAPIView):
    queryset = Blog.objects.all
    serializer_class = BlogSerializer


class blogpostdetail(RetrieveAPIView):
    queryset = Blog.objects.all
    serializer_class = BlogSerializer