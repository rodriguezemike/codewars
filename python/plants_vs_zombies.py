# https://www.codewars.com/kata/5a5db0f580eba84589000979/train/python

from enum import Enum
class GameState(Enum):
    Init = 0
    Plants = 1
    Zombies = 2
    EndTurn = 3
    GoalPlants = 4
    GoalZombies = 5

class GameManager(object):
    def __init__(self, board, zombies):
        self.turn = 0
        self.gameState = GameState.Init
        self.length = len(board[0])
        self.width = len(board)
        self.board_input = board
        self.zombie_inputs = zombies
        self._board = None
        self._plants = None
        self._zombies = None
    
    def __str__(self):
        message = "PVZ TURN %s\n" % self.turn
        for row in self.board:
            message += str([str(ele) for ele in row]) + "\n"
        message += "\n"
        return message
        
    def init_board_and_plants(self):
        board = []
        plants = []
        for y, row in enumerate(self.board_input):
            row = []
            for x, cell in enumerate(self.board_input[y]):
                if cell.isalpha() or cell.isdigit():
                    plant = Plant(cell, y, x)
                    row.append(plant)
                    plants.append(plant)
                else:
                    row.append(None)
            board.append(row)
        self._plants = plants
        self._board = board       
    
    def init_zombies(self):
        zombies = []
        for zombie_input in self.zombie_inputs:
            zombies.append(Zombie(zombie_input, self.length))
        return zombies
    
    def zombies_turn(self):
        for zombie in sorted(filter(lambda z: z.alive == True, self.zombies), key=lambda z:z.pos[1]):
            entity = self.board[zombie.pos[0]][zombie.pos[1]-1]
            if isinstance(entity, Plant):
                zombie.attack(entity)
            self.board[zombie.pos[0]][zombie.pos[1]-1] = zombie
            self.board[zombie.pos[0]][zombie.pos[1]] = None
            zombie.pos[1] -= 1
        for zombie in sorted(filter(lambda z: z.alive == False and z.move_number == self.turn, self.zombies),key=lambda z:z.pos[0]):
            self.board[zombie.pos[0]][zombie.pos[1]] = zombie
            zombie.alive = True
            zombie.spawned = True
        
    def plants_turn(self):
        for plant in filter(lambda p:p.alive == True and p.type != "S", self.plants):
            for _ in range(plant.shots):
                for zombie in sorted(filter(lambda z:z.alive == True and z.pos[0] == plant.pos[0], self.zombies), key=lambda z:z.pos[1]):
                    self.attack_zombie(plant, zombie)
                    break
        for plant in sorted(filter(lambda p:p.alive == True and p.type == "S", self.plants), key=lambda p:(p.pos[0], p.pos[1])):
            #Upper
            for zombie in filter(lambda z:z.alive == True and z.pos in self.get_s_range(plant, upper=True), self.zombies):
                self.attack_zombie(plant, zombie)
                break
            #Middle
            for zombie in sorted(filter(lambda z:z.alive == True and z.pos[0] == plant.pos[0], self.zombies), key=lambda z:z.pos[1]):
                self.attack_zombie(plant, zombie)
                break
            #Lower
            for zombie in filter(lambda z:z.alive == True and z.pos in self.get_s_range(plant, upper=False), self.zombies):
                self.attack_zombie(plant, zombie)
                break
    
    def attack_zombie(self, plant, zombie):
        plant.attack(zombie)
        if zombie.alive == False:
            self.board[zombie.pos[0]][zombie.pos[1]] = None
                    
    def get_s_range(self, plant, upper = False):
        s_range = []
        if upper:
            for i in range(1,self.length):
                s_range.append([plant.pos[0]-i, plant.pos[1]+i])
        else:
            for i in range(1,self.length):
                s_range.append([plant.pos[0]+i, plant.pos[1]+i])
        return s_range
                
    def run_game(self):
        while True:
            if self.gameState == GameState.Zombies:
                self.zombies_turn()
                self.gameState = GameState.Plants
            elif self.gameState == GameState.Plants:
                self.plants_turn()
                self.gameState = GameState.EndTurn
            elif self.gameState == GameState.EndTurn:
                if all([zombie.alive == False and zombie.spawned == True for zombie in self.zombies]):
                    self.gameState = GameState.GoalPlants
                    return None
                elif any([zombie.pos[1] <= 0 for zombie in self.zombies]):
                    self.gameState = GameState.GoalZombies
                    return self.turn + 1
                else:
                    self.turn += 1
                    self.gameState = GameState.Zombies
            else:
                self.init_board_and_plants()
                self.gameState = GameState.Zombies
            
    def get_plants(self):
        if not self._plants:
            self.init_board_and_plants()
        return self._plants
    
    def get_zombies(self):
        if not self._zombies:
            self._zombies = self.init_zombies()
        return self._zombies
    
    def get_board(self):
        if not self._board:
            self.init_board_and_plants()
        return self._board
    
    plants = property(get_plants)
    zombies = property(get_zombies)
    board = property(get_board)


class Plant(object):
        def __init__(self, type, row, column):
            self.type = type
            self.pos = [row, column]
            self.hp = 1
            self.damage = 1 
            self.shots = 1 if self.type == "S" else int(self.type) 
            self.alive = True
            
        def __str__(self):            
            return "P__%s" % self.type
            
        def attack(self, target):
            target.hp -= self.damage
            if target.hp <= 0:
                target.alive = False
            
class Zombie(object):
        def __init__(self, input_list, length):
            self.move_number = input_list[0]
            self.row = input_list[1]
            self.pos = [self.row, length-1]
            self.hp = input_list[2]
            self.damage = 1
            self.alive = False
            self.spawned = False
        
        def __str__(self):
            return "Z_%s" % self.hp
            
        def attack(self, target):
            target.hp -= self.damage
            if target.hp <= 0:
                target.alive = False
            
def plants_and_zombies(lawn, zombies):
    #your code goes here. you can do it!
    manager = GameManager(lawn, zombies)
    return manager.run_game()
