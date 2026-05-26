# md-to-txt

## 中文

一个很小的 Markdown 转 TXT 脚本。

我写这个脚本只是因为 DeepSeek 网页版不认识 `.md` 文件；把 Markdown 先转成 `.txt` 后，就可以更直接地上传或粘贴给网页工具使用。

### 使用方法

1. 准备一个或多个 `.md` 文件。
2. 把文件拖拽到 `md_to_txt_drag.py` 上。
3. 程序会在每个 `.md` 文件旁边生成对应的 `.txt` 文件。
4. 转换完成后，窗口会等待 5 秒自动关闭。

### 规则

- 只转换 `.md` 文件。
- 非文件路径会跳过。
- 非 `.md` 文件会跳过。
- 如果同名 `.txt` 已存在，程序会生成 `_2.txt`、`_3.txt` 这样的新文件名，不覆盖旧文件。
- 输出文件使用 UTF-8 编码。

### 运行环境

需要 Python 3。

## English

A tiny script for converting Markdown files to TXT files.

I wrote this script simply because the DeepSeek web interface did not recognize `.md` files. Converting Markdown to `.txt` first makes it easier to upload or paste the content into web tools.

### Usage

1. Prepare one or more `.md` files.
2. Drag the files onto `md_to_txt_drag.py`.
3. The script creates matching `.txt` files next to each `.md` file.
4. After conversion, the window waits 5 seconds and closes automatically.

### Rules

- Only `.md` files are converted.
- Non-file paths are skipped.
- Non-`.md` files are skipped.
- If a matching `.txt` file already exists, the script creates `_2.txt`, `_3.txt`, and so on instead of overwriting the old file.
- Output files are written as UTF-8.

### Requirements

Python 3 is required.
