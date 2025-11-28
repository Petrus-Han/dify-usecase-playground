# Dify Use Case Playground

> 🎯 A collection of real-world Dify workflow DSL examples and use cases

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## Introduction

**Dify Use Case Playground** is a personal open-source repository that collects practical Dify workflow DSL examples and use cases. This repository serves as a learning resource and reference for building production-ready workflows using Dify's workflow engine.

## What's Inside

This repository contains:

- 📋 **Workflow DSL Files** (`.yml`) - Complete workflow definitions ready to import into Dify
- 📖 **Documentation** (`README.md`) - Detailed explanations for each use case
- 🎨 **Best Practices** - Real-world patterns and solutions

## Features

- ✅ Production-ready workflows
- ✅ Comprehensive documentation
- ✅ Easy to import and customize
- ✅ Real-world use cases
- ✅ Best practices and patterns
- 🔒 **Security**: Automated secret scanning via CI/CD

## Use Cases

### 🤖 Automation

- **[Daily News for Slack Channel](./usecases/daily-news-slack/)** - Automated daily news delivery to Slack channels using scheduled triggers

### 💬 Chatbots & Assistants

- **[Slack Trigger News Researcher](./usecases/slack-news-researcher/)** - Intelligent Slack bot with question classification and news research capabilities

## Getting Started

1. **Browse Use Cases**
   - Explore the `usecases/` directory
   - Each use case has its own folder with a `workflow.yml` and `README.md`

2. **Import a Workflow**
   - Open Dify console
   - Import the `.yml` file from the use case folder
   - Follow the setup instructions in the use case README

3. **Customize**
   - Modify the workflow according to your needs
   - Update configuration parameters
   - Test and deploy

## Directory Structure

```
.
├── README.md                 # This file (English)
├── README.zh-Hans.md         # Simplified Chinese
├── README.zh-Hant.md         # Traditional Chinese
├── README.ja.md              # Japanese
├── LICENSE                   # Apache 2.0 License
├── .gitignore               # Git ignore rules
├── .gitleaks.toml          # Secret scanning configuration
├── .github/
│   └── workflows/
│       ├── secret-scanning.yml      # CI/CD secret scanning workflow
│       └── code-language-check.yml  # CI/CD language check workflow
└── usecases/                 # Use case collection
    ├── daily-news-slack/
    │   ├── workflow.yml      # Workflow DSL file
    │   └── README.md         # Use case documentation (English)
    └── slack-news-researcher/
        ├── workflow.yml      # Workflow DSL file
        └── README.md         # Use case documentation (English)
```

## Requirements

- [Dify](https://github.com/langgenius/dify) platform access
- Required plugins and API keys (see individual use case READMEs)

## Security

🔒 **This repository uses automated secret scanning** to prevent accidental commits of sensitive information:

- **CI/CD Integration**: GitHub Actions workflow automatically scans for secrets on every push and pull request
- **Tools Used**: 
  - [Gitleaks](https://github.com/gitleaks/gitleaks) - Comprehensive secret detection
  - Custom pattern matching for common sensitive data
- **What's Checked**: API keys, tokens, passwords, webhook URLs, AWS keys, Slack tokens, and more

**Important**: Never commit sensitive information like API keys, tokens, or credentials. Use environment variables or secure configuration management instead.

## Code Language Policy

🌐 **This project maintains an international positioning.**

- ✅ **Code files may contain Chinese or other languages** - Encouraged for internationalization (i18n) support
- ✅ i18n fields (`zh_Hans`, `zh_Hant`, `ja_JP`, `pt_BR`, etc.) in Dify workflow files are fully supported
- ✅ **Git commit messages must be in English** - To maintain international project positioning
- ✅ **Pull request titles and descriptions must be in English** - For global collaboration
- 📖 Documentation files are available in multiple languages (English, Simplified Chinese, Traditional Chinese, Japanese)

**Note**: CI checks enforce English for git commit messages and PR content, but allow any language in code files for internationalization purposes.

## Contributing

This is a personal project, but suggestions and feedback are welcome! Feel free to:

- Open issues for bugs or feature requests
- Submit pull requests with improvements
- Share your own use cases

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## Author

Personal project by [@petrus](https://github.com/petrus)

---

**Note**: This repository is maintained as a personal learning and reference resource. Use cases are based on real-world scenarios and may require customization for your specific needs.
