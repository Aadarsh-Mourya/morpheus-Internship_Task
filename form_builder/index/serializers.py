from rest_framework import serializers
from .models import Form, Questions, Choices, Answer, Responses

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ['id', 'choice', 'is_answer']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Questions
        fields = ['id', 'question', 'question_type', 'required', 'answer_key', 
                 'score', 'feedback', 'choices']

class FormSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Form
        fields = ['id', 'code', 'title', 'description', 'creator', 
                 'background_color', 'text_color', 'collect_email',
                 'authenticated_responder', 'edit_after_submit', 
                 'confirmation_message', 'is_quiz', 'allow_view_score',
                 'questions']