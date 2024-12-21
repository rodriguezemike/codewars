//https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/rust

use std::collections::HashMap;

fn count(input: &str) -> HashMap<char, i32> {
    let mut countMap: HashMap<char,i32> = HashMap::new();
    for c in input.chars(){
        countMap.entry(c).and_modify(|x| *x+=1).or_insert(1);
    }
    countMap
}


fn count_functional(input: &str) -> HashMap<char, i32> {
    input
        .chars()
        .fold(HashMap::new(), |mut map, c|{
           *map.entry(c).and_modify(|x| *x+=1).or_insert(1);
            map
    })
}

