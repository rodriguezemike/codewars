//https://www.codewars.com/kata/51b6249c4612257ac0000005/train/rust

fn roman_as_num(roman: &str) -> u64 {
    let roman_chars = vec!["M","CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    let num = vec![1000,900,500,400,100,90,50,40,10,9,5,4,1];
    let mut value = 0;
    let mut chars = roman.chars().peekable();
    let mut skip = false;
    while let Some(c) = chars.next(){
        if skip == true{
            skip = false;
            continue;
        }
        let index_c = roman_chars.iter().position(|&x| x == &c.to_string()).unwrap();
        if let Some(d) = chars.peek(){
            let index_d = roman_chars.iter().position(|&x| x == &d.to_string()).unwrap();
            if index_d < index_c {
                let mut cd = String::new();
                cd.push_str(&c.to_string());
                cd.push_str(&d.to_string());
                let index_cd = roman_chars.iter().position(|&x| x == cd).unwrap();
                value += num[index_cd];
                skip = true;
            } else {
                value += num[index_c];   
            }
        }else {
            value += num[index_c];
        }
    }
    return value;
}
