std::string to_camel_case(std::string text) {
  std::set<char> delimiters = {'-', '_'};
  std::string result = "";
  for (int i=0; i < int(text.size()); ++i){
    if(delimiters.find(text[i]) != delimiters.end()){
      result = result + std::string(1, toupper(text[i+1]));
      ++i;
    } else {
      result = result + std::string(1, text[i]);
    }
  }
  return result;
}
