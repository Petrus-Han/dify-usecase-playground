# Security Policy

## 🔒 Secret Scanning

This repository uses automated secret scanning to prevent accidental commits of sensitive information.

### How It Works

1. **GitHub Actions Workflow**: Automatically runs on every push and pull request
2. **Gitleaks**: Scans the entire codebase for common secret patterns
3. **Custom Pattern Matching**: Additional checks for project-specific patterns

### What Gets Scanned

The CI checks for:

- API keys (various formats)
- Authentication tokens
- Passwords and credentials
- Webhook URLs with embedded tokens
- Slack tokens (`xoxb-`, `xoxa-`, `xoxp-`, etc.)
- AWS access keys (`AKIA...`)
- Database connection strings
- Private keys and certificates
- And many more patterns...

### If You Accidentally Commit Secrets

If you accidentally commit sensitive information:

1. **Immediately rotate/revoke** the exposed credentials
2. **Remove the secret** from the commit history using `git rebase` or `git filter-branch`
3. **Force push** the cleaned history (⚠️ coordinate with team first)
4. **Consider using** [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/) for large repositories

### Best Practices

✅ **DO:**
- Use environment variables for sensitive data
- Use Dify's built-in environment variable management
- Store secrets in secure vaults (e.g., GitHub Secrets, HashiCorp Vault)
- Use placeholder values in example files (e.g., `your-api-key-here`)

❌ **DON'T:**
- Commit API keys or tokens directly in code
- Hardcode credentials in workflow files
- Share secrets in pull request descriptions
- Include `.env` files in commits

### Configuration Files

- `.gitleaks.toml` - Gitleaks configuration and allowlist
- `.github/workflows/secret-scanning.yml` - CI workflow definition
- `.gitignore` - Files and patterns to exclude from version control

### Reporting Security Issues

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT** create a public issue
2. Contact the repository maintainer directly
3. Provide details about the vulnerability
4. Allow time for the issue to be addressed before public disclosure

---

**Remember**: Security is everyone's responsibility. When in doubt, don't commit it!

