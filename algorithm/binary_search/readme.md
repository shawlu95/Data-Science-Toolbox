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
* XXOO: Find point of change (first occurrence of a new series) [[278](278_First_Bad_Version.py)].
* XXOO: Find minimum in a rotated array (first bad version logic) [minimim_in_rotated_array.py](minimim_in_rotated_array.py)
* Half-half: Search in rotated sorted array [[33](33_search_in_rotated_sorted_array.py)].
* Half-half: Find peak index in a mountain array. Apply logic, not template [[852](852_peak_index_in_a_mountain_array.py)].
* No array: Square root [[69](69_sqrtx.py)].
* 二分答案：Wood cut [[link](https://www.lintcode.com/problem/wood-cut/description)][[wood_cut.py](wood_cut.py)]
* 二分答案：Copy book [[link](https://www.lintcode.com/problem/copy-books/description)][[copy_book.py](copy_book.py)]
