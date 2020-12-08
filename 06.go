package main

import (
	"fmt"
	"io/ioutil"
	"math/bits"
	"os"
	"strings"
)

func parse(data string) [][]uint {
	var groups [][]uint
	for _, s := range strings.Split(data, "\n\n") {
		fields := strings.Fields(s)
		group := make([]uint, len(fields))
		for i, f := range fields {
			for _, c := range f {
				group[i] |= 1 << (c - 'a')
			}
		}
		groups = append(groups, group)
	}
	return groups
}

func main() {
	bytes, _ := ioutil.ReadAll(os.Stdin)
	groups := parse(string(bytes))
	var part1, part2 int
	for _, group := range groups {
		a := group[0]
		b := group[0]
		for _, g := range group {
			a |= g
			b &= g
		}
		part1 += bits.OnesCount(a)
		part2 += bits.OnesCount(b)
	}
	fmt.Println(part1)
	fmt.Println(part2)
}
