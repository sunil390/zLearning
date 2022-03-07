# Ansible Snippets

```sh
- name: Convert a local JCL file to IBM-037 and submit the job
  zos_job_submit:
    src: /Users/maxy/ansible-playbooks/provision/sample.jcl
    location: LOCAL
    wait: false
    encoding:
      from: ISO8859-1
      to: IBM-037
```

```sh
- name: Submit long running PDS job, and wait for the job to finish
  zos_job_submit:
    src: TEST.UTILs(LONGRUN)
    location: DATA_SET
    wait: true
    wait_time_s: 30
```
