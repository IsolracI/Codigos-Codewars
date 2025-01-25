# fuck this code, i can only do cabled bullshit
def will_you(young, beautiful, loved):
    if young and beautiful:
        if loved:
            return False
        else:
            return True
    if young or beautiful:
        if loved:
            return True
        else:
            return False
    if not young and not beautiful:
        if loved:
            return True
        else:
            return False
        
#1
def will_you(young, beautiful, loved):
    return (young and beautiful) != loved #me cago en mi mismo, esto tiene tanta puta lógica xD