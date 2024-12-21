// https://www.codewars.com/kata/550f22f4d758534c1100025a/train/go

package kata

func max(a int, b int) int {
  if a > b {
    return a
  }
  return b
}

func min(a int, b int) int {
  if a < b {
    return a
  }
  return b
}

func compare(slice []string, strA string, strB string) bool {
  if (slice[0] == strA && slice[1] == strB) || (slice[0] == strB && slice[1] == strA){
    return true
  }
  return false
}

func remove(arr []string, i int) []string {
  if len(arr) > 2 {
    j := max(0, i)
    k := min(i+2, len(arr))
    return append(arr[:j], arr[k:]...)
  } else {
    return []string{}
  }
}

func DirReduc(arr []string) []string {
  arrLen := len(arr)
  i := 0
  horizontal := []string{"NORTH", "SOUTH"}
  vertical := []string{"EAST", "WEST"}
  for i < arrLen-1{
    if compare(horizontal, arr[i], arr[i+1]) || compare(vertical, arr[i], arr[i+1]){
      arr = remove(arr, i)
      arrLen = len(arr)
      i = max(0, i-1)
      continue
    }
    i+=1
  }
  return arr
}

