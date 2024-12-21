// https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/go

package kata

func swap(arr []int, i int, j int) []int{
  tmp := arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
  return arr
}

func MoveZeros(arr []int) []int {
  swapped := false
  for i:= len(arr)-1; i > 0; i--{
    if arr[i] == 0 {
      continue
    }
    for j:= i-1; j >= 0; j--{
      if arr[j] == 0 && arr[i] != 0{
        for k:= j; k < i; k++ {
          arr = swap(arr, k+1, k)
          }
        }
	swapped = true
      }
    if swapped == false {
      return arr
    }
    swapped = false
  }
  return arr
}
