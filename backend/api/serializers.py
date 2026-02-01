from rest_framework import serializers

class AnalyzeRequest(serializers.Serializer):
    text = serializers.CharField()
    sequence = serializers.CharField()

class AnalyzeResponse(serializers.Serializer):
    sentiment = serializers.FloatField()
    emotion = serializers.CharField()
    emotion_confidence = serializers.FloatField()
    accomplishment = serializers.FloatField()
    phrase = serializers.CharField()
