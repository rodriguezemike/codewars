//https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/cpp

#include <string>
bool solution(std::string const &str, std::string const &ending) {
    return str.size() >= ending.size() && str.compare(str.size() - ending. Size(), ending.size(), ending) == 0;
}
