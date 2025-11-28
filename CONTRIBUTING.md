# Contributing Guidelines

Thank you for your interest in contributing to Dify Use Case Playground!

## Language Requirements

**This project maintains an international positioning. While code may contain Chinese or other languages for internationalization purposes, git commit messages and PR content should be in English.**

### Code Files
- ✅ **Code files may contain Chinese or other languages** - This is encouraged for internationalization (i18n) support
- ✅ i18n fields like `zh_Hans`, `zh_Hant`, `ja_JP`, `pt_BR` in Dify workflow YAML files are fully supported
- ✅ Code comments and strings may be in any language to support international users

### Git & PR Communication
- ✅ **Git commit messages must be in English** - To maintain international project positioning
- ✅ **Pull request titles and descriptions must be in English** - For global collaboration
- ✅ **Issue titles and descriptions should be in English** - For better international visibility

### Documentation
- ✅ Documentation files (like `README.md`) may contain multiple languages for better accessibility

**Note**: CI checks will enforce English for git commit messages and PR content, but allow any language in code files for internationalization purposes.

## Pull Request Process

1. **Fork the repository** and create your branch from `main`
2. **Write your code** following the project's style guidelines
3. **Ensure all code and comments are in English**
4. **Write clear commit messages in English**
5. **Update documentation** if needed
6. **Submit a pull request** with a clear description in English

## Commit Message Guidelines

Write clear, descriptive commit messages in English:

```
feat: add new workflow for email automation
fix: correct timezone handling in schedule trigger
docs: update README with new use case
refactor: simplify agent configuration
```

Use conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

## Code Style

- Follow existing code style and patterns
- Add comments for complex logic (in English)
- Keep functions and variables focused and well-named
- Ensure YAML files are properly formatted

## Testing

- Test your changes locally before submitting
- Ensure workflows can be imported into Dify successfully
- Verify all configurations are correct

## Questions?

If you have questions, please open an issue (in English) and we'll be happy to help!

---

**Remember**: All code, comments, and git messages must be in English. This is enforced by CI checks.

