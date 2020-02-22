##部署
1. docker pull hub.c.163.com/tianshuhua/gitbook:latest
2. docker run -p 4000:4000 -it -v "/mnt/gitbook/docs:/srv/gitbook" -v "/mnt/gitbook/html:/srv/html"  hub.c.163.com/tianshuhua/gitbook bash
3. 复制好目录到服务器上后
4. gitbook init
5. gitbook build
6. gitbook serve .


```
---TAGStes
```

* hellp
