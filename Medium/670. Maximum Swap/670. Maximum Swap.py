class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num

        # turn num into an array (reversed though)
        n = []
        while num:
            n.append(num%10)
            num //= 10

        # return num back to its original order
        n.reverse()

        # find the point that needs to be swapped
        j = 0
        k = len(n)
        while j < k and n[j] == max(n[j:]):
            j += 1

        # starting from the other end, find the largest number to swap with
        cur_max = n[k-1]
        max_index = k-1
        for i in range(k-2, j, -1):
            if n[i] > cur_max:
                max_index = i
                cur_max = n[i]


        # perform swap if a swap can be performed
        if j < k:
            print(j, max_index)
            n[j], n[max_index] = n[max_index], n[j] # god i love python bro

        # turn num back into a number
        i = 0
        while i < k:
            num *= 10
            num += n[i]

            i += 1
        print(n)
        return num
        """
        Time Complexity = O(n) (techinically) but since n <= 8 -> O(8) worst case ~ O(1)
        Space Complexity = O(n) but for the same reason why TC = O(1), SC = O(1)
        """
