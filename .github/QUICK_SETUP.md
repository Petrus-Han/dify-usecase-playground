# Quick Setup Guide for Open Source Project

This guide helps you quickly set up your GitHub repository as an open-source project with proper protection rules.

## Step 1: Enable Branch Protection

### Via GitHub Web Interface

1. Go to your repository on GitHub
2. Click **Settings** → **Branches**
3. Click **Add rule**
4. Branch name: `main` (or `master`)
5. Enable these settings:

```
☑ Require a pull request before merging
  ☑ Require approvals: 1
  ☑ Dismiss stale pull request approvals when new commits are pushed

☑ Require status checks to pass before merging
  ☑ Require branches to be up to date before merging
  ☑ Select: Secret Scanning, Code Language Check

☑ Require conversation resolution before merging
☑ Include administrators
☑ Do not allow bypassing the above settings
```

6. Click **Create**

### Via GitHub CLI (Alternative)

```bash
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["Secret Scanning","Code Language Check"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null
```

## Step 2: Verify CI Workflows

1. Go to **Actions** tab
2. Ensure workflows are enabled:
   - Secret Scanning
   - Code Language Check
3. Test by creating a test PR

## Step 3: Configure Repository Settings

### General Settings

1. **Settings** → **General**
2. Enable:
   - ☑ **Issues** (for bug reports and feature requests)
   - ☑ **Discussions** (optional, for community discussions)
   - ☑ **Projects** (optional, for project management)

### Features

1. **Settings** → **General** → **Features**
2. Enable:
   - ☑ **Issues**
   - ☑ **Pull requests**
   - ☑ **Discussions** (optional)
   - ☑ **Wikis** (optional)

### Security

1. **Settings** → **Security**
2. Enable:
   - ☑ **Dependency graph**
   - ☑ **Dependabot alerts**
   - ☑ **Dependabot security updates**

## Step 4: Add Repository Topics

1. Go to repository main page
2. Click the gear icon next to "About"
3. Add topics: `dify`, `workflow`, `dsl`, `automation`, `ai`, `open-source`

## Step 5: Create Initial Issues Template

Create `.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Bug Report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

## Description
A clear description of the bug.

## Steps to Reproduce
1. 
2. 
3. 

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Environment
- Dify Version: 
- OS: 
- Browser (if applicable): 

## Additional Context
Any other relevant information.
```

## Step 6: Enable Community Health Files

The repository already includes:
- ✅ `CONTRIBUTING.md` - Contribution guidelines
- ✅ `SECURITY.md` - Security policy
- ✅ `.github/CODEOWNERS` - Code owners for auto-review requests
- ✅ `.github/pull_request_template.md` - PR template

## Step 7: Test the Setup

1. Create a test branch: `git checkout -b test/branch-protection`
2. Make a small change
3. Push: `git push origin test/branch-protection`
4. Create a Pull Request
5. Verify:
   - ✅ CI checks run automatically
   - ✅ Direct merge is blocked
   - ✅ Approval is required

## Verification Checklist

- [ ] Branch protection rule is active
- [ ] CI workflows are running
- [ ] Direct push to main is blocked
- [ ] PR requires approval
- [ ] PR requires CI checks to pass
- [ ] CODEOWNERS file is in place
- [ ] Security policy is visible
- [ ] Contributing guidelines are accessible

## Next Steps

1. **Add a LICENSE file** (already done - Apache 2.0)
2. **Create a CHANGELOG.md** (optional)
3. **Set up release workflow** (optional)
4. **Enable GitHub Sponsors** (if applicable)
5. **Add project description** on GitHub

---

**Congratulations!** Your repository is now properly configured as an open-source project with protection rules in place.

