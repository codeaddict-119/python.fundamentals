package main

import (
	"fmt"
	"os/exec"
	"strings"
)

func main() {

	cmd := exec.Command("python", "add.py")

	cmd.Stdin = strings.NewReader("5\n7\n")

	out, err := cmd.Output()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println("Result:", string(out))
}
