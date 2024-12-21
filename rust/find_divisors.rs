//https://www.codewars.com/kata/544aed4c4a30184e960010f4

fn divisors(integer: u32) -> Result<Vec<u32>, String> {
    let res = (2.. integer).filter(|x| integer % x == 0).collect::<Vec<u32>>();
    match res.is_empty(){
        true => return Err(integer.to_string() + " is prime"),
        false => return Ok(res)
    }
}

