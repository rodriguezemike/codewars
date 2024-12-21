//https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/rust

fn multiplication_table(len: usize) -> Vec<Vec<usize>> {
    let mut table: Vec<Vec<usize>> = Vec::new();
    for i in (1..len+1){
        let mut row: Vec<usize> = Vec::new();
        for j in (1..len+1){
            row.push(i*j);
        }
        table.push(row);
    }
    table
}


fn multiplication_table)functional(len: usize) -> Vec<Vec<usize>> {
    (1..len+1).map(
        |x| (1..len+1).map(
            |y| x*y
        ).collect()
    ).collect()
}
