//https://www.codewars.com/kata/52503c77e5b972f21600000e/train/go
/*
Summary: Write a function which takes an array data of numbers and returns the largest difference in indexes j - i such that data[i] <= data[j]

Long Description:

The largestDifference takes an array of numbers. That array is not sorted. Do not sort it or change the order of the elements in any way, or their values.

Consider all of the pairs of numbers in the array where the first one is less than or equal to the second one.

From these, find a pair where their positions in the array are farthest apart.

Return the difference between the indexes of the two array elements in this pair.


Error here was in readin the problem, It was assumed that it wanted a subarray of numbers such that data[i] <= data[j]. Instead of a block of numbers, it only wanted a single pair of numbers. Not multiple running pairs.

*/

package kata

func LargestDifference(data []int) int {
  for j:= len(data)-1; j > 0; j--{
    for i:=0; i < len(data)-j; i++ {
      if data[i] <= data[i+j]{
        return j
      }
    }
  }
  return 0
}

