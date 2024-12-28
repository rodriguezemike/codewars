//https://www.codewars.com/kata/55466989aeecab5aac00003e/cpp

#include <vector>

class SqInRect
{
  public:
  
  static std::vector<int> sqInRect(int lng, int wdth){
    if (lng != wdth){
      std::vector<int> sqres;
      int sqre = std::min(lng, wdth);
      while (lng != wdth){
        if (std::max(lng, wdth) == lng) {
          lng -= sqre;
        } else {
          wdth -= sqre;
        }
        sqres.push_back(sqre);
        sqre = std::min(lng, wdth);
      }
      sqres.push_back(sqre);
      return sqres;
    }
    return {};
  }
};
