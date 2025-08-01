class Notepad():

    def __init__(self):
        self.text = ""
        self.doc = []
        self.cursorPosition = 0

    def addText(self, newText):
        t = self.getText()
        c = self.getCursorPosition()

        self.text = t[:c] + newText + t[c:]
        self.cursorPosition += len(newText) #// Move cursor to the end of the new text
        self.doc.append(self.text)

    def deleteText(self, k):
        c = self.getCursorPosition()
        t = self.getText()
        start_delete = max(0, c-k)
        end_delete = c+k
        temp = t[:start_delete] + t[end_delete:]
        self.cursorPosition = c-k
        self.text = temp
        self.doc.append(temp) 

    def moveText(self, k):
        if k <= 0:
            self.moveCursorLeft(k)
        else:
            self.moveCursorRight(k)
    def undo(self, k):
        # undo the number of steps (at least where the text is, not sure about cursor movement?)
        self.text = self.doc[len(self.doc)-k]
        self.doc.append(self.text)

    def moveCursorLeft(self, k):
        #Moves the cursor left by k
        #Constraints: Ensure the cursor always stays within the valid bounds of the text (not beyond the beginning or end of the document). 
        c = self.getCursorPosition()
        self.cursorPosition = c+k if c+k > 0 else 0

    def moveCursorRight(self, k):
        # Moves the cursor right by k
        #Constraints: Ensure the cursor always stays within the valid bounds of the text (not beyond the beginning or end of the document). 
        c = self.getCursorPosition()
        self.cursorPosition = c+k if c+k < len(self.text) else len(self.text)

    def getText(self):
        return self.text
    def getDoc(self):
        return self.doc
    def getCursorPosition(self):
        return self.cursorPosition
    
    
if __name__ == '__main__':
    queries = [
        ['append', 'hi there '],
        ['append', 'is this '],
        ['append', '!'],
        ['delete', 2],
        ['move', -10],
        ['move', 3],
        ['append', ' ~party in the middle! ~'],
        ['move', 100],
        ['undo', 2]
    ]

    N = Notepad()

    for q in queries:
        if q[0].lower() == 'append':
            N.addText(q[1])
        elif q[0].lower() == 'delete':
            N.deleteText(int(q[1]))
        elif q[0].lower() == 'move':
            N.moveText(int(q[1]))
        elif q[0].lower() == 'undo':
            N.undo(int(q[1]))
    
    print(f'\n ***** \n last known cursor position {N.getCursorPosition()}')

    print(f'\nThe document in total: {N.getDoc()}')

    print(f'\n*************\n All together now {N.getText()}')