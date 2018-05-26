代码基于Python2.7编写，第15章之前的所有代码只使用内置library，没有其它任何依赖项

第15章分布式RPC服务实践因为要用到zookeeper，所以需要安装kazoo库
```
pip install kazoo
```

安装zookeeper可以考虑使用docker进行快速安装
```
docker pull zookeeper
docker run -p 2181:2181 zookeeper
```

![](qrcode.jpg)

请关注公众号「码洞」，进入讨论组解答疑惑
