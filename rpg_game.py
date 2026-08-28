import random
import json
from datetime import datetime

# ===== GAME CONFIG =====
GAME_TITLE = "⚔️  DUNIA YUFZ - EPIC RPG ADVENTURE ⚔️"
GAME_STORY = "Anda adalah seorang pejuang muda yang memasuki dunia Yufz yang penuh dengan monster dan harta karun..."

# ===== PLAYER BASE STATS =====
PLAYER_MAX_HP = 100
PLAYER_ATTACK = 10
PLAYER_DEFENSE = 5
PLAYER_MAX_MANA = 50
PLAYER_STARTING_GOLD = 200

# ===== WEAPON SYSTEM (BERBAGAI KELAS) =====
WEAPONS = {
    # Kelas: Common (Umum)
    "Wooden Sword": {
        "class": "Common",
        "attack": 5,
        "mana_bonus": 0,
        "description": "Pedang kayu sederhana",
        "rarity": "⚪ Common",
        "cost": 30,
        "icon": "🔶"
    },
    "Iron Sword": {
        "class": "Common",
        "attack": 12,
        "mana_bonus": 0,
        "description": "Pedang besi berkualitas",
        "rarity": "⚪ Common",
        "cost": 80,
        "icon": "🔶"
    },
    
    # Kelas: Uncommon (Jarang)
    "Steel Blade": {
        "class": "Uncommon",
        "attack": 18,
        "mana_bonus": 0,
        "description": "Pedang baja yang tajam",
        "rarity": "🟢 Uncommon",
        "cost": 150,
        "icon": "🔷"
    },
    "Mage Staff": {
        "class": "Uncommon",
        "attack": 8,
        "mana_bonus": 30,
        "description": "Tongkat sihir untuk mage",
        "rarity": "🟢 Uncommon",
        "cost": 140,
        "icon": "🔷"
    },
    
    # Kelas: Rare (Langka)
    "Dragon Slayer": {
        "class": "Rare",
        "attack": 28,
        "mana_bonus": 0,
        "description": "Pedang legendaris pembunuh naga",
        "rarity": "🔵 Rare",
        "cost": 500,
        "icon": "🔶"
    },
    "Mystic Wand": {
        "class": "Rare",
        "attack": 15,
        "mana_bonus": 50,
        "description": "Tongkat mistis dengan kekuatan sihir",
        "rarity": "🔵 Rare",
        "cost": 480,
        "icon": "🔷"
    },
    "Frost Blade": {
        "class": "Rare",
        "attack": 24,
        "mana_bonus": 15,
        "description": "Pedang yang diselimuti es",
        "rarity": "🔵 Rare",
        "cost": 450,
        "icon": "❄️"
    },
    
    # Kelas: Epic (Epik)
    "Excalibur": {
        "class": "Epic",
        "attack": 40,
        "mana_bonus": 0,
        "description": "Pedang legendaris Excalibur",
        "rarity": "🟣 Epic",
        "cost": 1000,
        "icon": "👑"
    },
    "Inferno Sword": {
        "class": "Epic",
        "attack": 35,
        "mana_bonus": 20,
        "description": "Pedang yang membakar dengan api neraka",
        "rarity": "🟣 Epic",
        "cost": 950,
        "icon": "🔥"
    },
    
    # Kelas: Legendary (Legendaris)
    "Godslayer": {
        "class": "Legendary",
        "attack": 60,
        "mana_bonus": 30,
        "description": "Pedang pembunuh dewa - kekuatan tertinggi",
        "rarity": "🌟 Legendary",
        "cost": 2500,
        "icon": "⚡"
    }
}

# ===== ARMOR SYSTEM =====
ARMORS = {
    # Common Armor
    "Cloth Armor": {
        "class": "Common",
        "defense": 3,
        "hp_bonus": 10,
        "rarity": "⚪ Common",
        "cost": 25,
        "icon": "👕"
    },
    "Leather Armor": {
        "class": "Common",
        "defense": 7,
        "hp_bonus": 20,
        "rarity": "⚪ Common",
        "cost": 70,
        "icon": "👔"
    },
    
    # Uncommon Armor
    "Chain Mail": {
        "class": "Uncommon",
        "defense": 12,
        "hp_bonus": 35,
        "rarity": "🟢 Uncommon",
        "cost": 130,
        "icon": "⛓️"
    },
    "Dragon Scale Armor": {
        "class": "Uncommon",
        "defense": 15,
        "hp_bonus": 50,
        "rarity": "🟢 Uncommon",
        "cost": 200,
        "icon": "🐉"
    },
    
    # Rare Armor
    "Plate Armor": {
        "class": "Rare",
        "defense": 20,
        "hp_bonus": 70,
        "rarity": "🔵 Rare",
        "cost": 400,
        "icon": "🛡️"
    },
    "Crystal Armor": {
        "class": "Rare",
        "defense": 18,
        "hp_bonus": 80,
        "rarity": "🔵 Rare",
        "cost": 420,
        "icon": "💎"
    },
    
    # Epic Armor
    "Obsidian Plate": {
        "class": "Epic",
        "defense": 30,
        "hp_bonus": 120,
        "rarity": "🟣 Epic",
        "cost": 800,
        "icon": "⬛"
    },
    
    # Legendary Armor
    "Divine Plate": {
        "class": "Legendary",
        "defense": 50,
        "hp_bonus": 200,
        "rarity": "🌟 Legendary",
        "cost": 2000,
        "icon": "✨"
    }
}

# ===== SKILL SYSTEM =====
SKILLS = {
    "Power Strike": {
        "mana_cost": 10,
        "damage": 25,
        "description": "Serangan kuat dengan pedang",
        "type": "attack"
    },
    "Fireball": {
        "mana_cost": 20,
        "damage": 40,
        "description": "Ledakkan api ke musuh",
        "type": "attack"
    },
    "Heal": {
        "mana_cost": 15,
        "heal": 60,
        "description": "Penyembuhan diri sendiri",
        "type": "heal"
    },
    "Ice Storm": {
        "mana_cost": 25,
        "damage": 50,
        "description": "Badai es yang dahsyat",
        "type": "attack"
    },
    "Lightning Strike": {
        "mana_cost": 18,
        "damage": 45,
        "description": "Petir menyambar ke musuh",
        "type": "attack"
    },
    "Shield Barrier": {
        "mana_cost": 20,
        "defense_boost": 15,
        "duration": 3,
        "description": "Penghalang pertahanan",
        "type": "defense"
    },
    "Meteors": {
        "mana_cost": 35,
        "damage": 70,
        "description": "Hujan meteor dari langit",
        "type": "attack"
    },
    "Holy Light": {
        "mana_cost": 25,
        "heal": 100,
        "description": "Cahaya suci untuk penyembuhan besar",
        "type": "heal"
    },
    "Berserk": {
        "mana_cost": 15,
        "attack_boost": 20,
        "duration": 2,
        "description": "Masuki mode berserk untuk attack lebih besar",
        "type": "buff"
    }
}

# ===== REGULAR ENEMIES (MOB) =====
ENEMIES = {
    "Goblin": {
        "hp": 30,
        "attack": 5,
        "defense": 1,
        "reward_exp": 50,
        "reward_gold": 25,
        "rarity": "⚪",
        "level": 1
    },
    "Wolf": {
        "hp": 40,
        "attack": 8,
        "defense": 2,
        "reward_exp": 75,
        "reward_gold": 40,
        "rarity": "⚪",
        "level": 2
    },
    "Skeleton": {
        "hp": 45,
        "attack": 9,
        "defense": 3,
        "reward_exp": 100,
        "reward_gold": 50,
        "rarity": "🟢",
        "level": 3
    },
    "Orc": {
        "hp": 60,
        "attack": 12,
        "defense": 5,
        "reward_exp": 120,
        "reward_gold": 70,
        "rarity": "🟢",
        "level": 4
    },
    "Dark Knight": {
        "hp": 80,
        "attack": 15,
        "defense": 7,
        "reward_exp": 150,
        "reward_gold": 100,
        "rarity": "🔵",
        "level": 5
    },
    "Mage": {
        "hp": 50,
        "attack": 18,
        "defense": 4,
        "reward_exp": 130,
        "reward_gold": 90,
        "rarity": "🔵",
        "level": 5
    },
    "Troll": {
        "hp": 100,
        "attack": 14,
        "defense": 8,
        "reward_exp": 180,
        "reward_gold": 120,
        "rarity": "🔵",
        "level": 6
    },
    "Vampire": {
        "hp": 70,
        "attack": 16,
        "defense": 6,
        "reward_exp": 160,
        "reward_gold": 110,
        "rarity": "🔵",
        "level": 6
    },
    "Shadow Beast": {
        "hp": 90,
        "attack": 18,
        "defense": 7,
        "reward_exp": 200,
        "reward_gold": 150,
        "rarity": "🟣",
        "level": 7
    }
}

# ===== BOSS ENEMIES =====
BOSSES = {
    "Dungeon Guardian": {
        "hp": 200,
        "attack": 20,
        "defense": 10,
        "reward_exp": 500,
        "reward_gold": 300,
        "rarity": "🔵 BOSS",
        "level": 10,
        "drops": ["Dragon Slayer", "Plate Armor"],
        "description": "Penjaga dungeon dengan kekuatan besar"
    },
    "Shadow King": {
        "hp": 300,
        "attack": 25,
        "defense": 12,
        "reward_exp": 800,
        "reward_gold": 500,
        "rarity": "🟣 BOSS",
        "level": 15,
        "drops": ["Obsidian Plate", "Mystic Wand"],
        "description": "Raja kegelapan yang mendominasi nether realm"
    },
    "Fire Dragon": {
        "hp": 350,
        "attack": 28,
        "defense": 14,
        "reward_exp": 1000,
        "reward_gold": 700,
        "rarity": "🟣 BOSS",
        "level": 18,
        "drops": ["Inferno Sword", "Dragon Scale Armor"],
        "description": "Naga api yang membakar segalanya"
    },
    "Ice Sorcerer": {
        "hp": 250,
        "attack": 30,
        "defense": 10,
        "reward_exp": 900,
        "reward_gold": 600,
        "rarity": "🟣 BOSS",
        "level": 16,
        "drops": ["Frost Blade", "Crystal Armor"],
        "description": "Penyihir es dengan kontrol penuh atas frost"
    },
    "Demon Lord": {
        "hp": 400,
        "attack": 35,
        "defense": 15,
        "reward_exp": 1500,
        "reward_gold": 1000,
        "rarity": "🌟 LEGENDARY BOSS",
        "level": 20,
        "drops": ["Godslayer", "Divine Plate"],
        "description": "Tuhan iblis tertua dari dimensi gelap"
    }
}

# ===== ITEMS/CONSUMABLES =====
ITEMS = {
    "Health Potion": {
        "cost": 20,
        "type": "consumable",
        "heal": 50,
        "description": "Menyembuhkan 50 HP"
    },
    "Mana Potion": {
        "cost": 30,
        "type": "consumable",
        "mana_restore": 40,
        "description": "Mengembalikan 40 Mana"
    },
    "Super Potion": {
        "cost": 80,
        "type": "consumable",
        "heal": 150,
        "description": "Menyembuhkan 150 HP"
    },
    "Mega Mana": {
        "cost": 100,
        "type": "consumable",
        "mana_restore": 100,
        "description": "Mengembalikan 100 Mana"
    },
    "Antidote": {
        "cost": 15,
        "type": "consumable",
        "effect": "cure_poison",
        "description": "Menyembuhkan keracunan"
    },
    "Revival Scroll": {
        "cost": 300,
        "type": "consumable",
        "effect": "revive",
        "description": "Menghidupkan kembali saat mati (1x per dungeons)"
    }
}

# ===== CRAFTING RECIPES =====
CRAFTING_RECIPES = {
    "Strong Potion": {
        "ingredients": {"Health Potion": 3, "Mana Potion": 1},
        "result": "Super Potion",
        "level_required": 5,
        "description": "Membuat potion super dari 3 health potion dan 1 mana potion"
    },
    "Enhanced Blade": {
        "ingredients": {"Iron Sword": 1, "Steel Blade": 1},
        "result": "Dragon Slayer",
        "level_required": 10,
        "description": "Upgrade pedang ke Dragon Slayer"
    },
    "Reinforced Armor": {
        "ingredients": {"Leather Armor": 1, "Chain Mail": 1},
        "result": "Plate Armor",
        "level_required": 8,
        "description": "Upgrade armor ke Plate Armor"
    }
}

# ===== HOUSE/HOUSING SYSTEM =====
HOUSE_TYPES = {
    "Small Cottage": {
        "cost": 500,
        "capacity": 5,
        "description": "Rumah kecil yang nyaman",
        "storage_bonus": 10,
        "regen_bonus": 1.1
    },
    "Medium House": {
        "cost": 1500,
        "capacity": 15,
        "description": "Rumah medium dengan ruang lebih",
        "storage_bonus": 20,
        "regen_bonus": 1.2
    },
    "Mansion": {
        "cost": 5000,
        "capacity": 50,
        "description": "Mansion mewah dengan semua fasilitas",
        "storage_bonus": 50,
        "regen_bonus": 1.5
    }
}

# ===== PLAYER CLASS =====
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = PLAYER_MAX_HP
        self.max_hp = PLAYER_MAX_HP
        self.mana = PLAYER_MAX_MANA
        self.max_mana = PLAYER_MAX_MANA
        self.attack = PLAYER_ATTACK
        self.defense = PLAYER_DEFENSE
        self.level = 1
        self.exp = 0
        self.exp_to_level = 200
        self.gold = PLAYER_STARTING_GOLD
        self.inventory = {}
        self.equipment = {
            "weapon": None,
            "armor": None
        }
        self.house = None
        self.playtime = 0
        self.dungeons_cleared = 0
        self.boss_kills = 0
        
    def show_stats(self):
        weapon_info = f"({WEAPONS[self.equipment['weapon']]['rarity']})" if self.equipment['weapon'] else "None"
        armor_info = f"({ARMORS[self.equipment['armor']]['rarity']})" if self.equipment['armor'] else "None"
        house_info = self.house if self.house else "None"
        
        print("\n" + "="*60)
        print(f"📊 {self.name.upper()} - Level {self.level}")
        print("="*60)
        print(f"❤️  HP: {self.hp}/{self.max_hp}")
        print(f"💙 Mana: {self.mana}/{self.max_mana}")
        print(f"⚔️  Attack: {self.attack} | 🛡️  Defense: {self.defense}")
        print(f"⭐ XP: {self.exp}/{self.exp_to_level}")
        print(f"💰 Gold: {self.gold}")
        print(f"🗡️  Weapon: {self.equipment['weapon']} {weapon_info}")
        print(f"👕 Armor: {self.equipment['armor']} {armor_info}")
        print(f"🏠 House: {house_info}")
        print(f"📍 Dungeons Cleared: {self.dungeons_cleared}")
        print(f"👑 Boss Kills: {self.boss_kills}")
        print("="*60 + "\n")
        
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        return actual_damage
        
    def heal(self, amount):
        old_hp = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        healed = self.hp - old_hp
        return healed
        
    def restore_mana(self, amount):
        old_mana = self.mana
        self.mana = min(self.mana + amount, self.max_mana)
        restored = self.mana - old_mana
        return restored
        
    def gain_exp(self, amount):
        self.exp += amount
        print(f"✨ Dapat {amount} XP!")
        if self.exp >= self.exp_to_level:
            self.level_up()
            
    def level_up(self):
        self.level += 1
        self.exp = 0
        self.exp_to_level = int(self.exp_to_level * 1.15)
        self.max_hp += 20
        self.hp = self.max_hp
        self.max_mana += 10
        self.mana = self.max_mana
        self.attack += 5
        self.defense += 2
        print(f"\n🎉 LEVEL UP! Sekarang level {self.level}!")
        print(f"   HP: +20 | Mana: +10 | Attack: +5 | Defense: +2\n")
        
    def add_gold(self, amount):
        self.gold += amount
        
    def add_item(self, item_name, quantity=1):
        if item_name not in self.inventory:
            self.inventory[item_name] = 0
        self.inventory[item_name] += quantity
        
    def remove_item(self, item_name, quantity=1):
        if item_name in self.inventory:
            self.inventory[item_name] -= quantity
            if self.inventory[item_name] <= 0:
                del self.inventory[item_name]
                
    def equip_weapon(self, weapon_name):
        if weapon_name in WEAPONS:
            self.equipment['weapon'] = weapon_name
            weapon = WEAPONS[weapon_name]
            self.attack = PLAYER_ATTACK + weapon['attack']
            self.max_mana = PLAYER_MAX_MANA + weapon['mana_bonus']
            print(f"⚔️  Dilengkapi {weapon_name}!")
            return True
        return False
        
    def equip_armor(self, armor_name):
        if armor_name in ARMORS:
            self.equipment['armor'] = armor_name
            armor = ARMORS[armor_name]
            self.defense = PLAYER_DEFENSE + armor['defense']
            self.max_hp = PLAYER_MAX_HP + armor['hp_bonus']
            print(f"👕 Dilengkapi {armor_name}!")
            return True
        return False
        
    def buy_house(self, house_type):
        if house_type in HOUSE_TYPES:
            house = HOUSE_TYPES[house_type]
            if self.gold >= house['cost']:
                self.gold -= house['cost']
                self.house = house_type
                print(f"🏠 Anda membeli {house_type}!")
                return True
            else:
                print(f"❌ Gold tidak cukup! Butuh {house['cost']} gold")
                return False
        return False

# ===== ENEMY CLASS =====
class Enemy:
    def __init__(self, name):
        if name in ENEMIES:
            enemy_data = ENEMIES[name]
        else:
            enemy_data = BOSSES[name]
            
        self.name = name
        self.hp = enemy_data["hp"]
        self.max_hp = self.hp
        self.attack = enemy_data["attack"]
        self.defense = enemy_data["defense"]
        self.reward_exp = enemy_data["reward_exp"]
        self.reward_gold = enemy_data["reward_gold"]
        self.rarity = enemy_data["rarity"]
        self.level = enemy_data["level"]
        self.is_boss = name in BOSSES
        
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        return actual_damage
        
    def is_alive(self):
        return self.hp > 0

# ===== BATTLE SYSTEM =====
def battle(player, enemy):
    print(f"\n{'='*60}")
    print(f"⚔️  PERTARUNGAN DIMULAI!")
    print(f"{'='*60}")
    print(f"Anda vs {enemy.name} {enemy.rarity}")
    print(f"Level: {enemy.level} | HP: {enemy.hp} | Attack: {enemy.attack}\n")
    
    turn = 0
    battle_log = []
    
    while player.hp > 0 and enemy.hp > 0:
        turn += 1
        print(f"--- TURN {turn} ---")
        print(f"HP Anda: {player.hp}/{player.max_hp} | HP {enemy.name}: {enemy.hp}/{enemy.max_hp}\n")
        
        print("1. Attack")
        print("2. Use Skill")
        print("3. Use Item")
        print("4. Run Away")
        choice = input("Pilihan: ").strip()
        
        if choice == "1":
            damage = player.attack + random.randint(-5, 10)
            enemy.take_damage(damage)
            print(f"⚔️  Anda serang {enemy.name}! Damage: {damage}")
            print(f"   HP {enemy.name}: {max(0, enemy.hp)}\n")
            
        elif choice == "2":
            print("\nSkill yang tersedia:")
            skill_list = list(SKILLS.keys())
            for i, skill in enumerate(skill_list, 1):
                skill_info = SKILLS[skill]
                print(f"{i}. {skill} (Mana: {skill_info['mana_cost']}) - {skill_info['description']}")
            
            try:
                skill_choice = int(input("Pilih skill (nomor): ")) - 1
                if 0 <= skill_choice < len(skill_list):
                    skill_name = skill_list[skill_choice]
                    skill = SKILLS[skill_name]
                    
                    if player.mana >= skill["mana_cost"]:
                        player.mana -= skill["mana_cost"]
                        
                        if "damage" in skill:
                            damage = skill["damage"] + random.randint(-5, 10)
                            enemy.take_damage(damage)
                            print(f"\n✨ Anda gunakan {skill_name}! Damage: {damage}")
                            print(f"   Mana tersisa: {player.mana}")
                            print(f"   HP {enemy.name}: {max(0, enemy.hp)}\n")
                        elif "heal" in skill:
                            healed = player.heal(skill["heal"])
                            print(f"\n✨ Anda gunakan {skill_name}! Heal: {healed}")
                            print(f"   HP Anda: {player.hp}/{player.max_hp}\n")
                    else:
                        print("❌ Mana tidak cukup!\n")
                        continue
            except:
                print("❌ Input tidak valid!\n")
                continue
                
        elif choice == "3":
            if player.inventory:
                print("\nInventory Anda:")
                item_list = [item for item in player.inventory.keys() if item in ITEMS]
                for i, item in enumerate(item_list, 1):
                    print(f"{i}. {item} (x{player.inventory[item]}) - {ITEMS[item]['description']}")
                
                try:
                    item_choice = int(input("Pilih item (nomor): ")) - 1
                    if 0 <= item_choice < len(item_list):
                        item_name = item_list[item_choice]
                        item = ITEMS[item_name]
                        
                        if "heal" in item:
                            healed = player.heal(item["heal"])
                            print(f"\n🧪 Anda gunakan {item_name}! Heal: {healed}")
                            print(f"   HP Anda: {player.hp}/{player.max_hp}\n")
                        elif "mana_restore" in item:
                            restored = player.restore_mana(item["mana_restore"])
                            print(f"\n🧪 Anda gunakan {item_name}! Mana: +{restored}")
                            print(f"   Mana Anda: {player.mana}/{player.max_mana}\n")
                        
                        player.remove_item(item_name, 1)
                except:
                    print("❌ Input tidak valid!\n")
                    continue
            else:
                print("❌ Inventaris kosong!\n")
                continue
                
        elif choice == "4":
            if random.random() > 0.4:
                print("✅ Berhasil kabur!\n")
                return "run"
            else:
                print("❌ Gagal kabur! Terpaksa melanjutkan pertarungan\n")
        else:
            print("❌ Pilihan tidak valid!\n")
            continue
        
        # ENEMY ATTACK
        if enemy.is_alive():
            enemy_damage = enemy.attack + random.randint(-3, 5)
            actual_damage = player.take_damage(enemy_damage)
            print(f"👹 {enemy.name} menyerang Anda! Damage: {actual_damage}")
            print(f"   HP Anda: {player.hp}/{player.max_hp}\n")
    
    # Battle result
    if player.hp <= 0:
        print(f"\n💀 Anda KALAH! Game Over...")
        return "lose"
    else:
        print(f"\n🎉 Anda MENANG!")
        player.gain_exp(enemy.reward_exp)
        player.add_gold(enemy.reward_gold)
        print(f"💰 Dapat {enemy.reward_gold} gold!")
        
        # Boss drops
        if enemy.is_boss and "drops" in BOSSES[enemy.name]:
            drops = BOSSES[enemy.name]["drops"]
            print(f"✨ Boss drops: {', '.join(drops)}")
            for drop in drops:
                player.add_item(drop)
            player.boss_kills += 1
        
        player.dungeons_cleared += 1
        return "win"

# ===== SHOP SYSTEM =====
def shop(player):
    while True:
        print("\n" + "="*60)
        print("🏪 TOKO PENYEMBUHAN")
        print("="*60)
        print(f"💰 Gold Anda: {player.gold}\n")
        
        print("=== POTIONS ===")
        for i, (item_name, item) in enumerate(ITEMS.items(), 1):
            print(f"{i}. {item_name} - {item['cost']} gold ({item['description']})")
        
        print("\n=== WEAPONS ===")
        for i, (weapon_name, weapon) in enumerate(WEAPONS.items(), i+1):
            print(f"{i}. {weapon_name} {weapon['rarity']} - {weapon['cost']} gold (Attack: +{weapon['attack']})")
        
        print("\n=== ARMOR ===")
        for i, (armor_name, armor) in enumerate(ARMORS.items(), i+1):
            print(f"{i}. {armor_name} {armor['rarity']} - {armor['cost']} gold (Defense: +{armor['defense']})")
        
        print("\n0. Keluar")
        choice = input("Pilih item (nomor): ").strip()
        
        if choice == "0":
            return
        
        try:
            choice_idx = int(choice) - 1
            all_items = list(ITEMS.items()) + list(WEAPONS.items()) + list(ARMORS.items())
            
            if 0 <= choice_idx < len(all_items):
                item_name, item = all_items[choice_idx]
                cost = item.get('cost', 0)
                
                if player.gold >= cost:
                    player.gold -= cost
                    
                    if item_name in WEAPONS:
                        player.equip_weapon(item_name)
                        player.add_item(item_name)
                    elif item_name in ARMORS:
                        player.equip_armor(item_name)
                        player.add_item(item_name)
                    else:
                        player.add_item(item_name)
                        print(f"✅ Berhasil membeli {item_name}!")
                else:
                    print(f"❌ Gold tidak cukup! Butuh {cost - player.gold} gold lagi")
        except:
            print("❌ Input tidak valid!")

# ===== CRAFTING SYSTEM =====
def crafting(player):
    while True:
        print("\n" + "="*60)
        print("⚒️  CRAFTING SYSTEM")
        print("="*60)
        print(f"Level Anda: {player.level}\n")
        
        for i, (recipe_name, recipe) in enumerate(CRAFTING_RECIPES.items(), 1):
            req_level = recipe.get('level_required', 1)
            can_craft = "✅" if player.level >= req_level else "❌"
            print(f"{i}. {recipe_name} {can_craft} (Level {req_level}+)")
            print(f"   Ingredients: {recipe['ingredients']}")
            print(f"   Result: {recipe['result']}")
            print(f"   {recipe['description']}\n")
        
        print("0. Keluar")
        choice = input("Pilih recipe (nomor): ").strip()
        
        if choice == "0":
            return
        
        try:
            choice_idx = int(choice) - 1
            recipe_list = list(CRAFTING_RECIPES.items())
            
            if 0 <= choice_idx < len(recipe_list):
                recipe_name, recipe = recipe_list[choice_idx]
                
                if player.level < recipe.get('level_required', 1):
                    print(f"❌ Level tidak cukup! Butuh level {recipe['level_required']}")
                    continue
                
                # Check ingredients
                has_all = True
                for ingredient, needed in recipe['ingredients'].items():
                    if player.inventory.get(ingredient, 0) < needed:
                        print(f"❌ Kurang {ingredient}! Punya: {player.inventory.get(ingredient, 0)}, Butuh: {needed}")
                        has_all = False
                
                if has_all:
                    for ingredient, needed in recipe['ingredients'].items():
                        player.remove_item(ingredient, needed)
                    player.add_item(recipe['result'])
                    print(f"\n✅ Craft sukses! Anda mendapat {recipe['result']}")
        except:
            print("❌ Input tidak valid!")

# ===== INVENTORY SYSTEM =====
def inventory(player):
    print("\n" + "="*60)
    print("📦 INVENTARIS")
    print("="*60)
    
    if not player.inventory:
        print("Inventaris kosong!")
        return
    
    print("\n=== WEAPONS ===")
    for item, count in player.inventory.items():
        if item in WEAPONS:
            weapon = WEAPONS[item]
            print(f"- {item} {weapon['rarity']} x{count} (Attack: +{weapon['attack']})")
    
    print("\n=== ARMOR ===")
    for item, count in player.inventory.items():
        if item in ARMORS:
            armor = ARMORS[item]
            print(f"- {item} {armor['rarity']} x{count} (Defense: +{armor['defense']})")
    
    print("\n=== ITEMS ===")
    for item, count in player.inventory.items():
        if item in ITEMS:
            print(f"- {item} x{count} ({ITEMS[item]['description']})")
    
    print("\n" + "="*60)

# ===== HOUSING SYSTEM =====
def housing(player):
    while True:
        print("\n" + "="*60)
        print("🏠 SISTEM RUMAH")
        print("="*60)
        print(f"Rumah saat ini: {player.house if player.house else 'Tidak punya'}")
        print(f"💰 Gold Anda: {player.gold}\n")
        
        for i, (house_type, house) in enumerate(HOUSE_TYPES.items(), 1):
            print(f"{i}. {house_type} - {house['cost']} gold")
            print(f"   {house['description']}")
            print(f"   Kapasitas: {house['capacity']} items")
            print(f"   Storage Bonus: +{house['storage_bonus']}")
            print(f"   HP Regen: x{house['regen_bonus']}\n")
        
        print("0. Keluar")
        choice = input("Pilih rumah (nomor): ").strip()
        
        if choice == "0":
            return
        
        try:
            choice_idx = int(choice) - 1
            house_list = list(HOUSE_TYPES.items())
            
            if 0 <= choice_idx < len(house_list):
                house_name, house = house_list[choice_idx]
                if player.buy_house(house_name):
                    pass
        except:
            print("❌ Input tidak valid!")

# ===== TRADING SYSTEM =====
def trading(player):
    print("\n" + "="*60)
    print("🔄 TRADING SYSTEM")
    print("="*60)
    print("⚠️  Fitur trading dengan NPC sedang dikembangkan!")
    print("Untuk sekarang, gunakan inventory untuk melihat item Anda\n")

# ===== MAIN MENU =====
def show_menu():
    print("\n" + "="*60)
    print(f"{GAME_TITLE}")
    print("="*60)
    print("1. Mulai Pertarungan")
    print("2. Lihat Stats")
    print("3. Ke Toko")
    print("4. Lihat Inventaris")
    print("5. Crafting")
    print("6. Rumah")
    print("7. Trading")
    print("8. Keluar Game")
    print("="*60)
    return input("Pilihan: ").strip()

# ===== MAIN GAME =====
def main():
    print(f"\n{GAME_TITLE}\n")
    player_name = input("Masukkan nama karakter Anda: ").strip()
    player = Player(player_name)
    
    print(f"\n{GAME_STORY}\n")
    print(f"Selamat datang di dunia Yufz, {player_name}!")
    print(f"Anda memulai dengan {player.gold} gold dan HP {player.max_hp}\n")
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            print("\n1. Pertarungan Normal (Vs Mob)")
            print("2. Boss Battle (Tantang Boss)")
            battle_choice = input("Pilihan: ").strip()
            
            if battle_choice == "1":
                enemy_name = random.choice(list(ENEMIES.keys()))
                enemy = Enemy(enemy_name)
                result = battle(player, enemy)
            elif battle_choice == "2":
                print("\nBoss yang tersedia:")
                boss_list = list(BOSSES.keys())
                for i, boss in enumerate(boss_list, 1):
                    boss_info = BOSSES[boss]
                    print(f"{i}. {boss} {boss_info['rarity']} (Level {boss_info['level']})")
                
                try:
                    boss_idx = int(input("Pilih boss (nomor): ")) - 1
                    if 0 <= boss_idx < len(boss_list):
                        boss_name = boss_list[boss_idx]
                        enemy = Enemy(boss_name)
                        result = battle(player, enemy)
                except:
                    print("❌ Input tidak valid!")
                    continue
            else:
                continue
            
            if result == "lose":
                print("\nGame Over! Terima kasih sudah bermain!")
                break
                
        elif choice == "2":
            player.show_stats()
            
        elif choice == "3":
            shop(player)
            
        elif choice == "4":
            inventory(player)
            
        elif choice == "5":
            crafting(player)
            
        elif choice == "6":
            housing(player)
            
        elif choice == "7":
            trading(player)
            
        elif choice == "8":
            print("\n👋 Terima kasih sudah bermain! Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()
