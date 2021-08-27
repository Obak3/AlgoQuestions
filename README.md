# CrackingMyCodingInt

This is a **personal** repo that is designed to keep me accountable as I prepare for interview season. I'll list week by week what I'm doing, what I accomplished, etc. This will be updated frequently.     

## Tracking Problems

### Hash Map 

| Question | Solution | Additional Insight |
| --- | ----------- | ---------------------- |
| Two Sum (Easy) | Create a hashmap so you have constant lookup time and don't have to iterate again. | Try to use hashmaps wherever you can, you'll probably get SOMEWHERE. |
| Roman to Integer (Easy) | Create a lookup table to reference instead of splitting the string and having thousands of if statements. | You have to keep in mind what the rules of the problem are without blindly diving in. I forgot about "iv" reading as 4, so my first solution was very off base. |
| Best Time to Buy and Sell Stocks (Easy)| Create a min and max int var to write and read from while iterating. Max profit is set to the max() of the maxprofit var and the value at the current iteration (minus) the min value where the min is the min() of the min and the current iteration. | Don't be afraid to create new data strucutures. |
|Two Sum II - Input array is sorted| Same kind of deal with the two-sum problem where you create a hashmap and update it on the iteration for the i, value enumerate(list) method. Only trick with this was that they said that it had to be a 1 index list, which means that the index began at 1. | Pay pretty close attention to what was said or else you're going to get bodied. |


### Linked Lists

| Question | Solution | Additional Insight |
| --- | ----------- | ---------------------- |
| Linked List Cycle (Easy) | You're not given the index position to see if it's truly linked. So either do a while loop and add to a set because you can't have duplicate values or use a two pointer solution. | Two pointer solutions are kind of sick, try to use them where you can and run some problems with just those. |

### Graphs 

I got an interview at Google! Look at the README for updates on how I prep.

