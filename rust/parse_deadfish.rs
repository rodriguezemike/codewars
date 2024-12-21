//https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/rust

fn parse(code: &str) -> Vec<i32> {
    let mut result: Vec<i32> = Vec::new();
    let mut tmp = 0;
    for character in code. Chars(){
        match character.to_string().as_str() {
            "i" => tmp+=1,
            "d" => tmp-=1,
            "s" => tmp*=tmp,
            "o" => result.push(tmp),
            _ => continue
        }
    }
    result
}


fn parse_functional(code:&str) -> Vec<i32>{
    let mut tmp = 0;
    code.chars()
        .fold(Vec::new(), |mut vector, c|{
            match c.to_string().as_str(){
            "i" => tmp+=1,
            "d" => tmp-=1,
            "s" => tmp*=tmp,
            "o" => vector.push(tmp),
            &_ => ()            
            };
            vector
        }
    )
}
