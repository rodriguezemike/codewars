//https://www.codewars.com/kata/517abf86da9663f1d2000003/train/rust

fn to_camel_case(text: &str) -> String {
    let mut res = "".to_string();
    let mut chars = text.chars().peekable();
    while let Some(c) = chars.next(){
        match c.to_string().as_str(){
            "_" => res.push_str(chars.next().unwrap().to_string().to_uppercase().as_str()),
            "-" => res.push_str(chars.next().unwrap().to_string().to_uppercase().as_str()),
            &_ => res.push(c)
        };    
    } 
    res
}

//Functional with variable name expansion
fn to_camel_case_functional(text: &str) -> String {
    text.split(&['-','_'])
        .enumerate()
        .map(|(index, word)| match index{
            0 => word.to_string(),
            _ => word[..1].to_uppercase() + &word[1..],
    })
    .collect()
}
