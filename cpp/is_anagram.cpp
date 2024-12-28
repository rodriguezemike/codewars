//https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/cpp

#include <string>
#include <cctype>


bool isAnagram(std::string test, std::string original){
  //your code here
  int sum_test = 0;
  int sum_original = 0;
  
  for (char c : test){
    sum_test += tolower(c);
  }
  for (char c : original){
    sum_original += tolower(c);
  }
  return sum_test == sum_original;
}
