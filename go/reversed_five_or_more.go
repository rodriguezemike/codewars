/*
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
*/

package kata

import (
  "strings"
)

func reverse(str string) string {
  reversed_string := ""
  str_rune := []rune(str)
  for i:= len(str)-1; i > -1; i-- {
    reversed_string += string(str_rune[i])
  }
  return reversed_string
}

func SpinWords(str string) string {
  var result []string
  words := strings.Split(str, " ")
  for i:= 0; i < len(words); i++ {
    if len(words[i]) > 4 {
      result = append(result, reverse(words[i]))
    } else {
      result = append(result, words[i])
    }
  }
  return strings.Join(result, " ")
}
