class Settings:

    def __init__(self):

        #Game
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Dragon
        self.dragon_speed = 0.5
        self.dragon_limit = 3

        #Bullets
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Gems
        self.gem_speed = 0.15
        self.fleet_drop_speed = 30
        self.fleet_direction = 1