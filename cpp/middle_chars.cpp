//https://www.codewars.com/kata/56747fd5cb988479af000028/train/cpp

std::string get_middle(std::string input) 
{
  // return the middle character(s)
  if (input.size() % 2 != 0){
    return std::string(1,input[input.size()/2]);
  } else {
    return std::string(1,input[input.size()/2-1]) + std::string(1, input[input.size()/2]);
  }
}

