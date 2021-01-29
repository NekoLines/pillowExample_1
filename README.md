# Pillow

![](test.png)

通过Pillow模块和Python3自动生成大鸟转转转酒吧梗图。具体的说明请参考[这个链接](https://0w0.in/pscdnzzzgt/)

值得注意的是，本程序 *不* 包含开发所需的字体文件，请自行下载并放到相同目录即可执行。

字体文件为*更纱黑体*，前往其 release 下载 [sarasa-gothic-ttc-0.17.0.7z](https://github.com/be5invis/Sarasa-Gothic/releases/tag/v0.17.0) 并解压出其中的 sarasa-bolditalic.ttc 字体。放到 makeTest.py 同目录下即可。

## 食用方法

- 本地运行

前往 release 页面下载文件，解压后执行：`python3 cmd.py xxx yyy` (xxx 和 yyy 替换成自己准备p上去的字)，然后程序就会在当前目录生成一张 `meme.png`。

- HTTP 服务

访问 <http://127.0.0.1:11451/api/v1/make> ，并填写表单，服务器会发送文件给你。你可以选择直接运行 `python3 server.py`，如果是公开接口，建议使用 gunicon 作为服务。

你需要正确填写表单才能获得图片，表单有两个 key：first 和 second，分别对应上面一行和下面一行。

运行示例：

```bash
# 本地测试运行
python3 server.py
curl -X POST http://127.0.0.1:11451/api/v1/make -d "first=锦鲤&second=太强了！！" --output meme.png

# 使用 gunicon
pip3 install gunicon
gunicon -w 2 -b 0.0.0.0:11451 -t 0 web:app --log-level critical
```

> 如果需要更改监听 ip 或 端口，请自行修改 `server.py` 的 `app.run()` 方法参数
