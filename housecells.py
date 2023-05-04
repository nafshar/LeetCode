def house(states, days):
    # add padding
    day = []
    myop = lambda a, b: 0 if a == b else 1
    states.insert(0,0)
    states.append(0)
    for i in range(days):
        for j in range(1, len(states)-1):
            day.append(myop(states[j-1], states[j+1]))
            print ("day(", j-1, " ) = ", day[j-1])
        #replace the oringial states with current
        for k in range(len(day)):
            states[k+1] = day[k]

        #clear day list
        day = []
    return states[1:-1]

def housecells():
    td = [1, 1, 1, 0, 1, 1, 1, 1]
    state = house(td, 2)
    print(state)

if __name__ == "__main__":
    housecells()


