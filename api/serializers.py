from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    display_word = serializers.SerializerMethodField()
    incorrect_guesses_left = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'status', 'display_word', 'incorrect_guesses', 'incorrect_guesses_left']

    def get_display_word(self, obj):
        return obj.get_display_word()

    def get_incorrect_guesses_left(self, obj):
        return obj.get_incorrect_guesses_left()
