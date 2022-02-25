# Gitlab CI/CD Snippets

## Script Execution

```
variables:
 DBB_HOME: "/usr/lpp/dbb/v1r0"
 DBB_EXTENSIONS: "/var/dbb/extensions"
Code Review:
 stage: Analysis
 tags: [z/OS]
 variables:
 GIT_STRATEGY: none
 script:
 - cd $CI_PROJECT_DIR/BUILD-$CI_PIPELINE_ID/build*
 - export BUILDPATH=`pwd`
 - $DBB_HOME/bin/groovyz $DBB_EXTENSIONS/idz-codereview/RunCodeReview.groovy --workDir
$BUILDPATH --properties $DBB_EXTENSIONS/idz-codereview/codereview.genapp.properties
```
