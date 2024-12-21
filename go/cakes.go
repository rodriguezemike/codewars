//https://www.codewars.com/kata/525c65e51bf619685c000059/train/go

package kata

func Cakes(recipe, available map[string]int) int {
  cakes := int(^uint(0) >> 1)
  for ingredient, amount := range recipe{
    val, ok := available[ingredient]
    if !ok{
      return 0
    }else if ok && val/amount < cakes && val/amount >= 0 {
      cakes = val/amount
    }
  }
  return cakes
}

