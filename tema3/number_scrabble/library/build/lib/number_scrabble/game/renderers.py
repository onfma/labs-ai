# number_scrabble/game/renderers.py

import abc

from number_scrabble.logic.models import GameState

class Renderer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """Render the current game state."""
