//https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/cpp

#include <string>
#include <unordered_map>
std::string duplicate_encoder(const std::string& word){
  std::string toReturn = "";
  std::unordered_map<char, int> countMap;
  for (unsigned long i=0; i < word.length(); ++i){
    if(countMap.find(std::tolower(word[i])) == countMap.end()){
      countMap[std::tolower(word[i])] = 1;
    } else {
      countMap[std::tolower(word[i])] += 1;
    }
  }
  for (unsigned long i=0; i < word.length(); ++i){
    if (countMap[std::tolower(word[i])] > 1){
      toReturn.insert(toReturn.length(), 1, ')');
    } else {
      toReturn.insert(toReturn.length(), 1, '(');
    }
  }
  return toReturn;
}

// Modified Alternative

#include <string>
#include <unordered_map>

std::string duplicate_encoder_new(const std::string& word){
  std::string toReturn;
  std::unordered_map<char, int> countMap;
  
  for(auto c: word) countMap[std::tolower(c)]++;
  for(auto c: word) toReturn += countMap[std::tolower(c)] > 1 ? ")":"(";
    
  return toReturn;
}

