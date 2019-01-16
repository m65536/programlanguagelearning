package main

import (
  
  "net/http"
  "encoding/json"
  "io/ioutil"
  "log"
  
)

type Profile struct {
  Name    string
  Hobbies []string
}



func main() {
    url := "http://localhost:8001"

    req, _ := http.NewRequest("GET", url, nil)

    req.Header.Add("accept", "application/json")
    req.Header.Add("content-type", "application/json")

    res, err := http.DefaultClient.Do(req)

    if err != nil {
          log.Fatal(err) 
    }
  

    var user=Profile{}
    body, _ := ioutil.ReadAll(res.Body)
    json.Unmarshal(body, &user)
    println(user.Name)

}
