'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Creates a default value of list in the dict and avoids key not found
        lookup = defaultdict(list)
        
        # Iterate over every element in the list of words
        for s in strs:
            # set the key to the sorted letters of the word...
            # Sorted() returns a list, so that's why we join on an empty space to set the proper key
            key = "".join(sorted(s))
            # Append the 's' value to the key respective to the sorted string
            lookup[key].append(s)
            
        # Empty anwer var    
        answer = []    
        # for every element in the values for the keys
        for l in lookup.values():
            # Append to it's own list
            answer.append(l)
        
        return answer
