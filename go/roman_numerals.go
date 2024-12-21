// >

package kata

func Solution(number int) string {
  // convert the number to a roman numeral
  roman_numerals := []string{"M","CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
  numericals := []int{1000,900,500,400,100,90,50,40,10,9,5,4,1}
  roman_numeral_string := ""
  for i:= 0; i < len(numericals); i++ {
    count := int(number/numericals[i])
    for j:= 0; j < count; j++{
      roman_numeral_string += roman_numerals[i]
    }
    number -= numericals[i]*count
  }
  return roman_numeral_string
}
