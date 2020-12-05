package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var ids []int
	r := strings.NewReplacer("F", "0", "B", "1", "L", "0", "R", "1")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		id, _ := strconv.ParseInt(r.Replace(scanner.Text()), 2, 0)
		ids = append(ids, int(id))
	}
	sort.Ints(ids)

	// part 1
	fmt.Println(ids[len(ids)-1])

	// part 2
	for i := 1; i < len(ids); i++ {
		if ids[i]-ids[i-1] == 2 {
			fmt.Println(ids[i] - 1)
		}
	}
}
