//https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/cpp
#include <string>
#include <regex>

std::string extractBody(const std::string &str){
  for (int i = str.length()-1; i >= 0; --i){ 
    if (std::isalpha(str[i])){
      return str.substr(0,i+1);
    }
  }
  return "";
}

std::string extractAndUpdateNumberString(const std::string &str){
  std::string originalNumberString = "";
  std::string newNumberString = "";
  int number = 1;
  for (int i = str.length()-1; i >= 0; --i){
    if (std::isdigit(str[i])){
      originalNumberString = str[i] + originalNumberString;
    } else {
      break;
    }
  } 
  if (originalNumberString != ""){
    number = std::stoi(originalNumberString) + 1;
    newNumberString = std::to_string(number);
    if (originalNumberString.length() > newNumberString.length()){
        newNumberString.insert(0, originalNumberString.length() - newNumberString.length(), '0');
    }
  } else {
    newNumberString = std::to_string(number);
  }
  return newNumberString;
}

std::string incrementString(const std::string &str)
{
  std::string stringBody = extractBody(str);
  std::string stringNumber = extractAndUpdateNumberString(str);
  return stringBody + stringNumber;
}


/* Modified Alternate Solution, uses 1 less loop, trivial difference on complexities

std::string incrementString(const std::string &str)
{
  std::string updated = str;
  if (updated.empty() || !isdigit(updated.back())){
    return updated + "1";
  }

  for (int i = str.length() - 1; i >= 0; i--){
    if(isdigit(updated[i])){
      if (updated[i] < '9'){
        updated[i]++;
        return updated;
      } else {
        updated[i] = '0';
        continue;
      }
    } else {
      updated.insert(i+1, "1");
      return updated;
    }
  }
  return updated;
}

*/


