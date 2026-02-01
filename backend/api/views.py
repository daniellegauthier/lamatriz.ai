from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnalyzeRequest
from core.analyze import analyze
from django.http import HttpResponse
from .cache import load_png

@api_view(["POST"])
def analyze_view(request):
    serializer = AnalyzeRequest(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        result = analyze(**serializer.validated_data)
    except ValueError as e:
        return Response({"error": str(e)}, status=400)

    return Response(result, status=status.HTTP_200_OK)

def gnh_plot_view(request, key: str):
    png = load_png(key)
    if not png:
        return HttpResponse(status=404)

    return HttpResponse(png, content_type="image/png")

