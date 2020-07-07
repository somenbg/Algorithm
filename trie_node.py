class TrieNode():

    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_complete_indicator = False
        self.counter = 1

def add_name(root, string):
    node = root
    for char in string:
        found_in_child = False

        for child in node.children:
            if child.char == char:
                found_in_child = True
                child.counter += 1
                node = child
                break

        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    
    node.word_complete_indicator = True


def find_name(root, string):
    node = root

    if not node.children:
        return False, 0

    for char in string:

        char_not_found = True

        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break

        if char_not_found:
            return False, 0

    return True, node.counter
        
root = TrieNode('*')
add_name(root, "hackathon")
add_name(root, 'hack')
add_name(root, 'hacker')

print(find_name(root, 'hac'))
print(find_name(root, 'hack'))
print(find_name(root, 'hackathon'))
print(find_name(root, 'ha'))
print(find_name(root, 'hammer'))