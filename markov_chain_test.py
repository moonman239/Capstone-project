
#dataset_1 = hstack((X_1_dev,Y_1_dev))
# Works with a data iterator.
def markovChainModel(data):
    model = {}
    stateIndex = 0
    # While iterator has items, get next item.
    try:
        # Python allows us to grab each item in an iterator one at a time.
        state = ""
        transition = next(data)
        # We don't know when we have run out of items until Python gives us an exception.
        while (True):
            state = transition
            transition = next(data)
            # Store the number of times we have encountered this next state after the current state.
            try:
                model[state][transition] += 1
            except:
                model[state] = {transition:1}
    except Exception as e:
        print("Exception reached",e)
    return model
    
def predict(model,state_length=1,state=-1,count=0,maxCount=500): #WARNING: Assumes dictionary is ordered with the first word at the beginnning.
    # Check for base case.
    if (state ==-1):
        state = list(model.keys())[0]
        #print(state)
    chain = [state]
    # Predict the next state.
    try:
        nextStates_dict = model[state]
    except Exception:
        # Most likely done.
        return chain
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
string = "Hello I am Sam and I like cheese and enchiladas."
stringIterator = iter(string.split())
model = markovChainModel(stringIterator)
print("Model:",model)
print (predict(model,1))