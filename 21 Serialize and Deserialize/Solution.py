from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        
        # write your code here
        if root == None:
            return '{}'
            
        q = deque()
        q.append(root)
        
        i = 0
        while i < len(q):
            node = q[i]
            if node == None:
                i += 1
                continue
            q.append(node.left)
            q.append(node.right)
            i += 1
            
        while q[-1] == None:
            q.pop()

        result = str(q[0].val)
        q.popleft()
        
        for node in q:
            if node != None:
                result += ',' + str(node.val)
            else:
                result += ',#'
                
        return '{' + result + '}'
        

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data == '{}':
            return None
        
        data = data.lstrip('{').rstrip('}')
        values = data.split(',')
        
        root = TreeNode(int(values[0]))
        
        q = deque()
        q.append(root)
        isLeft = True
        index = 0
        
        for n in values[1:]:
            if n != '#':
                node = TreeNode(int(n))
                if isLeft:
                    q[index].left = node
                else:
                    q[index].right = node
                q.append(node)
            if not isLeft:
                index += 1
            isLeft = not isLeft
        return root

if __name__ == "__main__":
    data = '{3,9,20,#,#,15,7}'
    sol = Solution()
    root = sol.deserialize(data)
    print(sol.serialize(root))

    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    print(sol.serialize(root))

            