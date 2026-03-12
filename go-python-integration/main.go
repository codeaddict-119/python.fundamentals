package main

import (
	"fmt"
	"log"
	"os/exec"
	"strings"
)

func main() {
	// Numbers to send to Python
	num1 := "5"
	num2 := "7"

	// Run Python script
	cmd := exec.Command("py", "add.py", num1, num2)

	output, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatalf("Error running Python script: %v\nOutput: %s", err, output)
	}

	// Clean output (remove newline)
	result := strings.TrimSpace(string(output))

	fmt.Println("Result from Python:", result)
}
