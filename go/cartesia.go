/*

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


This is a special case of the balance algorithms, open and closed parens, etc. Here want to make sure we end up at the same place we start
Which we can all 0. Each step takes us futher or closer to it
Order doesn't matter but it all has to balance


*/

package kata


func IsValidWalk(walk []rune) bool {
  north_south := 0
  east_west := 0
  if len(walk) != 10 {
    return false
  }
  for i:= 0; i < len(walk); i++{
    if walk[i] == 'n'{
      north_south += 1
    } else if walk[i] == 's'{
      north_south -= 1
    } else if walk[i] == 'e' {
      east_west += 1
    } else {
      east_west -= 1
    }
  }
  return north_south == 0 && east_west == 0

