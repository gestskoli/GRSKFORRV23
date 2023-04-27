import arcade
import random

# Vefsíða arcade: https://api.arcade.academy/en/latest/index.html

# Myndir (e. sprites) sem notaðar eru í leiknum
# Fleiri myndir hér: https://api.arcade.academy/en/latest/resources.html
MYND_LEIKMADUR_GEIMSKIP = ":resources:images/space_shooter/playerShip1_orange.png"
MYND_OVINUR_GEIMSKIP = ":resources:images/space_shooter/playerShip1_green.png"
MYND_SKOT = ":resources:images/space_shooter/laserBlue01.png"
MYND_BAKGRUNNUR = ":resources:images/backgrounds/stars.png"
MYND_SPRENGING = ":resources:images/spritesheets/explosion.png"
HLJOD_LAZER = ":resources:sounds/laser2.wav"
HLJOD_SPRENGING = ":resources:sounds/explosion2.wav"

# Aðrir fastar (e. constant) fyrir leikinn
BREIDD = 800
HAED = 600
NAFN_LEIKS = "Skotleikurinn"
SKALI = 0.75
HRADI_SKOTA = 10
FJOLDI_MYNDA_I_SPRENGINGU = 60
