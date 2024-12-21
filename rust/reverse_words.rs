//https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/rust

fn reverse_words(str: &str) -> String {
    // your code here
    let mut reversed: Vec<String> = Vec::new();
    for word in str.split(" "){
        reversed.push(word.chars().rev().collect::Vec<String>())
    }
    return reversed.join(" ")
}

fn reverse_words_functional(str: &str) -> String {
    str.to_string()
      .split(" ")
      .map(|sub| sub.chars().rev().collect())
      .collect::<Vec<String>>()
      .join(" ")
}
