// ?

package kata

func HorizontalWins(board [3][3]int) int {
  for i,_ := range board{
    if board[i][0] != 0 && board[i][0] == board[i][1] && board[i][1] == board[i][2] {return board[i][0]}
  }
  return 0
}
func VerticalWins(board[3][3]int) int {
  for i,_ := range board{
    if board[0][i] != 0 && board[0][i] == board[1][i] && board[1][i] == board[2][i] {return board[0][i]}
  }
  return 0
}
func DiagonalWins(board[3][3]int) int{
  if board[0][0] != 0 && board[0][0] == board[1][1] && board[1][1] == board[2][2] {return board[0][0]}
  if board[0][2] != 0 && board[0][2] == board[1][1] && board[1][1] == board[2][0] {return board[0][2]}
  return 0
}
func IsIncomplete(board[3][3]int) int{
  for _,row := range board{
    if row[0] == 0 || row[1] == 0 || row[2] == 0 { return -1}
  }
  return 0
}

func IsSolved(board [3][3]int) int {
  wins := VerticalWins(board) + HorizontalWins(board) + DiagonalWins(board)
  if wins > 0 {return wins}
  return IsIncomplete(board)
}

