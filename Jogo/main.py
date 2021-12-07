import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

from connection import Bluetooth
bt = Bluetooth()

class PongPaddle(Widget):
    score = NumericProperty(0)
    can_bounce = BooleanProperty(True)

    def bounce_ball(self, ball): #toda vez que a função é chamada, realizar uma vibração curta (ping, pong..)
        if self.collide_widget(ball) and self.can_bounce:
            bt.send(code='4')
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            self.can_bounce = False
        elif not self.collide_widget(ball) and not self.can_bounce:
            self.can_bounce = True


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    pause_game = BooleanProperty(False)
    endgame_message = StringProperty('')

    def __init__(self):
        super(PongGame, self).__init__()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down = self._on_keyboard_down)
        self._keyboard.bind(on_key_up = self._on_keyboard_up)
        self.pressed_keys = set()
        

    def _keyboard_closed (self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down (self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(keycode[1])

    def _on_keyboard_up(self, keyboard, keycode):
        self.pressed_keys.remove(keycode[1])

    def _player_position_update(self):
        if 'w' in self.pressed_keys:
            self.player1.center_y += 15
        if 's' in self.pressed_keys:
            self.player1.center_y -= 15
        if 'up' in self.pressed_keys:
            self.player2.center_y += 15
        if 'down' in self.pressed_keys:
            self.player2.center_y -= 15

    def serve_ball(self, vel=(4, 0)): #toda vez que a função é chamada, realizar uma vibração longa (vooosh)- dar uma pausa antes do efeito para que tenha a vibração correspondente ao jogador que venceu
        self.ball.center = self.center
        self.ball.velocity = vel
        bt.send(code='3')
        
#1: ..-
#2: _..
# ou fazer o jogo só para um jogador já que estou fazendo só para uma pulseira (perguntar para a prof)
#     
    def endgame(self, max_score = 5):
        flag = False
        if self.player1.score >= max_score:
            self.endgame_message = "[color=3333ff]Jogador 1 venceu[/color]"
            flag = True
        elif self.player2.score >= max_score:
            self.endgame_message = "[color=#ff820d]Jogador 2 venceu[/color]"
            flag = True
    
        if flag:
            self.pause_game = True
            Clock.schedule_once(self.start_game, 5)
            self.player1.score = 0
            self.player2.score = 0
            bt.send(code='5')

    def start_game(self, *args):
        self.endgame_message = ''
        self.pause_game = False

    def update(self, dt):
        if self.pause_game:
            return

        self._player_position_update()
        self.ball.move()

        # bounce ball off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went off a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
            bt.send(code='2')
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))
            bt.send(code='1')

        self.endgame(5)


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

# Eventos
# 1 - Jogador 1 faz um ponto
# 2 - Jogador 2 faz um ponto
# 3 - Bola servida
# 4 - Bola quica
# 5 - Fim de jogo

# Novas funcionalidades
# 1 - Fim de jogo com 5 pontos
# 2 - Delay de "animação" depois que um jogador faz um ponto ate a bola ser servida


if __name__ == '__main__':
    PongApp().run()