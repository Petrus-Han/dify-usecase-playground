# Branch Protection Setup Guide

This guide explains how to set up branch protection rules for this open-source project on GitHub.

## Why Branch Protection?

Branch protection rules help maintain code quality and prevent accidental changes to important branches by:
- Requiring pull request reviews before merging
- Requiring CI checks to pass
- Preventing force pushes and branch deletion
- Ensuring linear history

## Setup Steps

### 1. Navigate to Repository Settings

1. Go to your GitHub repository
2. Click on **Settings** tab
3. Click on **Branches** in the left sidebar

### 2. Add Branch Protection Rule

1. Click **Add rule** or **Add branch protection rule**
2. In the **Branch name pattern** field, enter:
   - `main` (or `master` if that's your default branch)

### 3. Configure Protection Rules

Enable the following settings:

#### ✅ Required Settings

- **☑ Require a pull request before merging**
  - **☑ Require approvals**: Set to `1` (or more if you have multiple maintainers)
  - **☑ Dismiss stale pull request approvals when new commits are pushed**
  - **☑ Require review from Code Owners** (optional, if you have CODEOWNERS file)

- **☑ Require status checks to pass before merging**
  - **☑ Require branches to be up to date before merging**
  - Select the following required status checks:
    - `Secret Scanning` (from `.github/workflows/secret-scanning.yml`)
    - `Code Language Check` (from `.github/workflows/code-language-check.yml`)

- **☑ Require conversation resolution before merging**

- **☑ Require signed commits** (optional, but recommended for security)

- **☑ Require linear history** (optional, prevents merge commits)

- **☑ Include administrators** (recommended - applies rules to admins too)

#### ⚠️ Restrictive Settings (Recommended)

- **☑ Do not allow bypassing the above settings**
- **☑ Restrict who can push to matching branches**: Only repository administrators
- **☑ Allow force pushes**: ❌ Disabled
- **☑ Allow deletions**: ❌ Disabled

### 4. Save the Rule

Click **Create** or **Save changes** to apply the branch protection rule.

## Recommended Additional Settings

### Protected Tags

1. Go to **Settings** → **Tags**
2. Click **Add rule**
3. Pattern: `v*` (protect version tags)
4. Enable:
   - **☑ Restrict who can create matching tags**: Only administrators

### Code Owners (Optional)

Create a `.github/CODEOWNERS` file to automatically request reviews from specific maintainers:

```
# Default owners for everything in the repo
* @your-github-username

# Use case maintainers
/usecases/ @your-github-username

# CI/CD workflows
/.github/workflows/ @your-github-username
```

## Verification

After setting up branch protection:

1. Try to push directly to `main` branch - should be blocked
2. Create a pull request - should require:
   - At least one approval
   - All CI checks to pass
   - Conversation resolution

## Workflow

With branch protection enabled, the typical workflow becomes:

1. **Create a feature branch**: `git checkout -b feature/new-use-case`
2. **Make changes and commit**: `git commit -m "feat: add new use case"`
3. **Push to remote**: `git push origin feature/new-use-case`
4. **Create Pull Request** on GitHub
5. **Wait for CI checks** to complete
6. **Request review** from maintainers
7. **Address review feedback** if needed
8. **Merge** after approval and all checks pass

## Troubleshooting

### CI Checks Not Showing Up

- Ensure workflow files are in `.github/workflows/` directory
- Check that workflows are triggered on `pull_request` events
- Verify workflow files have valid YAML syntax

### Cannot Push to Protected Branch

- This is expected behavior
- Always work in feature branches and use Pull Requests
- If you need to push directly (emergency fix), temporarily disable protection (not recommended)

### PR Shows "Required checks not found"

- Make sure the workflow has run at least once
- Check the Actions tab to see if workflows are running
- Verify branch protection is checking the correct workflow names

## Security Best Practices

1. **Never disable branch protection** for convenience
2. **Use CODEOWNERS** to ensure critical files are reviewed
3. **Require signed commits** for better security
4. **Keep protection rules strict** - it's better to be safe than sorry
5. **Review all PRs** before merging, even from trusted contributors

---

**Note**: These settings ensure that all changes go through proper review and testing before being merged into the main branch, maintaining code quality and project integrity.

