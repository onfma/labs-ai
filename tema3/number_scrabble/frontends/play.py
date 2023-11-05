from number_scrabble.game.engine import TicTacToe
from number_scrabble.game.players import RandomComputerPlayer, MinimaxComputerPlayer
from number_scrabble.logic.models import Mark

from console.players import ConsolePlayer
from console.renderers import ConsoleRenderer

player1 = ConsolePlayer(Mark("X"))
player2 = MinimaxComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()
