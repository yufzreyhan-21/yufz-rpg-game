import turtle
import random
import math
from enum import Enum

# ===== GAME CONFIG =====
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GAME_TITLE = "⚔️ DUNIA YUFZ - 2D RPG ADVENTURE ⚔️"

# ===== COLORS =====
class Color:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED = "#FF0000"
    GREEN = "#00FF00"
    BLUE = "#0000FF"
    YELLOW = "#FFFF00"
    CYAN = "#00FFFF"
    MAGENTA = "#FF00FF"
    ORANGE = "#FFA500"
    PURPLE = "#800080"
    GRAY = "#808080"
    DARK_RED = "#8B0000"
    DARK_GREEN = "#006400"
    DARK_BLUE = "#00008B"

# ===== GAME STATE =====
class GameState(Enum):
    MENU = 1
    PLAYING = 2
    BATTLE = 3
    SHOP = 4
    INVENTORY = 5
    PAUSED = 6

# ===== WEAPON & ARMOR =====
WEAPONS = {
    "Wooden Sword": {"attack": 5, "cost": 30, "color": Color.YELLOW},
    "Iron Sword": {"attack": 12, "cost": 80, "color": Color.GRAY},
    "Steel Blade": {"attack": 18, "cost": 150, "color": Color.CYAN},
    "Dragon Slayer": {"attack": 28, "cost": 500, "color": Color.RED},
}

ARMORS = {
    "Cloth Armor": {"defense": 3, "hp": 10, "cost": 25, "color": Color.BLUE},
    "Leather Armor": {"defense": 7, "hp": 20, "cost": 70, "color": Color.ORANGE},
    "Plate Armor": {"defense": 20, "hp": 70, "cost": 400, "color": Color.GRAY},
}

# ===== ENEMIES =====
ENEMIES = {
    "Goblin": {"hp": 30, "attack": 5, "exp": 50, "gold": 25, "color": Color.GREEN},
    "Orc": {"hp": 60, "attack": 10, "exp": 100, "gold": 50, "color": Color.DARK_GREEN},
    "Skeleton": {"hp": 45, "attack": 9, "exp": 100, "gold": 50, "color": Color.WHITE},
    "Dark Knight": {"hp": 80, "attack": 15, "exp": 150, "gold": 100, "color": Color.BLACK},
}

BOSSES = {
    "Dungeon Guardian": {"hp": 200, "attack": 20, "exp": 500, "gold": 300, "color": Color.PURPLE},
    "Fire Dragon": {"hp": 350, "attack": 28, "exp": 1000, "gold": 700, "color": Color.DARK_RED},
    "Shadow King": {"hp": 300, "attack": 25, "exp": 800, "gold": 500, "color": Color.BLACK},
}

# ===== PLAYER CLASS =====
class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.exp = 0
        self.exp_to_level = 200
        self.gold = 200
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None
        
        # Visual
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(Color.CYAN)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.showturtle()
        
    def move(self, dx, dy):
        new_x = self.x + dx * 5
        new_y = self.y + dy * 5
        
        # Keep in bounds
        if -SCREEN_WIDTH/2 < new_x < SCREEN_WIDTH/2 and -SCREEN_HEIGHT/2 < new_y < SCREEN_HEIGHT/2:
            self.x = new_x
            self.y = new_y
            self.turtle.goto(self.x, self.y)
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        return actual_damage
    
    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)
    
    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.exp_to_level:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.exp = 0
        self.exp_to_level += 100
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 2
    
    def equip_weapon(self, weapon_name):
        if weapon_name in WEAPONS:
            self.equipped_weapon = weapon_name
            weapon = WEAPONS[weapon_name]
            self.attack = 10 + weapon["attack"]
            return True
        return False
    
    def equip_armor(self, armor_name):
        if armor_name in ARMORS:
            self.equipped_armor = armor_name
            armor = ARMORS[armor_name]
            self.defense = 5 + armor["defense"]
            self.max_hp = 100 + armor["hp"]
            return True
        return False

# ===== ENEMY CLASS =====
class Enemy:
    def __init__(self, name, x, y, is_boss=False):
        self.name = name
        self.x = x
        self.y = y
        self.is_boss = is_boss
        
        if is_boss:
            enemy_data = BOSSES[name]
        else:
            enemy_data = ENEMIES[name]
        
        self.hp = enemy_data["hp"]
        self.max_hp = self.hp
        self.attack = enemy_data["attack"]
        self.exp = enemy_data["exp"]
        self.gold = enemy_data["gold"]
        self.color = enemy_data["color"]
        
        # Visual
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle" if not is_boss else "square")
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.showturtle()
        
        # Movement
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x < -SCREEN_WIDTH/2 or self.x > SCREEN_WIDTH/2:
            self.vx *= -1
        if self.y < -SCREEN_HEIGHT/2 or self.y > SCREEN_HEIGHT/2:
            self.vy *= -1
        
        self.turtle.goto(self.x, self.y)
    
    def take_damage(self, damage):
        self.hp -= damage
    
    def is_alive(self):
        return self.hp > 0
    
    def distance_to(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)

# ===== UI CLASS =====
class UI:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.pen.penup()
    
    def draw_text(self, x, y, text, size=12, color=Color.WHITE):
        self.pen.goto(x, y)
        self.pen.color(color)
        self.pen.write(text, align="left", font=("Arial", size, "normal"))
    
    def draw_hp_bar(self, x, y, current, max_hp, width=100, height=10):
        # Background
        self.pen.goto(x, y)
        self.pen.color(Color.RED)
        self.pen.pendown()
        for _ in range(2):
            self.pen.forward(width)
            self.pen.right(90)
            self.pen.forward(height)
            self.pen.right(90)
        self.pen.penup()
        
        # Fill
        if max_hp > 0:
            fill_width = (current / max_hp) * width
            self.pen.goto(x, y)
            self.pen.color(Color.GREEN)
            self.pen.pendown()
            for _ in range(2):
                self.pen.forward(fill_width)
                self.pen.right(90)
                self.pen.forward(height)
                self.pen.right(90)
            self.pen.penup()
    
    def clear(self):
        self.pen.clear()

# ===== GAME CLASS =====
class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.title(GAME_TITLE)
        self.screen.bgcolor(Color.BLACK)
        self.screen.tracer(0)
        
        self.state = GameState.MENU
        self.player = None
        self.enemies = []
        self.current_enemy = None
        self.ui = UI()
        
        self.setup_controls()
        self.show_menu()
    
    def setup_controls(self):
        self.screen.onkey(lambda: self.move_player(-1, 0), "Left")
        self.screen.onkey(lambda: self.move_player(1, 0), "Right")
        self.screen.onkey(lambda: self.move_player(0, 1), "Up")
        self.screen.onkey(lambda: self.move_player(0, -1), "Down")
        self.screen.onkey(self.handle_space, "space")
        self.screen.listen()
    
    def move_player(self, dx, dy):
        if self.player and self.state == GameState.PLAYING:
            self.player.move(dx, dy)
            self.check_collision()
    
    def check_collision(self):
        for enemy in self.enemies:
            distance = enemy.distance_to(self.player.x, self.player.y)
            if distance < 30:
                self.start_battle(enemy)
                break
    
    def start_battle(self, enemy):
        self.state = GameState.BATTLE
        self.current_enemy = enemy
        self.enemies.remove(enemy)
    
    def handle_space(self):
        if self.state == GameState.MENU:
            self.start_game()
        elif self.state == GameState.BATTLE:
            self.do_battle_action("attack")
        elif self.state == GameState.PLAYING:
            self.spawn_enemy()
    
    def start_game(self):
        self.player = Player("Hero", 0, 0)
        self.state = GameState.PLAYING
        self.spawn_enemies()
    
    def spawn_enemies(self):
        self.enemies = []
        for _ in range(5):
            x = random.uniform(-SCREEN_WIDTH/2 + 50, SCREEN_WIDTH/2 - 50)
            y = random.uniform(-SCREEN_HEIGHT/2 + 50, SCREEN_HEIGHT/2 - 50)
            enemy_name = random.choice(list(ENEMIES.keys()))
            self.enemies.append(Enemy(enemy_name, x, y))
    
    def spawn_enemy(self):
        if self.state == GameState.PLAYING:
            x = random.uniform(-SCREEN_WIDTH/2 + 50, SCREEN_WIDTH/2 - 50)
            y = random.uniform(-SCREEN_HEIGHT/2 + 50, SCREEN_HEIGHT/2 - 50)
            enemy_name = random.choice(list(ENEMIES.keys()))
            self.enemies.append(Enemy(enemy_name, x, y))
    
    def do_battle_action(self, action):
        if self.state != GameState.BATTLE:
            return
        
        if action == "attack":
            # Player attack
            damage = self.player.attack + random.randint(-5, 10)
            self.current_enemy.take_damage(damage)
            
            # Enemy counter attack
            if self.current_enemy.is_alive():
                enemy_damage = self.current_enemy.attack + random.randint(-3, 5)
                self.player.take_damage(enemy_damage)
            else:
                # Victory
                self.player.gain_exp(self.current_enemy.exp)
                self.player.gold += self.current_enemy.gold
                self.current_enemy.turtle.hideturtle()
                self.state = GameState.PLAYING
                self.current_enemy = None
            
            # Check if player died
            if self.player.hp <= 0:
                self.show_game_over()
    
    def show_menu(self):
        self.ui.draw_text(-300, 200, GAME_TITLE, 24, Color.CYAN)
        self.ui.draw_text(-300, 100, "2D RPG ADVENTURE GAME", 18, Color.WHITE)
        self.ui.draw_text(-300, 0, "Press SPACE to Start", 16, Color.YELLOW)
        self.ui.draw_text(-300, -100, "Controls:", 14, Color.WHITE)
        self.ui.draw_text(-300, -150, "Arrow Keys: Move", 12, Color.GRAY)
        self.ui.draw_text(-300, -200, "SPACE: Attack/Confirm", 12, Color.GRAY)
    
    def show_game_over(self):
        self.ui.clear()
        self.ui.draw_text(-200, 100, "GAME OVER!", 24, Color.RED)
        self.ui.draw_text(-200, 0, f"Level: {self.player.level}", 16, Color.WHITE)
        self.ui.draw_text(-200, -50, f"Gold: {self.player.gold}", 16, Color.WHITE)
        self.state = GameState.PAUSED
    
    def draw_hud(self):
        self.ui.clear()
        
        # Player Info
        self.ui.draw_text(-SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 - 40, f"Level: {self.player.level}", 12, Color.CYAN)
        self.ui.draw_text(-SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 - 80, f"Gold: {self.player.gold}", 12, Color.YELLOW)
        self.ui.draw_text(-SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 - 120, f"EXP: {self.player.exp}/{self.player.exp_to_level}", 12, Color.GREEN)
        
        # HP Bar
        self.ui.draw_text(-SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 - 160, "HP:", 12, Color.WHITE)
        self.ui.draw_hp_bar(-SCREEN_WIDTH/2 + 80, SCREEN_HEIGHT/2 - 155, self.player.hp, self.player.max_hp)
        
        # Battle Info
        if self.state == GameState.BATTLE and self.current_enemy:
            self.ui.draw_text(SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 - 40, f"Battle: {self.current_enemy.name}", 14, Color.RED)
            self.ui.draw_text(SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 - 80, f"Enemy HP: {self.current_enemy.hp}/{self.current_enemy.max_hp}", 12, Color.WHITE)
            self.ui.draw_text(SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 - 120, "Press SPACE to Attack", 12, Color.YELLOW)
    
    def update(self):
        if self.state == GameState.PLAYING:
            for enemy in self.enemies:
                enemy.move()
        
        self.draw_hud()
        self.screen.update()
    
    def run(self):
        while True:
            self.update()
            self.screen.update()

# ===== MAIN =====
if __name__ == "__main__":
    game = Game()
    game.run()
