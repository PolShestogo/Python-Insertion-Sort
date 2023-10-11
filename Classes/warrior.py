class Hero:
        '''
        
        Класс герой обладает следующими свойствами
        координаты
        здоровье
        урон
        скорость передвижения
        броня
        рыгучесть
        '''

        __coord_x=0
        __coord_y=0
        __health=1000
        __damage=50
        __velocity=5
        __armoredcore6=20
        def __init__(self):
                pass
        def coord_x():
                return self.__coord_x
        def coord_y():
                return self.__coord_y
        def health():
                return self.__health
        def damage():
                return self.__damage
        def velocity():
                return self.__velocity
        def armor():
                return self.__armoredcore6
        def __str__(self):
                return f"Hero:  {self.coord_x},\n {self.coord_y}, \n {self.health},\n{ self.damage},\n  { self.velocity},\n { self.armor}"
        
        @property.setter
        def damage(self, new_damage):
                self.__damage=new_damage
        @property.deleter
        def armor(self):
                print("ASHALETTT")
                        
                        
                        
                       
                     
                       
                




