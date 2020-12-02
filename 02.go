package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	var part1, part2 int
	re := regexp.MustCompile(`(\d+)\-(\d+) (\w)\: (\w+)`)
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		tokens := re.FindStringSubmatch(line)
		a, _ := strconv.ParseInt(tokens[1], 0, 0)
		b, _ := strconv.ParseInt(tokens[2], 0, 0)
		letter := tokens[3]
		password := tokens[4]
		n := strings.Count(password, letter)
		if n >= int(a) && n <= int(b) {
			part1++
		}
		if (password[a-1] == letter[0]) != (password[b-1] == letter[0]) {
			part2++
		}
	}
	fmt.Println(part1)
	fmt.Println(part2)
}
