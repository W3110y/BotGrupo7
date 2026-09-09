from BotInRedUC3M import BotInRedUC3M
from robocode_tank_royale.bot_api.events import ScannedBotEvent

class BotGrupo7(BotInRedUC3M):

    def __init__(self):
        super().__init__("BotGrupo7.json") # vuestro .json
        
    # Lógica principal: se repite cada turno de la ronda
    def run(self):
        while self.running:
            self.set_turn_radar_right(45) # barrer el radar SIEMPRE
            self.go() # cierra el turno

    # Os han escaneado a un rival -> aquí va vuestro targeting / movimiento
    def on_scanned_bot(self, e: ScannedBotEvent):
        self.set_fire(1)
        # (Opcional) lógica por turno

    def on_tick(self, e):
        pass

def main():
    BotGrupo7().start()

if __name__ == "__main__":
    main()
