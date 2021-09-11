package main

import (
	"flag"
	"fmt"
	"net"
	"sync"
)

var wg = sync.WaitGroup{}

func portscan(target string, n int) {
	channel := make(chan int, 100)
	for j := 0; j < n; j++ {
		wg.Add(2)
		//Sender
		go func(channel chan<- int, j int) {
			defer wg.Done()
			target := fmt.Sprintf("%s:%v", target, j)
			conn, err := net.Dial("tcp", target)
			if err != nil {
				return
			}
			channel <- j
			conn.Close()
		}(channel, j)

		//Receive
		go func(channel <-chan int) {
			defer wg.Done()
			result := <-channel
			fmt.Println("Open port: ", result)
		}(channel)
	}
	wg.Wait()
}
func main() {
	//Domain
	var target string
	flag.StringVar(&target, "d", "127.0.0.1", "Specify a Domain/ip")

	//Number of ports
	var ports bool
	flag.BoolVar(&ports, "p-", false, "Scan all Ports")
	flag.Parse()
	if ports {
		n := 65535
		fmt.Printf("[++]Scanning [%v] Ports\n", n)
		portscan(target, n)
	} else {
		n := 10000
		fmt.Printf("[++]Scanning [%v] Ports\n", n)
		portscan(target, n)
	}
}
