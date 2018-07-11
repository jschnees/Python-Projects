class DrakeEquation():

    def Title(self):
        print("""
                        The Drake Equation\n
                Enter criteria below and get a result!
                
                  N = R * fp * ne * fl * fi * fc * L
                  
    Example: R = 10 fp = 0.5 ne = 2.0 fl = 1.0 fi = 0.01fc = 0.01 L = 10000
        """)
        
    def Data(self):
        
        R = int(input("The rate of formation of stars suitable for the development of intelligent life. "))
        fp = float(input("The fraction of those stars with planetary systems. "))
        ne = float(input("The number of planets, per solar system, with an environment suitable for life. "))
        fl = float(input("The fraction of suitable planets on which life actually appears. "))
        fi = float(input("The fraction of life bearing planets on which intelligent life emerges. "))
        fc = float(input("The fraction of civilizations that develop a technology that releases detectable signs of their existence into space. "))
        L = float(input("The length of time such civilizations release detectable signals into space. "))


        N = R * fp * ne * fl * fi * fc * L

        print("The number of civilizations in the Milky Way galaxy whose electromagnetic emissions are detectable. ", N)
                
aliens = DrakeEquation()
aliens.Title()
aliens.Data()
