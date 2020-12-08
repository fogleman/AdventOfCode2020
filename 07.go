package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Rule map[string]int
type Rules map[string]Rule

func parseRules(r io.Reader) Rules {
	rules := make(Rules)
	re := regexp.MustCompile(`(\d+) ([^,]+)`)
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		line := scanner.Text()
		line = strings.TrimSuffix(line, ".")
		line = strings.ReplaceAll(line, " bags", "")
		line = strings.ReplaceAll(line, " bag", "")
		split := strings.Split(line, " contain ")
		rule := make(Rule)
		for _, m := range re.FindAllStringSubmatch(split[1], -1) {
			x, _ := strconv.ParseInt(m[1], 0, 0)
			rule[m[2]] = int(x)
		}
		rules[split[0]] = rule
	}
	return rules
}

func canContain(rules Rules, color, target string) bool {
	for c := range rules[color] {
		if c == target || canContain(rules, c, target) {
			return true
		}
	}
	return false
}

func canContainSum(rules Rules, color string) int {
	var sum int
	for c := range rules {
		if canContain(rules, c, color) {
			sum++
		}
	}
	return sum
}

func bagCount(rules Rules, color string) int {
	var sum int
	for c, n := range rules[color] {
		sum += n + n*bagCount(rules, c)
	}
	return sum
}

func main() {
	rules := parseRules(os.Stdin)
	fmt.Println(canContainSum(rules, "shiny gold"))
	fmt.Println(bagCount(rules, "shiny gold"))
}
