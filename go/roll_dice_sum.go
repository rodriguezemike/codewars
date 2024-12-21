//https://www.codewars.com/kata/56f78a42f749ba513b00037f/train/go

package kata

//Bernoulli Distribution
func RolldiceSumProb(sum, dice int) float64 {
  if dice == 0 && sum == 0 {
    return 1
  } else if sum < dice || sum > 6 * dice {
    return 0
  } else {
    sumProb := 0.0
    for i := 1; i <= 6; i++ {
      sumProb += RolldiceSumProb(sum - i, dice - 1)
    }
    return sumProb / 6
  }
}
