from collections import deque

from debugger import debug


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):        
    traversal_queue = deque([root]) if root else None
    while traversal_queue:
        cur_node = traversal_queue.popleft()
        cur_node.left, cur_node.right = cur_node.right, cur_node.left
        if cur_node.left:
            traversal_queue.append( cur_node.left )
        if cur_node.right:
            traversal_queue.append( cur_node.right )                
    return root


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    debug(invertTree, (root,))