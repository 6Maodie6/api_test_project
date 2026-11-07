# Python API Automation Testing Project

基于 Python + Requests + Pytest 的接口自动化测试项目，使用 JSONPlaceholder 作为测试 API 服务，实践接口请求封装、测试用例设计、参数化、异常处理、日志记录和测试报告生成。

## 1. 项目介绍

本项目用于学习和实践 Python 接口自动化测试，主要覆盖：

- GET、POST 接口测试
- 接口响应状态码和 JSON 数据校验
- 参数化测试
- 边界值测试和异常场景测试
- 请求超时配置测试
- 网络异常模拟测试
- API Client 公共请求封装
- 公共断言方法封装
- 日志记录
- Allure 测试报告

## 2. 技术栈

| 技术 | 用途 |
|---|---|
| Python | 编程语言 |
| Requests | HTTP 接口请求 |
| Pytest | 自动化测试框架 |
| Allure | 测试报告 |
| Git | 版本管理 |

## 3. 项目结构

```text
api_test_project/
├── common/
│   ├── assertions.py
│   └── client.py
├── config/
│   └── settings.py
├── data/
│   └── post_cases.json
├── logs/
├── tests/
│   ├── test_client_config.py
│   ├── test_client_errors.py
│   ├── test_create_post.py
│   ├── test_post_workflow.py
│   └── test_posts.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 4. 环境准备

建议使用 Python 3.10 或以上版本。

安装项目依赖：

```bash
pip install -r requirements.txt
```

## 5. 运行测试

运行全部测试：

```bash
python -m pytest -v
```

生成 Allure 测试结果：

```bash
python -m pytest --alluredir=allure-results
```

生成并打开 Allure 报告：

```bash
allure serve allure-results
```

## 6. 测试内容

| 测试类型 | 测试内容 |
|---|---|
| 功能测试 | 获取文章、创建文章 |
| 参数化测试 | 使用多组文章 ID 验证接口 |
| 边界值测试 | 有效 ID、无效 ID |
| 异常测试 | Timeout、ConnectionError |
| 配置测试 | 默认超时时间、自定义超时时间 |
| 资源管理 | Session 关闭验证 |
| 工作流测试 | 创建文章后查询并校验数据 |

## 7. 测试服务

本项目使用 JSONPlaceholder 提供的模拟 REST API：

https://jsonplaceholder.typicode.com

注意：JSONPlaceholder 是模拟 API 服务，POST 等写入操作不会真正持久化数据。

## 8. 项目说明

本项目为个人学习与实战项目，后续将继续完善测试覆盖率、测试报告、持续集成和项目工程化能力。
