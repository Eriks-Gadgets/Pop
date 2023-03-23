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
pop_win = sg.Window("Pop", pop_layout)
pop_query = []

pop_init = Pop(pop_layout, pop_win, pop_query)

while True:
    event, values = pop_win.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "SAVE":
        pop_init.addqry(values[0])
    if event == "OPEN":
        query_inventory = pop_init.readqry(values[0])
        pop_sub_layout = [[]]
        for query in query_inventory:
            query_inventory[0].append(sg.Text(query))
        pop_sub_window = sg.Window("Past Queries [from this session]:", layout)
              
              
pop_win.close()
