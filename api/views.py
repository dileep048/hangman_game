# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework .decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer
from random import choice
from .constants import WORDS

class GameViewSet(ViewSet):
    """
    A ViewSet for managing the Hangman game API.
    
    This ViewSet contains endpoints to start a new game, retrieve the game state,
    and allow the player to make guesses. It manages the game lifecycle and tracks
    the player's progress.
    """
    
    @action(detail=False, methods=['post'], url_path='new')
    def create_game(self, request):
        """Handles creating a new game."""
        word = choice(WORDS).lower() 
        game = Game.objects.create(
            word=word,
            max_incorrect_guesses= ((len(word) // 2) + len(word) % 2)
        )
        return Response({'game_id': game.id}, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        """Returns the current game state."""
        try:
            game = Game.objects.get(id=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Game.DoesNotExist:
            return Response({'error': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'], url_path='guess')
    def guess_word(self, request, pk):
        """Handles a letter guess for a specific game instance."""
        try:
            game = Game.objects.get(id=pk)
        except Game.DoesNotExist:
            return Response({'error': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)

        letter = str(request.data.get('letter', '')).lower()

        if len(letter) != 1 or not letter.isalpha():
            return Response({'error': 'Invalid guess. Must be a single letter.'}, status=status.HTTP_400_BAD_REQUEST)

        if letter in game.guessed_letters:
            return Response({'error': 'Letter already guessed.'}, status=status.HTTP_400_BAD_REQUEST)

        game.guessed_letters += letter

        if letter not in game.word:
            game.incorrect_guesses += 1

        game.check_game_status()
        serializer = GameSerializer(game)
        return Response({
            'correct': letter in game.word,
            'game_state': serializer.data
        }, status=status.HTTP_200_OK)
