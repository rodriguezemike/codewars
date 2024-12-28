//https://www.codewars.com/kata/57f609022f4d534f05000024/train/cpp

#include <set>

int stray(std::vector<int> numbers) {
  std::set<int> unique(numbers.begin(), numbers.end());
  for(int num:unique){
    if(count(numbers.begin(), numbers.end(), num) == 1){
      return num;
    }
  }
};
