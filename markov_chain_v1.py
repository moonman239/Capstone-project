
#dataset_1 = hstack((X_1_dev,Y_1_dev))
def markovChainModel(data,STATE_LEN):
    from collections import OrderedDict
    model = OrderedDict()
    stateIndex = 0
    nextIndexFunction = lambda x: x + STATE_LEN
    while (nextIndexFunction(stateIndex) <= len(data)):
        nextIndex = nextIndexFunction(stateIndex)
        state = tuple(data[stateIndex:stateIndex + STATE_LEN])
        next = tuple(data[nextIndex:nextIndex + STATE_LEN])
        # Store the number of times we have encountered this next state after the current state.
        try:
            model[state][next] += 1
        except:
            if (stateIndex < len(data) - 1):
                model[state] = {next:1}
            else:
                # End of string.
                model[state] = {"EOS":0}
        stateIndex = nextIndex
    return model
    
def predict(model,state_length,state=-1,count=0,maxCount=500):
    # Check for base case.
    if (state ==-1):
        state = list(model.keys())[0]
        #print(state)
    chain = [state]
    # Predict the next state.
    nextStates_dict = model[state]
    nextStates = nextStates_dict.keys()
    nextStates = sorted(nextStates,key=lambda x: nextStates_dict[x],reverse=True)
    nextState = nextStates[0]
    print(nextState)
    if nextState != "EOS":
        #Not done!
        nextState = nextStates[0]
        chain.extend(predict(model,state_length,state=nextState,count=count,maxCount=maxCount))
    count += 1
    return chain

string = "Hello, I am sam"