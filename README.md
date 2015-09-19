# Python-practise

<h4>1-20</h4>
<table style="width:100%">
  <tr>
    <th>Index</th>
    <th>Name</th>
    <th>source code</th>
    <th>Improved</th>
    <th>Note</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Two Sum</td>
    <td></td>
    <td>Ok</td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Add Two Numbers</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Longest Substring Without Repeating Characters</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Median of Two Sorted Arrays</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Longest Palindromic Substring</td> 
    <td></td>
    <td>Bad</td>
    <td>Need improve</td>
  </tr>
  <tr>
    <td>6</td>
    <td>ZigZag Conversion</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Reverse Integer</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>8</td>
    <td>String to Integer (atoi)</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>9</td>
    <td>Palindrome Number</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>10</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>11</td>
    <td>Container With Most Water</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>12</td>
    <td>Integer to Roman</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>13</td>
    <td>Roman to Integer</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>14</td>
    <td>Longest Common Prefix</td> 
    <td></td>
    <td>Yes</td>
    <td>My approach, 1, compare two shorest string, 2, compare char by char</td>
  </tr>
  <tr>
    <td>15</td>
    <td>3Sum</td> 
    <td></td>
    <td>Yes</td>
    <td>1, can use hashmap, too. 2, can choose set, 3, my approach, less space cost</td>
  </tr>
  <tr>
    <td>16</td>
    <td>3Sum Closest </td> 
    <td></td>
    <td>Yes</td>
    <td>Trick, if find target, return immediately</td>
  </tr>
  <tr>
    <td>17</td>
    <td>Letter Combinations of a Phone Number </td> 
    <td></td>
    <td>Yes</td>
    <td>IMPORTANT, Bracktracking method, need to redo it again</td>
  </tr>
  <tr>
    <td>18</td>
    <td>4 Sum</td> 
    <td></td>
    <td>Yes</td>
    <td><a href="http://blog.csdn.net/linhuanmars/article/details/24826871" target="_blank">2, 3, 4 sum summary</a> Best approach is O(kn^2), k is the hashvalue average length 哈嘻表, LESSONS Learned, When using API like set.add(). be careful. It is very costly</td>
  </tr>
  <tr>
    <td>19</td>
    <td>Remove Nth Node From End of List</td> 
    <td></td>
    <td>Ok</td>
    <td>My apporoach: 1, change the node, delete the last one. 2, inorder traverse(n = total - n). Other approach: Remove directly or using list as extra storage. TRY recursive later</td>
  </tr>
  <tr>
    <td>20</td>
    <td>Valid Parentheses</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  </table>
  
  <h4>21-40</h4>
  <table style="width:100%">
  <tr>
    <th>Index</th>
    <th>Name</th>
    <th>source code</th>
    <th>Improved</th>
    <th>Note</th>
  </tr>
  <tr>
    <td>21</td>
    <td>Merge Two Sorted Lists</td>
    <td></td>
    <td>Yes</td>
    <td>Note, not best performance need to improve</td>
  </tr>
  <tr>
    <td>22</td>
    <td>Generate Parentheses</td> 
    <td></td>
    <td>Yes</td>
    <td>poor performance, I used iteration, Can try recursion, I also have it in CC150</td>
  </tr>
  <tr>
    <td>23</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>24</td>
    <td>Swap Nodes in Pairs</td> 
    <td></td>
    <td>Yes</td>
    <td>It is not a hard problem, but it is very easy to make mistake. if seperate the reverse pair into two case:
    1, the init case and other cases. The inital case is simple and do not need to think about the connections between previous nodes</td>
  </tr>
  <tr>
    <td>25</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>26</td>
    <td>Remove Duplicates from Sorted Array</td> 
    <td></td>
    <td>Yes</td>
    <td>The question itself does not state clear, Two points: 1, return length 2, new list with no-duplicate elements and it doesn't matter what you leave beyond the new length.</td>
  </tr>
  <tr>
    <td>27</td>
    <td>Remove Element</td> 
    <td></td>
    <td>Yes</td>
    <td>Tips, be careful about changing and iterating the list at the same time</td>
  </tr>
  <tr>
    <td>28</td>
    <td>Implement strStr()</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>29</td>
    <td>Divide Two Integers</td>
    <td></td>
    <td>Yes</td>
    <td>NNNEED to redo it. Some tricks. 1, two nested while loop, only decrease in the inner loop. 2, the difference between the <<= and <<: 
    1, << shifts things, but if you don not assign the result to anything, nothing will be record.
    ex: y = 8. y<<1 -> this gives you 16, but y will still be 8. But for <<=,  y = 8. y <<=1 -> y becomes 16
    </td>
  </tr>
  <tr>
    <td>30</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>31</td>
    <td>Next Permutation</td> 
    <td></td>
    <td>Yes</td>
    <td><a href="https://leetcode.com/discuss/17631/share-my-python-code-and-explain-how-to-get-the-solution" target="_blank">Detailed alg, 3 major steps, 1, find, 2, swapping, 3 sorting.</a>Trick, do not return, you need an in-place sorting alg</td>
  </tr>
  <tr>
    <td>32</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>33</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>34</td>
    <td>Search for a Range</td> 
    <td></td>
    <td>Yes</td>
    <td>Tips, if I wanna 6, I search for both 5.5 and 6.5, then find both lower and upper boundaries for 6.</td>
  </tr>
  <tr>
    <td>35</td>
    <td>Search Insert Position</td> 
    <td></td>
    <td>Yes</td>
    <td>Easy, maybe have some other cool way to solve it</td>
  </tr>
  <tr>
    <td>36</td>
    <td>Valid Sudoku</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>37</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>38</td>
    <td>Count and Say</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>39</td>
    <td>Combination Sum</td> 
    <td></td>
    <td>Yes</td>
    <td>First, sorted. Then, dfs:  index keep the same position for recursion</td>
  </tr>
  <tr>
    <td>40</td>
    <td>Combination Sum II</td> 
    <td></td>
    <td>Yes</td>
    <td>Performance matters, the recursive call need to prevent the duplicate cases. First, increasing index, Second, the consecutive duplicated integer should be ignored. tracking the current value. GOOD LUCK</td>
  </tr>
  </table>
  
  <h4>41-60</h4>
  <table style="width:100%">
  <tr>
    <th>Index</th>
    <th>Name</th>
    <th>source code</th>
    <th>Improved</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td>41</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>42</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>43</td>
    <td>Multiply Strings</td> 
    <td></td>
    <td>Yes</td>
    <td>May try some other methods, the API is pretty simple. Do not see the point adding char by char</td>
  </tr>
  <tr>
    <td>44</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>45</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>46</td>
    <td>Permutations</td> 
    <td></td>
    <td>Yes</td>
    <td>Permutations: 1, bracktrack question using recursion to solve, faster. 2, the increment normally used in the input, not seperate. the function will auto becoming append and pop. Not hard question overall</td>
  </tr>
  <tr>
    <td>47</td>
    <td>Permutations II</td> 
    <td></td>
    <td>Yes</td>
    <td>Need to redo by iteration. Tricks, 1, similar to closet sum. avoid duplicate iteration. 2, using a list of bool to track the integer used or not. </td>
  </tr>
  <tr>
    <td>48</td>
    <td>Rotate Image</td> 
    <td></td>
    <td>Yes</td>
    <td>for i in( 0, len/2) , then 1, first = i, 2, last = len - i - 1, inner for j in (first, last). Finally, offset = last -i. Neet to draw the matrix. It is not hard, but easy to make a tiny mistake</td>
  </tr>
  <tr>
    <td>49</td>
    <td>Group Anagrams</td> 
    <td></td>
    <td>Yes</td>
    <td>NEED huge improve, the normal way is not efficient. maybe string compression</td>
  </tr>
  <tr>
    <td>50</td>
    <td>Pow(x, n)</td> 
    <td></td>
    <td>Yes</td>
    <td>The odd or even power is different. Also, the positive and negative power is different</td>
  </tr>
  <tr>
    <td>51</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>52</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>53</td>
    <td>Maximum Subarray</td> 
    <td></td>
    <td>Yes</td>
    <td>Poor perfornamce, the DP method will be better, Need to redo later</td>
  </tr>
  <tr>
    <td>54</td>
    <td>Spiral Matrix</td> 
    <td></td>
    <td>Yes</td>
    <td>Trick for 2d Matrix, 1, the matrix: [[]]: len(matrix) == 1 2, the matrix: []: len(matrix) == 0. So we need to check both of cases, before we do the pop operation</td>
  </tr>
  <tr>
    <td>55</td>
    <td>Jump Game</td> 
    <td></td>
    <td>Yes</td>
    <td>First, I disagree this question uses greedy alg, it is not taking the sub-optimal solution for every step. COOL question, track the max every iteration, step increase, max-1. O(n) method can be found</td>
  </tr>
  <tr>
    <td>56</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>57</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>58</td>
    <td>Length of Last Word</td> 
    <td></td>
    <td>Yes</td>
    <td>Nothing hard</td>
  </tr>
  <tr>
    <td>59</td>
    <td>Spiral Matrix II</td> 
    <td></td>
    <td>Yes</td>
    <td>The odd and even cases need to be careful, the logic is similar to array rotating 90 degree</td>
  </tr>
  <tr>
    <td>60</td>
    <td>Permutation Sequence</td> 
    <td></td>
    <td>Yes</td>
    <td>EX: [1, 2, 3, 4], we will have 6! permutation first digit is "1". The next iteration: factorial number: f2 = 6!/i, i = 3. => f2 = 2!</td>
  </tr>
  </table>
  
  <h4>61-80</h4>
  <table style="width:100%">
  <tr>
    <th>Index</th>
    <th>Name</th>
    <th>source code</th>
    <th>Improved</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td>61</td>
    <td>Rotate List</td>
    <td></td>
    <td>Yes</td>
    <td>The rotation k can be larger than len(list). First, k = k % len(list)</td>
  </tr>
  <tr>
    <td>62</td>
    <td>Unique Paths</td> 
    <td></td>
    <td>Yes</td>
    <td>Dp program, using the bottom-up approach to save the result for the subproblems. However, the trick is the initialize the matrix at the beginning</td>
  </tr>
  <tr>
    <td>63</td>
    <td>Unique Paths II</td> 
    <td></td>
    <td>Yes</td>
    <td>Similar method as Question 62. Set 1 to None</td>
  </tr>
  <tr>
    <td>64</td>
    <td>Minimum Path Sum</td> 
    <td></td>
    <td>Yes</td>
    <td>Need an improvement</td>
  </tr>
  <tr>
    <td>65</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>66</td>
    <td>Plus One</td> 
    <td></td>
    <td>Ok</td>
    <td>May be need some other approach, nothing hard</td>
  </tr>
  <tr>
    <td>67</td>
    <td>Add Binary</td> 
    <td></td>
    <td>Ok</td>
    <td>Need an improvement</td>
  </tr>
  <tr>
    <td>68</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>69</td>
    <td>Sqrt(x)</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>70</td>
    <td>Climbing Stairs</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>71</td>
    <td>Simplify Path</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>72</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>73</td>
    <td>Set Matrix Zeroes</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>74</td>
    <td>Search a 2D Matrix</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>75</td>
    <td>Sort Colors</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>76</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>77</td>
    <td>Combinations</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>78</td>
    <td>Subsets</td> 
    <td></td>
    <td>Yes</td>
    <td></td>
  </tr>
  <tr>
    <td>79</td>
    <td>Word Search</td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>80</td>
    <td>Remove Duplicates from Sorted Array II</td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  </table>
  
  <h4>61-80</h4>
  <table style="width:100%">
  <tr>
    <th>Index</th>
    <th>Name</th>
    <th>source code</th>
    <th>Improved</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td>41</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>42</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>43</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>44</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>45</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>46</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>47</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>48</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>49</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>50</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>51</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>52</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>53</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>54</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>55</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>56</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>57</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>58</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>59</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>60</td>
    <td></td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  </table>
  <table style="width:100%">
  <tr>
    <th>Index</th>
    <th>Name</th>
    <th>source code</th>
    <th>Improved</th>
  </tr>
  <tr>
    <td>36</6td>
    <td>Valid Sudoku</td> 
    <td></td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>37</6td>
    <td>Count and Say</td> 
    <td></td>
    <td>Ok</td>
  </tr>
  <tr>
    <td>146</6td>
    <td>LRU Cache</td> 
    <td></td>
    <td>Ok, need other approach</td>
  </tr>
  <tr>
    <td>202</6td>
    <td>Happy Number</td> 
    <td></td>
    <td>Yes</td>
  </tr>
  </table>
