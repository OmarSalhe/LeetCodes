### 27. Remove Element

Two things to note from the instructions: 
    1. only the first k elements are checked 
    2. order doesn't need to be preserved.

From those two facts, you should begin to realize you're not actually 'removing' elements (although popping elements would still work) but rather just all the not 'to-be-removed' elements (AKA valid elements) to the first k elements.

Following this idea, you now should question what that would look like and or how that should work. Since you don't need to worry about order you could simply just replace all non-valid elements with valid elements.

i.e.
    if num is not valid:
        swap with valid element

with this general idea, there are two things that need answers before starting:
    1. how do you swap?
    2. how do you have valid elements on standby?/where are the valid elements coming from?

for the first question, since you don't need to worry about order, you can just set the invalid element there to be a valid element from later on.
leading into the second question, the valid elements would come from the valid elements from later on in the list.

when put together it would look something like this:
    remove = 3, k = 3
    list = [0, 1, 2, 3, 4] 

    before:
    list = [0, 1, 2, 3, 4] 

    after:
    list = [0, 1, 2, 4, 4] -> [1,2,4] is what would be checked

this is the general idea to the approach. to just swap (or shift if that helps) all the invalid elements with valid elements such that the first k elements are valid.

to do this you would need:
    A -> an invalid element
    B -> a valid element

from this you should see two pointers are used. one for keeping track of invalid elements and one for keeping track of valid elements to swap with.

There are technically two ways to do this, so my solution is just one way.

both are:
    x = 0 -> an index starting at the beginning
    for each element:
    if element is valid:
        place it at x
        shift x forward by 1
    else:
        continue
    
    this approach just places all valid elements at the start even if they are in a good spot.  (which is why I said swapping OR shifting)

    ex. list = [3, 1, 2], remove = 3, k = 2

        x = 0
        [3, 1, 2] -> 3 is invalid -> continue
         ^
        x = 0
        [3, 1, 2] -> 1 is valid -> place it at x -> [1, 1, 2]
            ^
        x = 1
        [1, 1, 2] -> 2 is valid -> place it at x ->  [1, 2, 2]
               ^ 

        result (AKA the first k elements) = [1, 2] 


    second approach
    x = 0 -> a pointer to go through the list from the start (catches invalid elements)

    y = n -> a pointer starting from the end of the list (catches all the valid elements outside of the checked range)

    for each element:
        if element at x is valid:
            shift x by one -> only stops for invalid elements

        if element at y is invalid:
            shift y by one -> only stops for valid elements
        
        numX = num at x
        numY = num at Y

        if numX is invalid and numY is valid:
            set element at X to be numY

        if x and y are at the same point:
            stop

    this swaps only the invalid elements, which keeps order, but is longer to code.

    obv i chose the first one since its the shortest, but both should work. 

        


