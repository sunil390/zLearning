# azure DevOps

1. Project Settings -> Repos -> Repositories -> Security -> {Repo} Build Service ( { Project} ) -> Allow - Contribute, Create Branch, Create Tag.
2. checkout section
```
- checkout: self
  persistCredentials: true
```
3. Git Push
```
    git config --global user.email "sunil.sukumaran@atos.net" & git config --global user.name "Sunil Sukumaran"
    git add -A
    git commit -m "Commit After Run [skip ci]"
    git push origin HEAD:main
```
