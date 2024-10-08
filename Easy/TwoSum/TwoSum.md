### Two Sum

The idea is to find the complement (or pair) necessary for their sums to equal the target.

To do this, you just need to find the pair for any number such that its sum is equal to the target.

i.e. for each number:
        cur = cur number
        for the remaining numbers:
            num = one of the remaining numbers
            if cur + num = given target:
                pair is found

this requires re-searching for every number. if there are n numbers then you need to search through n-1 numbers (excluding itself) n times -> O(n*(n-1)) which is about O(n^2)

to speed this up, instead of searching through the list for each individual number, you can check to see if the missing number is in the list as you go.

this can be done using this equation
target = num1 + num2 -> num2 = target - num1

By using this equation, you now have an actual number in mind as you search, removing the need to check each number's sum to the current number's sum. Now all you have to do is check if the number you're on is a number you needed earlier

so now it'd be something like this:
for each number:
    if num was needed earlier:
        pair is found
    else:
        save this number's pair -> num2 = target - num1

Now all you need to do is figure out how to save the numbers. You can use two lists, two arrays, or a hash map. I chose a hash map, because it cuts down on the time needed to check if a number was needed earlier.

(if you used a list you have to check each saved number one by one)

and that's it.