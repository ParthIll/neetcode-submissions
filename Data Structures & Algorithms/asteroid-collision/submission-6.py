class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def sign(x):
            return (x > 0) - (x < 0)
        asts=[]
        for ast in asteroids:
            if not asts:
                asts.append(ast)
                continue
            if sign(ast)==sign(asts[-1])or sign(ast)==1:
                asts.append(ast)
            else:
                while(abs(ast)>=abs(asts[-1]) and sign(ast)!=sign(asts[-1])):
                    if abs(asts[-1])==abs(ast):
                        asts.pop()
                        break
                    else:
                        asts.pop()
                        if not asts or sign(ast)==sign(asts[-1]):
                            asts.append(ast)
                            break
                
                    
        return asts
       