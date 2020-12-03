package main

import (
	"bufio"
	"fmt"
	"os"
)

type Vector struct {
	X int
	Y int
}

func hits(grid []string, dir Vector) int {
	var result int
	var pos Vector
	size := Vector{len(grid[0]), len(grid)}
	for pos.Y < size.Y {
		if grid[pos.Y][pos.X%size.X] == '#' {
			result++
		}
		pos.X += dir.X
		pos.Y += dir.Y
	}
	return result
}

func main() {
	var grid []string
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		grid = append(grid, scanner.Text())
	}

	// part 1
	fmt.Println(hits(grid, Vector{3, 1}))

	// part 2
	dirs := []Vector{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}
	product := 1
	for _, d := range dirs {
		product *= hits(grid, d)
	}
	fmt.Println(product)
}
