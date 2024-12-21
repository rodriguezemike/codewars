// ?

package kata

func Comp(array1 []int, array2 []int) bool {
  if array1 == nil || array2 == nil{
    return false
  } else if len(array1) == 0 || len(array2) == 0 {
    return false
  } else {
    exists:= false
    square:= 0
    for i:=0; i < len(array1); i++{
      square = array1[i]*array1[i]
      exists = false
      for j:=0; j < len(array2); j++{
        if square == array2[j]{
          exists = true
          break
        }
      }
      if exists == false{
        break
      }
    }
    return exists
  }
}
