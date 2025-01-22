rooms = {
    "room 1" : {"name": "room 1", "description": "description room 1", "completed": "what do you mean completed?"},
    "room 2" : {"name": "room 2", "description": "description room 2", "completed": "what do you mean completed?"},
    "room 3" : {"name": "room 3", "description": "description room 3", "completed": "what do you mean completed?"}
}



# Other examples

# that is my exact question, WTF?
f = lambda x, d=0: {y: f(x, d=d+1) for y in x} if d < len(x) else {}
rooms = f("wtf")



rooms = { 'C': { 'suspect': "Colonel Mustard",
                 'room':    "The Study",
                 'weapon':  "Candlestick" },

          'L': { 'suspect': "Mr. Green",
                 'room':    "The Library",
                 'weapon':  "Revolver" },
                   
          'U': { 'suspect': "Mrs. Peacock",
                 'room':    "The Kitchen",
                 'weapon':  "Knife" },
                   
          'E': { 'suspect': "Professor Plum",
                 'room':    "The Ballroom",
                 'weapon':  "Rope" }, }



rooms = {   'name':        { 
                          'x': {},
                          'y': {},
                          'z': {}
                           },
            'description': {
                          'x': {},
                          'y': {},
                          'z': {}
                           },
            'completed':   {
                          'x': {},
                          'y': {},
                          'z': {}
                           }
        }