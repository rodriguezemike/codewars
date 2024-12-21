//Open and closed valid brackets problem

func ValidBraces(str string) bool {
  bracketStack := []byte{}
  for i:=0; i < len(str); i++{
    if string(str[i]) == "}" {
      if string(bracketStack[len(bracketStack)-1]) != "{"{
        return false
      }
      bracketStack = bracketStack[:len(bracketStack)-1]
    }else if string(str[i]) == ")"{
      if string(bracketStack[len(bracketStack)-1]) != "("{
        return false
      }
      bracketStack = bracketStack[:len(bracketStack)-1]
    } else if string(str[i]) == "]"{
      if string(bracketStack[len(bracketStack)-1]) != "["{
        return false
      }
      bracketStack = bracketStack[:len(bracketStack)-1]
    } else {
      bracketStack = append(bracketStack, str[i])
    }
  }
  if len(bracketStack) != 0{
    return false
  }
  return true
}
