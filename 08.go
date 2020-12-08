package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

type Instruction struct {
	Op  string
	Arg int
}

type Program []Instruction

func parseProgram(r io.Reader) Program {
	var program Program
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		arg, _ := strconv.ParseInt(fields[1], 0, 0)
		program = append(program, Instruction{fields[0], int(arg)})
	}
	return program
}

func runProgram(program Program) (int, bool) {
	var ip, acc int
	seen := make(map[int]bool)
	for ip < len(program) {
		if seen[ip] {
			return acc, false
		}
		seen[ip] = true
		op := program[ip].Op
		arg := program[ip].Arg
		switch op {
		case "acc":
			acc += arg
		case "jmp":
			ip += arg - 1
		}
		ip++
	}
	return acc, true
}

func part1(program Program) int {
	acc, _ := runProgram(program)
	return acc
}

func part2(program Program) int {
	for i := 0; i < len(program); i++ {
		instruction := program[i]
		switch instruction.Op {
		case "jmp":
			program[i].Op = "nop"
		case "nop":
			program[i].Op = "jmp"
		}
		acc, ok := runProgram(program)
		program[i] = instruction
		if ok {
			return acc
		}
	}
	return 0
}

func main() {
	program := parseProgram(os.Stdin)
	fmt.Println(part1(program))
	fmt.Println(part2(program))
}
