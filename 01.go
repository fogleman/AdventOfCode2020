package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func find(values map[int]bool, sum, depth int) int {
	if sum < 0 {
		return -1
	}
	if depth == 1 {
		if values[sum] {
			return sum
		}
		return -1
	}
	for value, ok := range values {
		if !ok {
			continue
		}
		values[value] = false
		product := find(values, sum-value, depth-1)
		values[value] = true
		if product >= 0 {
			return product * value
		}
	}
	return -1
}

func main() {
	values := make(map[int]bool)
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		value, _ := strconv.ParseInt(scanner.Text(), 0, 0)
		values[int(value)] = true
	}

	fmt.Println(find(values, 2020, 2))
	fmt.Println(find(values, 2020, 3))
}
