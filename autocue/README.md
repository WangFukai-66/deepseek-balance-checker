# 提词器（TXT+DOCX）
macOS 快捷指令一键启动本地网页提词器，支持txt、docx文稿，自动滚动，可调速度、字号，支持全屏。

## ✨功能
- 读取本地 `.txt` / `.docx` 文件
- 文本向上滚动，可调节滚动速度、字体大小
- 全屏模式，滚动到底自动停止

## 🚀使用
### AppleScript脚本
```applescript
on run {input, parameters}
	tell application "Microsoft Edge"
		open POSIX file "/Users/kk/MyScripts/shortcuts/autocue.html"
		activate
	end tell
	return input
end run
```
路径需与autocue.html实际存放位置保持一致；切换Safari只需修改脚本内浏览器名称。
操作步骤:
1. 运行脚本，Edge自动打开提词器页面

2. 选择本地txt/docx文稿

3. 调节速度、字号，点击开始滚动；支持暂停、重置、全屏

⚠️注意

1. docx解析需要联网加载依赖库

2. 更改html文件位置，务必同步修改AppleScript中的文件路径
直接保存为 `README.md`，放到autocue文件夹，git提交即可。
