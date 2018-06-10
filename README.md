深入理解 RPC : 基于 Python 自建分布式高并发 RPC 服务
--
本小册代码运行环境为Mac和Linux，如果是windows用户，建议安装虚拟机

小册代码均基于Python2.7编写，第15章之前的所有代码只使用了内置library，没有任何第三方依赖项

第15章之后分布式RPC服务实践因为要用到zookeeper，所以需要安装kazoo库来和zk交互
```
pip install kazoo
```

安装zookeeper可以考虑使用docker进行快速安装
```
docker pull zookeeper
docker run -p 2181:2181 zookeeper
```

代码上如有任何问题，可以在官方的微信交流群里进行讨论
