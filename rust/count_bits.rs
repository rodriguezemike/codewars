// ?

fn count_bits(n: i64) -> u32 {
    String::from(format!("{n:b}"))
        .chars()
        .fold(0, |mut counter, bit| {
            match bit.to_string().as_str(){
                "1" => counter+=1,
                &_ => () 
            };
            counter
        }
    )
}
