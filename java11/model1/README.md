
* 下载
官网下载`jdk-11.0.1_osx-x64_bin.tar.gz`

* 安装
```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-11.0.1.jdk/Contents/Home

```

# test model1
```
javac -d mods/model1 src/module-info.java src/top/moxingwang/model1/Main1.java
java --module-path mods -m  model1/top.moxingwang.model1.Main1
```

# reference 
* [A Guide to Java 9 Modularity](https://www.baeldung.com/java-9-modularity)