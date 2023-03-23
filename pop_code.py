class Pop():
  def __init__(self, layout, window, queries):
    self.layout = layout
    self.window = window
    self.queries = queries
  def appqry(self, query):
    self.queries.append(query)
  def readqry(self, queries):
    return self.queries
  
pop_layout = [[sg.Input(), sg.Button("SAVE") [sg.Button("OPEN")]]
pop_query = []

pop_init = Pop(pop_layout, sg.Window("Pop", pop_layout), pop_query)

