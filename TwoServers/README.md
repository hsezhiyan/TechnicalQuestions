# Problem Statement

Two servers exist. We are given an array, where each entry represents the completion time for a certain process. These processes
all get sent to either of the two servers. We want to  minimize the difference in total completion time between the two servers.
For example, if the input array is [1, 2, 3, 4, 5], we would return 1 because one server would complete processes [1, 3, 4], and the
other [2, 5]. The difference is minimized at (1 + 3 + 4) - (2 + 5) = 1.

**Example test cases**

*Input*: [1, 2, 3, 4, 100]<br />
*Output*: 90

*Input*: [2, 3, 4, 5, 6]<br />
*Output*: 0
