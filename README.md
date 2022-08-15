# CrackingMyCodingInt

I got the job at Adobe, but I kind of miss these questions so I'm going back through the Neetcode 150 list. Let's see how consistent I am lol....


## Question List

| Question Name | Approach | Insight |
| ----------- | ----------- | -------------- |
| Two Sum | Brute force is to use two loops for the first val and check the rest of the values. Optimal approach is ahashmap that you update so you can access it in constant lookup time. | When in doubt, see if you can cast things to a HashMap to reduce lookup time and not get exponential time complexity |
 | Remove Vowels | Just iterate through it once and add elements not found to the answer string. You could use replace but that's also doing iteration at a lower level. | I don't think this will be used in an interview, but you can use '+=' to put something onto the end of a string in Python. |
 | Contains Duplicate | Check the len of nums against that of the len of a set(nums) | You could also use a hashmap to
 track if something is contained and if it isn't insert it into the map |
 | Single Number | Hashmap for tracking how many times a number appears. Iterate through the map after and return the
 key where the val is 1. | Basically what the other part said.  |


