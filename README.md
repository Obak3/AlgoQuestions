# Algorithmic Questions

I got the job at Adobe, but I kind of miss these questions so I'm going back through the Neetcode 150 list. Let's see how consistent I am lol....

This is the list: [List](neetcode.io)

## Arrays and Hashing

| Question Name | Approach | Insight |
| ----------- | ----------- | -------------- |
| Two Sum | You could brute force this with two loops that iterate over the array and check for a match between i and j and return the indices. You could also use a map to do a lookup for the complement of the target - cur val and then return the associated indices. | Pretty efficient because of the O(1) lookup on the map. | 
| Contains Duplicate | Two ways; hashmap where you add the value as the key and the value for the key as the count of occurences and also check the length of a set of the given array against the len of the given array. | Python is sick. |
| Valid Anagram | Two ways; cast both strings to a list, sort it, and then check if they're equal and then you could do a map. | Python is still sick. |
| Group Anagrams | Create a map that uses a sorted string as the KEY of the map with the values being an array of the words in the input list that are compreised of the letters from the key | yeah.... idk |
