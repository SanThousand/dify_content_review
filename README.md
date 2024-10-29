# dify内容审查 API

## 概述

这是一个基于 FastAPI 的 API，用于处理内容审查请求。API 会检查用户输入是否包含从文件 (`key_word.txt`) 中加载的敏感词。如果用户输入中包含任何敏感词，API 会标记内容并返回预设的响应，指示内容违反了使用政策。

## 功能

- **内容审查**：检查用户输入是否包含敏感词。
- **Ping 端点**：提供一个简单的健康检查端点。
- **身份验证**：使用 Bearer 令牌身份验证来保护 API。
- **错误处理**：包括对文件操作和身份验证的健壮错误处理。

## 先决条件

- Python 3.10
- FastAPI
- Uvicorn

## 安装

1. **克隆仓库**

   ```bash
   git clone https://github.com/SanThousand/dify_content_review.git
   ```

2. **安装依赖**

   ```bash
   pip install fastapi[all] uvicorn
   ```

3. **创建 `key_word.txt`**

   在项目的根目录下创建一个名为 `key_word.txt` 的文件。添加敏感词，每行一个。

   示例：
   ```
   坏词1
   坏词2
   坏词3
   ```

## 运行 API

1. **启动 API**

   ```bash
   python content_review.py
   ```

   API 将在 `http://0.0.0.0:8000/api/dify/receive` 上可用。
