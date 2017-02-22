import itertools
import copy

class breath_node:
    strings = []
    depth = 1
    children = []
    solution = ""

    def __init__(self):
        self.data = []

    def __init__(self,strings,depth):
        self.strings = strings
        self.depth = depth

    def create_children(self):
        nodes = []
        for x in range(0, len(self.strings)):
            # print("Running"+str(self.strings[x]))
            if len(self.strings[x]) > 0:
                move = self.strings[x][-1:]
                print("Move:"+str(move)+" at depth:"+str(self.depth+1))
                for y in range(0, len(self.strings)):
                    if self.depth >= m_depth:
                        break
                    if x != y:
                        strings_copy = copy.copy(self.strings)
                        strings_copy[y] = strings_copy[y]+move
                        strings_copy[x] = strings_copy[x][:-1]
                        print("Child node:" + str(strings_copy))

                        if strings_copy == strings_goal:
                            print(strings_copy)
                            print("Solution at d:"+str(self.depth+1))
                            return True

                        node_aux = breath_node(strings_copy, self.depth+1)
                        nodes.append(node_aux)

                        '''aux = ([z+move for z in self.strings if z != move])
                        print("Aux:"+str(aux))
                        strings_copy = copy.copy(self.strings)
                        print("Copy:"+str(strings_copy))
                        strings_copy[x] = strings_copy[x][:-1]

                        for i in aux:
                            strings_copy[y] = i
                            if strings_copy == strings_goal:
                                print("Solution")
                                return
                            print("Child node:"+str(strings_copy))
                            #node_aux = breath_node(strings_copy,self.depth+1)
                            #nodes.append(node_aux)'''
        if len(nodes) != 0:
            for x in nodes:
                # print(x.strings)
                if x.create_children():
                    return True
        else:
            # print("No solution found")
            return False


#Defining the default method for execution
if __name__ == "__main__":
    stringsin = []
    m_depth = int(input())
    received = input()
    goal = input()

    strings_goal = []

    print("Input received")
    while True:
        aux = received[:received.find(";")]
        aux = aux.replace("(", "")
        aux = aux.replace(")", "")
        aux = aux.replace(",", "")
        aux = aux.replace(" ", "")
        received = received[received.find(";")+1:]
        stringsin.append(list(aux))
        if received.find(";") < 0:
            aux = received
            aux = aux.replace("(", "")
            aux = aux.replace(")", "")
            aux = aux.replace(",", "")
            aux = aux.replace(" ", "")
            stringsin.append(list(aux))
            break

    while True:
        aux = goal[:goal.find(";")]
        aux = aux.replace("(", "")
        aux = aux.replace(")", "")
        aux = aux.replace(",", "")
        aux = aux.replace(" ", "")
        goal = goal[goal.find(";")+1:]
        strings_goal.append(list(aux))
        if goal.find(";") < 0:
            aux = goal
            aux = aux.replace("(", "")
            aux = aux.replace(")", "")
            aux = aux.replace(",", "")
            aux = aux.replace(" ", "")
            strings_goal.append(list(aux))
            break

    #print("Input:"+str(stringsin))
    #print("Goal:"+str(strings_goal))

    breath_tree  = breath_node(stringsin,1)

    breath_tree.create_children()
