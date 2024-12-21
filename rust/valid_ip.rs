//https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/rust/673d1c86ce5de40b7fafd7c1

use regex::Regex;

//Too Slow.
fn is_valid_ip_regex(ip: &str) -> bool {
    let ip_regex = Regex::new(r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]{2}|[1-9]0?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]{2}|[1-9]0?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]{2}|[1-9]0?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]{2}|[1-9]0?|0)$").unwrap();
    ip_regex.is_match(ip)
}

fn is_valid_ip(ip: &str) -> bool {
    ip.split(".")
        .collect::<Vec<&str>>()
        .iter()
        .all(|octet| (!octet.starts_with("0") || octet.len() == 1) && octet.parse::<u8>().is_ok()) && ip.split(".").collect::<Vec<&str>>().len() == 4
}
