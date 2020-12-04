package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Passport map[string]string

func parsePassports(data string) []Passport {
	var passports []Passport
	for _, s := range strings.Split(data, "\n\n") {
		passport := make(Passport)
		for _, field := range strings.Fields(s) {
			split := strings.SplitN(field, ":", 2)
			passport[split[0]] = split[1]
		}
		passports = append(passports, passport)
	}
	return passports
}

func part1(passports []Passport) int {
	required := []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	result := len(passports)
	for _, p := range passports {
		for _, k := range required {
			if _, ok := p[k]; !ok {
				result--
				break
			}
		}
	}
	return result
}

func part2(passports []Passport) int {
	type Validator struct {
		Key    string
		Regexp *regexp.Regexp
		Func   func([]string) bool
	}

	re := func(str string) *regexp.Regexp {
		return regexp.MustCompile(str)
	}

	parseInt := func(s string) int {
		x, _ := strconv.ParseInt(s, 0, 0)
		return int(x)
	}

	validators := []Validator{
		{"byr", re(`(\d{4})`), func(m []string) bool {
			year := parseInt(m[1])
			return year >= 1920 && year <= 2002
		}},
		{"iyr", re(`(\d{4})`), func(m []string) bool {
			year := parseInt(m[1])
			return year >= 2010 && year <= 2020
		}},
		{"eyr", re(`(\d{4})`), func(m []string) bool {
			year := parseInt(m[1])
			return year >= 2020 && year <= 2030
		}},
		{"hgt", re(`(\d+)(cm|in)`), func(m []string) bool {
			height := parseInt(m[1])
			units := m[2]
			if units == "cm" {
				return height >= 150 && height <= 193
			}
			return height >= 59 && height <= 76
		}},
		{"hcl", re(`(#[0-9a-f]{6})`), func(m []string) bool {
			return true
		}},
		{"ecl", re(`(amb|blu|brn|gry|grn|hzl|oth)`), func(m []string) bool {
			return true
		}},
		{"pid", re(`(\d{9})`), func(m []string) bool {
			return true
		}},
	}

	result := len(passports)
	for _, p := range passports {
		for _, v := range validators {
			value := p[v.Key]
			m := v.Regexp.FindStringSubmatch(value)
			if len(m) == 0 || len(m[0]) != len(value) || !v.Func(m) {
				result--
				break
			}
		}
	}
	return result
}

func main() {
	bytes, _ := ioutil.ReadAll(os.Stdin)
	passports := parsePassports(string(bytes))
	fmt.Println(part1(passports))
	fmt.Println(part2(passports))
}
