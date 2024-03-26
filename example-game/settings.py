class Settings:
    """Class for game settings"""
#     
    
    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 512
        self.caption = "Avoid The Bubbles"
        self.background_color = (0,0,90)
        
        self.bubble_min_r = 10
        self.bubble_max_r = 50