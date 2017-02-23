import time
import copy


class depth_node:
    strings = []
    depth = 1
    children = []
    solution = ""
    path = []

    def __init__(self, strings, depth, path):
        self.strings = strings
        self.depth = depth
        self.path = path

    def print_path(self, cost):
        return_path = ""
        for p in range(0, len(self.path), 2):
            i_pos = self.path[p]
            j_pos =self.path[p+1]
            return_path += "("+str(i_pos)+", "+str(j_pos)+"); "
            cost += 1 + abs(i_pos-j_pos)
        return [return_path, cost]

    def create_children(self):
        nodes = []
        for x in range(0, len(self.strings)):
            #print("Running"+str(self.strings[x]))
            if len(self.strings[x]) > 0:
                move = self.strings[x][-1:]
                #print("Move:" + str(move) + " at depth:" + str(self.depth))
                for y in range(0, len(self.strings)):
                    if len(self.strings[y]) + 1 > m_height or self.depth >= 4:
                        break
                    if x != y:
                        strings_copy = copy.copy(self.strings)
                        strings_copy[y] = self.strings[y] + move
                        strings_copy[x] = self.strings[x][:-1]
                        #print("Childnode:"+str(strings_copy))
                        valid = []
                        for z in range(0,len(strings_copy)):
                            if (strings_copy[z] == strings_goal[z]) and result[z]:
                                valid.append(True)
                            else:
                                valid.append(False)
                        if valid == result:
                            cost = 0
                            aux_path = self.print_path(cost)
                            cost += 1 + abs(x-y) + aux_path[1]
                            print(cost)
                            print(aux_path[0]+"(" + str(x) + ", " + str(y) + ")")
                            exit(0)
                        aux_path = copy.copy(self.path)
                        aux_path.append(x)
                        aux_path.append(y)
                        time.sleep(.2)
                        node_aux = depth_node(strings_copy, self.depth + 1, aux_path)
                        #print("Child Expand")
                        node_aux.create_children()
        return "False"

result = []
# Defining the default method for execution
if __name__ == "__main__":
    stringsin = []
    m_height = int(input())
    received = input()
    goal = input()

    strings_goal = []

    #print("Input received")
    while True:
        aux = received[:received.find(";")]
        aux = aux.replace("(", "")
        aux = aux.replace(")", "")
        aux = aux.replace(",", "")
        aux = aux.replace(" ", "")
        received = received[received.find(";") + 1:]
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
        goal = goal[goal.find(";") + 1:]
        strings_goal.append(list(aux))
        if goal.find(";") < 0:
            aux = goal
            aux = aux.replace("(", "")
            aux = aux.replace(")", "")
            aux = aux.replace(",", "")
            aux = aux.replace(" ", "")
            strings_goal.append(list(aux))
            break

    for x in range(0,len(strings_goal)):
        # print(strings_goal[x])
        if strings_goal[x] == ['X']:
            result.append(False)
        else:
            result.append(True)
    # print(result)
    # print("Input:"+str(stringsin))
    # print("Goal:"+str(strings_goal))

    breath_tree = depth_node(stringsin, 1, [])

    found = False
    aux_tree = []
    aux_tree.append(breath_tree)
    test = []
    for x in range(0, len(strings_goal)):
        if len(strings_goal[x]) > m_height:
            print("No solution found")
            exit(0)
    while not found:
        for x in range(0, len(aux_tree)):
            time.sleep(.2)
            # print(aux_tree[x].__class__ == depth_node)
            if aux_tree[x].__class__ == depth_node:
                temp = aux_tree[x].create_children()
            print(temp)
            if temp == "False":
                found = True
                print("No solution found")
                break
            test += temp
        else:
            aux_tree = copy.copy(test)
            test = []
    exit(0)