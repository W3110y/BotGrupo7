from BotInRedUC3M import BotInRedUC3M
from robocode_tank_royale.bot_api.events import ScannedBotEvent
from robocode_tank_royale.bot_api.events import HitByBulletEvent

class BotGrupo7(BotInRedUC3M):

    def __init__(self):
        super().__init__("BotGrupo7.json") # vuestro .json
        
    # Lógica principal: se repite cada turno de la ronda
    def run(self):
        while self.running:
            self.set_turn_radar_right(45) # barrer el radar SIEMPRE
            self.forward(100)
            self.turn_gun_left(360)
            self.back(100)
            self.turn_gun_left(360)
            self.go() # cierra el turno

    # Os han escaneado a un rival -> aquí va vuestro targeting / movimiento
    def on_scanned_bot(self, e: ScannedBotEvent):
        self.set_fire(1)
        self.forward(100)

    def on_hit_by_bullet(self, e: HitByBulletEvent):
        self.set_turn_left(100)
        self.set_turn_right(100)


    # (Opcional) lógica por turno
    def on_tick(self, e):
        pass

def main():
    BotGrupo7().start()

if __name__ == "__main__":
    main()
