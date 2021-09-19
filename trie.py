import math
import curses

from collections import defaultdict
from visualization_factory import SCREEN


class Trie:
    """
    Implement a trie with insert, search.
    """
    def __init__(self):
        self.root = dict()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")


    def visualize(self):
        return self.root


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False

def draw_circle(screen, pos_x, pos_y, val):
        r = 2
        for angle in range(0, 360, 5):
            x = r * 2 * math.sin(math.radians(angle)) + pos_x
            y = r * math.cos(math.radians(angle)) + pos_y
            screen.addstr(int(round(y)), int(round(x)), '*')
        screen.addstr(pos_y, pos_x, str(val))

def visualizer(a,space,screen,pos_x,pos_y):
    final_string = ""
    if (a == None):
        #print(len(a))
        #print(a)
        return ("")

    if(len(a) == 1):
        for i in a:
            #print((space*" ") + i + "\n" + visualizer((a[i]),space))
            draw_circle(screen, pos_x, pos_y, i)
            return ((space*" ") + i + "\n" + visualizer((a[i]),space,screen,pos_x,pos_y + 7))
    elif (len(a) == 2):
        #print("2")
        #print(a)
        final_string = ""
        t = True
        for i in a:
            if (t == True):
                first = i
                final_string = ((space-10)*" ") + i
                t = False
        second = i
        final_string = final_string + (20*" ") + i + "\n" + visualizer((a[first]),(space-10),screen,pos_x,pos_y + 7) + visualizer((a[second]),(space + 11),screen,pos_x,pos_y + 7)
        return (final_string)
    else :
        return ("")


test = Trie()
test.insert('helloworld')
test.insert('helloz')
#print(test.visualize())
y, x = SCREEN.getmaxyx()
#print(x)
#print(y)
SCREEN.addstr(1,0,"*****")
print(visualizer(test.visualize(),40,SCREEN,int(x/2), 7))
