package main

import (
  "encoding/json"
  "net/http"
)

type Profile struct {
  Name    string
  Hobbies []string
}

func main() {
  println("server started")
  http.HandleFunc("/", foo)
  http.ListenAndServe(":8001", nil)
}

func foo(w http.ResponseWriter, r *http.Request) {
  profile := Profile{"Alex", []string{"snowboarding", "programming"}}
  profile.Name = "111111111"

  js, err := json.Marshal(profile)
  if err != nil {
    http.Error(w, err.Error(), http.StatusInternalServerError)
    return
  }

  w.Header().Set("Content-Type", "application/json")
  w.Write(js)
}
