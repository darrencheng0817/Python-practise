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
    <td>Tips, if I wanna 6, I search for both 5.5 and 6.5, then find both lower and upper boundaries for both cases.</td>
  </tr>
  <tr>
    <td>35</td>
    <td>Search Insert Position</td> 
    <td></td>
    <td></td>
    <td></td>
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
    <td></td>
  </tr>
  <tr>
    <td>40</td>
    <td>Combination Sum II</td> 
    <td></td>
    <td></td>
    <td></td>
  </tr>
  </table>
  
  <h4>31-60</h4>
  <table style="width:100%">
  <tr>
    <th>Index</th>
    <th>Name</th>
    <th>source code</th>
    <th>Improved</th>
  </tr>
  <tr>
    <td>1</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>5</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>6</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>7</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>8</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>9</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>10</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>11</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>12</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>13</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>14</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>15</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>16</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>17</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>18</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>19</td>
    <td></td> 
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>20</td>
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
