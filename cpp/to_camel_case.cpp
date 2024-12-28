std::string to_camel_case(std::string text) {
  std::string result = "";
  for (int i=0; i < int(text.size()); ++i){
    if(text[i] == '-' || text[i] == '_'){
      result = result + std::string(1, toupper(text[i+1]));
      ++i;
    } else {
      result = result + std::string(1, text[i]);
    }
  }
  return result;
}

std::string to_camel_case_erase(std::string text){
  for(int i = 0; i < text.size(); ++i)
  {
    if(text[i] == '-' || text[i] == '_')
    {
      text.erase(i,1);
      text[i] = toupper(text[i]);
    }
  }
  return text;
}
