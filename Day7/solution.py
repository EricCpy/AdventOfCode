class TreeNode(object):
    def __init__(self, key, size=0):
        self.size = size
        self.children = {}
        self.key = key
    
    def __str__(self):
        for n in self.children:
            print(self.children[n])
        
        return self.key + " " + str(self.size)

def buildTree():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    root = TreeNode('/')
    curr = root   
    parents = [root]
    for x in data[1:]:
        split = x.split(' ')
        if split[0] == '$' and split[1] == 'cd':
            if split[2] == '..':
                parents.pop()
                curr = parents[-1]
            else:
                if split[2] in curr.children:
                    curr = curr.children[split[2]]
                else:
                    curr.children[split[2]] = TreeNode(split[2])
                    
                parents.append(curr)           
        elif split[0] != '$':
            if split[0] == 'dir' and split[1] not in curr.children:
                curr.children[split[1]] = TreeNode(split[1])
            else:
                curr.size += int(split[0])
                
    childValsToParent(root)
    return root
    
def childValsToParent(root):
    for n in root.children:
        root.size += childValsToParent(root.children[n])

    return root.size

def sumChildsSmaller(root, max):
    val = 0
    if root.size <= max:
        val += root.size
    
    for n in root.children:
        val += sumChildsSmaller(root.children[n], max)
    
    return val

def findSmallestBigger(root, val, currMax):
    if root.size >= val:
        currMax = min(currMax, root.size)
    
    for n in root.children:
        if root.children[n].size >= val:
            currMax = min(findSmallestBigger(root.children[n], val, currMax), currMax)
        
    return currMax

def solution1(root, max):  
    return sumChildsSmaller(root, max)

def solution2(root, needed):  
    return findSmallestBigger(root, needed - (70000000 - root.size), root.size)

if __name__ == "__main__":
    root = buildTree()
    print(solution1(root, 100000))
    print(solution2(root, 30000000))