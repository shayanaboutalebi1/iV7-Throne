# GitHub API Examples

### Create repo with curl
```bash
curl -L -X POST https://api.github.com/user/repos \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -d '{"name":"iV7-Throne","private":true,"description":"Archival research workspace"}'
```

### Push with gh CLI
```bash
git init
git add .
git commit -m "Initial iV7-Throne public-records scaffold"
gh repo create shayanaboutalebi1/iV7-Throne --private --source=. --push
```
