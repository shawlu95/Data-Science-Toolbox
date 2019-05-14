### Binary Search
Code template: [[template.py](template.py)].

#### Complexity
T(N) = T(N/2) + O(1) = logN * O(1) + T(1) = O(logN)

分析：用O(1)的时间把问题规模缩小一半。

类比：用O(N)的时间把问题缩小一半

T(N) = T(N/2) + O(N) = ... = O(N + N/2 + N/4 + ...) + T(1) ~= O(2N) = O(N)

#### Variation
* Insertion index: use template, return `r` [[template.py](template.py)].
* Find first occurrence of change [[first_occurence.py](first_occurence.py)].
* Find last occurrence of change [[last_occurence.py](last_occurence.py)].

#### Primer
* Plain vanilla binary search while loop [[704](704_Binary_Search.py)].
* Plain vanilla binary search recursion [[457](457_Classical_Binary_Search.py)].
* Plain vanilla binary search for insert position [[35](35_Search_Insert_Position.py)].

#### Application
* Find point of change (first occurrence of a new series) [[278](278_First_Bad_Version.py)].
* Search in rotated sorted array (XXOO format) [[33](33_search_in_rotated_sorted_array.py)]
