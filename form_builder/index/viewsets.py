from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Form, Questions, Choices
from .serializers import FormSerializer, QuestionSerializer, ChoiceSerializer

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    
    @action(detail=True, methods=['post'])
    def edit_title(self, request, pk=None):
        form = self.get_object()
        form.title = request.data.get('title')
        form.save()
        return Response({'status': 'title updated'})
    
    @action(detail=True, methods=['post'])
    def edit_description(self, request, pk=None):
        form = self.get_object()
        form.description = request.data.get('description')
        form.save()
        return Response({'status': 'description updated'})

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    
    @action(detail=True, methods=['post'])
    def edit_question(self, request, pk=None):
        question = self.get_object()
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choices.objects.all()
    serializer_class = ChoiceSerializer
