//https://www.codewars.com/kata/517abf86da9663f1d2000003/train/go

package kata

import "strings"


func ToCamelCase(s string) string {
  // your code
  res := ""
  for i:=0; i < len(s); i++{
    if string(s[i]) == "_" || string(s[i]) == "-"{
      res += strings.ToUpper(string(s[i+1]))
      i += 1
    }else{
      res += string(s[i])
    }
  }
  return res
}
