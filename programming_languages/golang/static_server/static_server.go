package main

import (
  "log"
  "net/http"
  "runtime"
  "os/exec"
  "fmt"
)

func openBrowser(url string) {
  var err error

  switch runtime.GOOS {
  case "linux":
    err = exec.Command("xdg-open", url).Start()
  case "windows":
    err = exec.Command("rundll32", "url.dll,FileProtocolHandler", url).Start()
  case "darwin":
    err = exec.Command("open", url).Start()
  default:
    err = fmt.Errorf("Unsupported platform!")
  }

  if err != nil {
    log.Fatal(err)
  }
}

func main() {
  fs := http.FileServer(http.Dir("./static"))
  http.Handle("/", fs)

  openBrowser("http://localhost:3000/")

  err := http.ListenAndServe(":3000", nil)
  log.Println("Listening on localhost:3000 ...")

  if err != nil {
    log.Fatal(err)
  }
}
